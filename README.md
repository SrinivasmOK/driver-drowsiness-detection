# 🛑 Driver Drowsiness Detection System (Real-Time)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Real--Time-FF0000)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)


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

![Sample 1](sample_image1.png)  
![Sample 2](sample_image2.png)  
![Sample 3](sample_image3.png)


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
















