# Mode Shift Behavior Using Discrete Choice Models

This repository contains the code, tools, and supporting materials used in the Civil Engineering thesis research:

**"Mode Shift Behavior Using Discrete Choice Models: A Case Study of BUBT Students in Dhaka"**

The project analyzes travel behavior of university students and examines how factors such as **travel time, cost, comfort, reliability, and safety** influence transportation mode choice.

The repository also includes tools for **survey generation, data collection preparation, and analysis workflows**.

---

# Research Objective

The objective of this research is to understand how students choose between different transport modes such as:

* MRT (Metro Rail)
* Public Bus
* Ridesharing (Uber / Pathao)
* Private Car
* Motorcycle
* Rickshaw

The study focuses on identifying the **key factors that influence mode switching behavior** using discrete choice modeling approaches.

---

# Repository Structure

```
mode-shift-discrete-choice-model
│
├── README.md
│
├── apps-script-form-exporter
│   └── README.md
│
├── Appscipt_Code
│   └── README.md
│
└── python-docx-generator
    └── README.md
```

---

# Project Components

## 1. python-docx-generator

This module contains a Python script that automatically generates a formatted **Word (.docx) survey questionnaire** from raw text.

Features:

* Automatic question formatting
* Checkbox options
* Likert scale ratings
* Clean academic survey layout

The tool helps researchers quickly create survey forms without manual formatting.

---

## 2. apps-script-form-exporter

This component contains scripts related to **Google Apps Script automation** for exporting or managing form responses.

It helps in organizing survey responses collected through online forms.

---

## 3. Appscipt_Code

This folder contains supporting scripts used for handling survey workflow and form integration.

---

# Survey Design

The survey used in this research collects information on:

* Socioeconomic characteristics
* Travel origin and destination
* Mode choice
* Travel time and cost
* Comfort level
* Reliability perception
* Safety perception
* Mode switching behavior

The questionnaire is designed to support **discrete choice modeling analysis**.

---

# Tools and Technologies

The following tools are used in this project:

* Python
* python-docx
* Google Apps Script
* Microsoft Word
* Visual Studio Code

---

# How to Use the Survey Generator

1. Create a project folder
2. Open it in **Visual Studio Code**
3. Create a Python file named `create_survey.py`
4. Paste the survey generator script
5. Install the required library:

```
pip install python-docx
```

6. Run the script:

```
python create_survey.py
```

The script will generate a formatted **Word survey form** automatically.

---

# Research Field

Transportation Engineering
Travel Behavior Analysis
Discrete Choice Modeling

---

# Author

**Majharul Islam**
Civil Engineering Student
Bangladesh University of Business and Technology (BUBT)

---

# License

This repository is intended for **academic and research purposes**.
