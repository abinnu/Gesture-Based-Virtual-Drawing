# Gesture-Based-Virtual-Drawing

✋ Gesture-Based Virtual Drawing 🎨

📌 Overview :

The Gesture-Based Virtual Drawing project is an AI-powered real-time whiteboard application where you can draw on the screen using your hand gestures.
It uses MediaPipe for hand landmark detection, OpenCV for real-time video processing, and a CNN-based gesture classification model to recognize finger positions for different actions:


This project focuses on :

✏️ Drawing on the canvas

🧹 Erasing selected areas

🎨 Changing colors

🛑 Clearing the board

This project integrates Computer Vision + Deep Learning + Gesture Control into an interactive AI tool.


📂 Dataset / Model Source :

🔹 Hand Tracking Model → MediaPipe Hands Solution [Google MediaPipe Hands Solution](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker) 

🔹 Gesture Classification Model → Custom CNN trained on hand landmark coordinates

🔹 Input → Live camera feed from OpenCV


🎯 Features :

✅ Real-time hand gesture recognition

✅ Draw on screen without touching mouse or keyboard

✅ Color selection using gestures

✅ Eraser mode & clear screen functionality

✅ High FPS optimized using OpenCV + MediaPipe

✅ Lightweight, fast & accurate


🧠 Tech Stack :

Language → Python 
Computer Vision → OpenCV
Hand Tracking → Google MediaPipe Hands Solution
Deep Learning → Convolutional Neural Network (CNN)


🔎 How It Works :

1️⃣ Hand Detection 🖐️

Uses MediaPipe Hands to detect 21 key landmarks per hand in real-time.

Calculates finger positions (tip, base, direction).


2️⃣ Gesture Classification 🧠 

Extracts landmark coordinates from MediaPipe.

Feeds them into a CNN model for gesture recognition.


3️⃣ Drawing Actions 🎨

If index finger is raised → Draw mode 🖊️

If both index & middle fingers are up → Eraser mode 🧹

If all fingers closed → Color selection

If five fingers open → Clear board


📈 Future Improvements :

* Add multi-hand drawing support ✍️✍️

* Integrate voice commands for better control 🎙️

* Deploy as a web app using Streamlit or Flask


🤝 Contribution :

Contributions are welcome! 🎉, If you'd like to improve this project, Feel free to:

- **Fork** the repository 🍴
  
- **Create a feature branch**  

- **Submit a pull request** 🚀  

Your feedback, ideas, and suggestions are always appreciated! 🙌


👨‍💻 Author :

Abinnu John Peter.P

📧 Email: abinnu75@gmail.com

🔗 LinkedIn : www.linkedin.com/in/abinnu
