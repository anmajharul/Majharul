# Chidori_YOLO

This project uses YOLOv8 to detect Naruto hand signs (jutsu signs). A trained model runs on a live camera feed to recognize signs and trigger a "Chidori" sound and visual effects.

**Tools and libraries used**
- Python 3.11 (tested)
- Ultralytics YOLOv8 (`yolov8n.pt`)
- OpenCV
- MediaPipe Hands
- NumPy
- Pygame (sound)
- Roboflow dataset (Naruto Signs, CC BY 4.0)

**Dataset**
- Location: `AI-Computer-Vision-Playground/Chidori_YOLO/Naruto_Signs`
- Classes: 12
- Labels: Hitsuji (ram), I (boar), Inu (dog), Mi (snake), Ne (rat), Saru (monkey), Tatsu (dragon), Tora (tiger), Tori (bird), U (hare), Uma (horse), Ushi (ox)
- Roboflow URL: `https://universe.roboflow.com/chayawats-workspace-z7lzz/naruto-lkanh/dataset/1`
- License: CC BY 4.0

**Process / Workflow**
1. Download dataset from Roboflow (`download_data` script)
1. Data augmentation (example: `data/Ox/augment_image` uses flip, brightness, noise)
1. Load a pre-trained YOLOv8n model
1. Train (`data/train_model`) with `data.yaml`, `epochs`, `imgsz`, `batch`
1. Save outputs to `runs/detect/...` (weights, plots, metrics)
1. Live inference (`live_test`) using MediaPipe for hand ROI crop, YOLO for sign classification, sound/VFX trigger

**How to run**
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Training:
```bash
python data/train_model
```

Live test:
```bash
python live_test
```

Notes:
- The script files have no `.py` extension, so run them with `python file_name`.
- The `live_test` script expects the model at `runs/detect/naruto_ultimate_v4/weights/best.pt`. Update the path to match your training run.
- If you use the Roboflow download script, install the extra package:
```bash
pip install roboflow
```

**Project structure (short)**
- `download_data` - download dataset from Roboflow
- `data/train_model` - training script
- `live_test` - live camera inference + sound/VFX
- `requirements.txt` - dependencies
- `runs/detect/...` - training outputs (weights, plots, metrics)

**How to use in Transportation Engineering**
- Detect traffic police/flagger hand signals (retrain with a relevant dataset)
- Monitor intersection gestures to support signal control or incident analysis
- Detect bus/ride-share stop intent or stop-request gestures
- Queue management in stations/terminals by recognizing directional gestures
- Work-zone safety: detect flagger/worker gestures to trigger warnings

**How to customize for transportation domain**
1. Collect videos of transportation-related gestures/signs
1. Label and export in YOLO format
1. Update `data.yaml`
1. Tune training config (epochs, imgsz, batch)
1. Field test and set confidence thresholds

**Limitations**
- Accuracy can drop with changes in lighting, angle, or occlusion
- Real-time performance depends on hardware
- For public-space video processing, follow privacy and ethical guidelines

**Security Note**
- The `download_data` script contains a hard-coded Roboflow API key. Remove or rotate the key before uploading to GitHub.

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

