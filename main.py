import cv2
import mediapipe as mp
import numpy as np
import pygame
import time

# Initialize MediaPipe and Pygame
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, max_num_faces=5)
mp_drawing = mp.solutions.drawing_utils

pygame.mixer.init()
yawn_sound = pygame.mixer.Sound("yawn_alert.mp3")
sleep_sound = pygame.mixer.Sound("sleep_alert.mp3")

yawn_sound.set_volume(1.0)  # max = 1.0
sleep_sound.set_volume(1.0)

# Eye landmark indices
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [263, 387, 385, 362, 380, 373]

def calculate_ear(eye_landmarks):
    # vertical distances
    A = np.linalg.norm(eye_landmarks[1] - eye_landmarks[5])
    B = np.linalg.norm(eye_landmarks[2] - eye_landmarks[4])
    # horizontal distance
    C = np.linalg.norm(eye_landmarks[0] - eye_landmarks[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Video capture
cap = cv2.VideoCapture(0)

# Drowsiness thresholds
sleep_threshold = 0.25
sleep_frame_limit = 20
sleep_frame_counter = 0  # for only 1 face now (driver)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    driver_face_landmarks = None
    max_area = 0
    selected_coords = None

    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            coords = np.array([(int(pt.x * w), int(pt.y * h)) for pt in landmarks.landmark])
            x_min, y_min = np.min(coords, axis=0)
            x_max, y_max = np.max(coords, axis=0)
            area = (x_max - x_min) * (y_max - y_min)

            if area > max_area:
                max_area = area
                driver_face_landmarks = landmarks
                selected_coords = coords

    if driver_face_landmarks is not None:
        coords = selected_coords

        # EAR calculation
        left_eye = coords[LEFT_EYE]
        right_eye = coords[RIGHT_EYE]
        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)
        avg_ear = (left_ear + right_ear) / 2.0

        # Drowsiness detection
        if avg_ear < sleep_threshold:
            sleep_frame_counter += 1
            if sleep_frame_counter > sleep_frame_limit:
                cv2.putText(frame, "DROWSINESS ALERT!", (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                sleep_sound.play()
        else:
            sleep_frame_counter = 0

        # Yawning detection
        top_lip = coords[13]
        bottom_lip = coords[14]
        mouth_distance = np.linalg.norm(top_lip - bottom_lip)
        if mouth_distance > 30:
            cv2.putText(frame, "YAWNING DETECTED!", (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            yawn_sound.play()

        # Draw face mesh for driver only
        mp_drawing.draw_landmarks(
            frame,
            driver_face_landmarks,
            mp_face_mesh.FACEMESH_TESSELATION,
            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1)
        )

    # Display frame
    cv2.imshow("Driver Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()




