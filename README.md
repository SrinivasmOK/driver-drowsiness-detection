# 🛑 Driver Drowsiness Detection System (Real-Time)

This project is a real-time driver drowsiness detection system that monitors up to 5 faces using MediaPipe, OpenCV, and Pygame. It detects eye closure and yawning, and plays alert sounds to prevent accidents.

---

## 🎯 Features

✅ Real-time detection of drowsiness and yawning  
✅ Multi-face support (up to 5 people)  
✅ Alert sounds for yawning and sleep  
✅ Accurate detection using MediaPipe Face Mesh  
✅ Optimized for real-time webcam use  

---

## 📸 Sample Output

If `sample_image(1).jpg`, `sample_image(2).jpg`, and `sample_image(3).jpg` exist, you’ll see sample frames below:

![Sample 1](sample_image(1).jpg)
![Sample 2](sample_image(2).jpg)
![Sample 3](sample_image(3).jpg)

---

## 🧠 How It Works

1. **MediaPipe Face Mesh** detects 468 facial landmarks.  
2. **EAR (Eye Aspect Ratio)** is calculated to detect drowsiness.  
3. **Lip distance** is calculated to detect yawning.  
4. Alerts are triggered if:
   - EAR < threshold → 🔔 Sleep Alert
   - Lip distance > threshold → 🔔 Yawn Alert

---

## 🗂️ Project Structure
















