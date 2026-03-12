# 🥷 Shadow Clone Jutsu (Real-Time Computer Vision Cloning System)

A standalone Python Computer Vision application that creates Naruto-style shadow clone effects in real time using a webcam.

This project demonstrates foreground extraction, frame compositing, and multi-instance rendering using classical Computer Vision techniques. It is useful for students, researchers, and developers exploring real-time video processing, human segmentation, and interactive visual effects.

---

## Features

* **Real-Time Webcam Processing:** Captures and processes live video feed with minimal latency
* **Foreground Extraction:** Separates the subject from the background
* **Clone Generation:** Creates multiple visual copies of the user within the scene
* **Live Rendering:** Displays clones simultaneously in real time
* **Lightweight Implementation:** Runs on CPU without requiring GPU acceleration
* **Interactive Demo:** Simple controls for capturing and managing clones

---

## How It Works

1. Captures frames from the webcam
2. Performs background subtraction / segmentation
3. Extracts the foreground (user) as a mask
4. Stores selected frames as clone templates
5. Overlays multiple clones onto the scene
6. Displays the composited output continuously

---

## Requirements

* Python 3.7 or higher
* OpenCV
* NumPy
* Webcam

---

## How to Use

1. Clone the repository

```
git clone https://github.com/anmajharul/Majharul.git
cd Majharul/AI-Computer-Vision-Playground/Shadow_Clone_Jutsu
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
python main.py
```

4. Allow webcam access if prompted

---

## Controls

*(Adjust if your implementation differs)*

* **C** → Capture a clone
* **R** → Reset all clones
* **Q / ESC** → Exit application

---

## Use Case

Originally developed as a Computer Vision demonstration project to explore real-time human segmentation and visual compositing techniques.

Applicable for:

* Computer Vision learning and experimentation
* Real-time video processing demos
* Interactive media applications
* Academic projects and presentations
* Portfolio demonstrations

---

## Limitations

* Works best with a stable background
* Sensitive to lighting variations
* Segmentation accuracy depends on environment
* Not depth-aware (2D compositing only)

---

## Possible Improvements

* Deep learning–based segmentation (MediaPipe / DeepLab)
* Gesture-controlled clone creation
* Pose tracking for animated clones
* Depth estimation for realistic layering
* Augmented Reality integration

---


## 🚦 Transportation & Smart Infrastructure Applications

Although originally developed as a visual demonstration, the underlying multi-instance rendering framework has direct relevance to Transportation Engineering and Intelligent Transportation Systems (ITS).

The cloning mechanism can be interpreted as real-time multi-agent scene generation, where each instance represents an individual pedestrian or vehicle within a shared environment.

**Potential applications include:**

* Pedestrian flow and crowd dynamics visualization
* Congestion analysis in transit facilities (stations, terminals, platforms)
* Traffic density and queue formation demonstration
* Synthetic data generation for transportation-related computer vision models
* Smart city and urban mobility scenario presentation

Such capabilities are relevant to studies involving Level of Service (LOS), human mobility, and infrastructure performance evaluation.

**Research potential:**
With additional modules such as object tracking, depth estimation, or deep learning–based segmentation, the system can evolve into a real-time multi-agent visualization framework for transportation planning, safety analysis, and operational research.

**Limitations:**
Performance depends on stable environmental conditions; current implementation is limited to 2D compositing without depth awareness.

**Future work:**
Integration of advanced segmentation models, pose tracking, depth sensing, and augmented reality techniques to improve realism and analytical utility.




# Author

Majharul Islam  
Civil Engineering Student  
Bangladesh University of Business and Technology (BUBT)

Research Focus:
Transportation Engineering  
Travel Behavior Analysis  
Discrete Choice Modeling

[![Portfolio](https://img.shields.io/badge/Website-anmajharul.bd-blue?style=for-the-badge&logo=googlechrome)](https://anmajharul.bd) 

© Majharul Islam – Research Portfolio
