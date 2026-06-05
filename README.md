# 🚗 Smart Parking Assistance System

## 📌 Project Overview

The **Smart Parking Assistance System** is a Python-based simulation that assists drivers in locating and parking their vehicles in an available parking slot. The system provides real-time parking guidance through visual indicators, dashboard statistics, parking status updates, and voice alerts.

The project simulates a modern vehicle rear-camera parking assistance interface commonly found in advanced driver assistance systems (ADAS).

---

# 🎯 Objectives

* Detect and guide the vehicle towards an available parking slot.
* Provide visual parking assistance through dashboard overlays.
* Calculate parking distance and direction.
* Generate voice alerts for parking guidance.
* Simulate parking slot alignment and parking completion.
* Validate parking logic using automated unit tests.

---

# ✨ Features

### 🚘 Parking Guidance

* Rear camera simulation.
* Available parking slot detection.
* Automatic parking guidance.

### 📊 Smart Dashboard

* Distance monitoring.
* Direction guidance.
* Sensor zone indication.
* Parking status updates.
* Parking score calculation.

### 🔊 Voice Assistance

* Move towards slot guidance.
* Turn left alerts.
* Turn right alerts.
* Continue reversing instructions.
* Parking complete announcement.

### 🅿️ Parking Status Monitoring

* SEARCHING
* APPROACHING
* ALIGN SLOT
* PARKED

### ✅ Testing

* Unit testing using PyTest.
* Validation of distance calculation.
* Validation of parking direction logic.
* Validation of parking status determination.

---

# 🛠️ Technologies Used

| Technology   | Purpose          |
| ------------ | ---------------- |
| Python 3     | Core Development |
| Tkinter      | GUI Development  |
| Pillow (PIL) | Image Processing |
| pyttsx3      | Voice Alerts     |
| PyTest       | Unit Testing     |

---

# 📂 Project Structure

```text
SmartParkingAssistanceSystem/
│
├── app.py
├── parking_logic.py
├── camera_scene.png
├── dashboard_overlay.png
├── requirements.txt
│
├── tests/
│   └── test_parking.py
│
├── output/
│   ├── screenshots/
│   ├── demo_video/
│   └── reports/
│
├── venv/
├── __pycache__/
├── .pytest_cache/
│
└── README.md
```

### Important Notes

* `app.py` → Main Smart Parking Assistance System application.
* `parking_logic.py` → Parking distance, direction, and status calculation logic.
* `camera_scene.png` → Rear camera parking scene image.
* `dashboard_overlay.png` → Futuristic dashboard overlay UI.
* `tests/test_parking.py` → Unit tests using PyTest.
* `requirements.txt` → Project dependencies.
* `output/` → Stores screenshots, demo video, and generated reports.
* `venv/`, `__pycache__/`, `.pytest_cache/` → Auto-generated development files and should not be included in the final submission ZIP.

```
```

---

# ⚙️ Installation

## Step 1: Clone or Download the Project

```bash
git clone https://github.com/Anushka-soni/SmartParkingAssistanceSystem
cd SmartParkingAssistanceSystem
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Run the simulator:

```bash
python app.py
```

---

# 🎮 Controls

| Key | Action                          |
| --- | ------------------------------- |
| ←   | Move Left                       |
| →   | Move Right                      |
| ↑   | Move Forward                    |
| ↓   | Reverse / Approach Parking Slot |

---

# 🧪 Running Unit Tests

Execute the test suite:

```bash
pytest tests -v
```

Expected Result:

```text
========================
7 passed
========================
```

---

# 🔍 Parking Logic

### Distance Calculation

The system calculates the distance between the vehicle and parking slot using Euclidean Distance.

### Direction Guidance

Based on vehicle position:

* TURN LEFT
* TURN RIGHT
* STRAIGHT

### Parking Status

| Distance Range | Status      |
| -------------- | ----------- |
| Far            | SEARCHING   |
| Medium         | APPROACHING |
| Near           | ALIGN SLOT  |
| Very Close     | PARKED      |

---

# 📸 Output Screens

The system displays:

* Rear Camera View
* Parking Slot Detection
* Smart Dashboard Overlay
* Voice Alert Status
* Parking Completion Indicator

---

# 📈 Test Coverage

The following functions are tested:

* `calculate_distance()`
* `get_direction()`
* `parking_status()`

---

# 🚀 Future Enhancements

* Real-time camera integration using OpenCV.
* Automatic parking algorithm.
* Android application deployment.
* Appium-based mobile automation testing.
* AI-powered parking slot detection.
* Multi-slot parking management.

---

# 🎓 Academic Purpose

This project was developed as part of a software engineering and automation testing learning project to demonstrate:

* GUI Development
* Python Programming
* Parking Assistance Logic
* Voice Guidance Systems
* Automated Unit Testing

---

# 👨‍💻 Author

**Anushka Soni**

Smart Parking Assistance System – 2026
