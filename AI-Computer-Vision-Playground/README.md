
1. Real-time Shadow Clone Jutsu | Computer Vision & AI
This project is part of my AI-Computer-Vision-Playground. It demonstrates the use of real-time hand gesture recognition and image segmentation to create an interactive "Shadow Clone" effect inspired by the Naruto series.

While this project is "fun" in nature, the underlying technology has significant applications in Smart Transportation Systems and Human-Machine Interaction (HMI).

Core Technical Logic
The system operates through a multi-stage pipeline:

Hand Landmark Tracking: Using MediaPipe Hands, I track 42 specific 3D coordinates (21 per hand). This allows the system to understand the exact geometry of the hand pose.

Gesture Recognition (ML): I trained a custom classifier using Scikit-learn to recognize the specific "Shadow Clone" hand sign.

Confidence Filtering: To prevent false positives, I implemented a 0.85 (85%) probability threshold. The effect only triggers when the AI is highly certain of the sign.

Selfie Segmentation: Using MediaPipe Selfie Segmentation, the system extracts the user from the background in real-time.

Alpha Blending & Compositing: The extracted user is duplicated and shifted horizontally (15% and 30% offsets). The original user is always rendered on the top layer to maintain a realistic 3D depth.

Engineering Applications (Civil & Transportation)
As a Civil Engineer specialized in Transportation, I developed this to explore:

Driver Monitoring Systems (DMS): Using hand tracking to detect driver distraction or steering wheel engagement.

Pedestrian Behavior Analysis: Utilizing segmentation to extract and analyze pedestrian movement patterns at intersections for safety studies.

Smart Mobility UI: Developing gesture-based controls for vehicle dashboards to minimize physical interaction and maximize road focus.

How to Run
Clone the Repository:

Bash
git clone https://github.com/anmajharul/Majharul.git
cd AI-Computer-Vision-Playground/01_Shadow_Clone_Jutsu
Install Dependencies:
Make sure you have Python 3.10+ installed.

Bash
pip install -r ../requirements.txt
Run the Script:

Bash
python detect_jutsu.py
Controls:

'f': Toggle Fullscreen Mode.

'n': Return to Normal Windowed Mode (with minimize buttons).

'q': Quit the application.


>>>>>>> 3f45c95 (feat: initialize computer vision playground with shadow clone project)

# Author

Majharul Islam  
Civil Engineering Student  
Bangladesh University of Business and Technology (BUBT)

Research Focus:
Transportation Engineering  
Travel Behavior Analysis  
Discrete Choice Modeling


© Majharul Islam – Research Portfolio
=======
[![Portfolio](https://img.shields.io/badge/Website-anmajharul.bd-blue?style=for-the-badge&logo=googlechrome)](https://anmajharul.bd) 

© Majharul Islam – Research Portfolio