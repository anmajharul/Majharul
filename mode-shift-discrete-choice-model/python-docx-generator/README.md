# Python DOCX Survey Generator

This project automatically converts a plain text survey into a formatted **Microsoft Word (.docx) survey form** using Python.

The script reads raw survey text and automatically formats:

- Questions (Q1, Q2, etc.)
- Checkbox options
- Likert scale rating (1–5)
- Section dividers
- Blank answer fields

The final output is a **clean Word survey form ready for printing or distribution**.

---

# Project Purpose

This tool was developed for the Civil Engineering thesis:

**Mode Shift Behavior Using Discrete Choice Models: A Case Study of BUBT Students in Dhaka**

The goal is to generate structured survey forms automatically without manually formatting them in Microsoft Word.

---

# Requirements

Before running the script, make sure you have:

- Python installed
- Visual Studio Code (VS Code)

Required Python library:

pip install python-docx

---

# Installation and Usage Guide

Follow these steps.

---

## Step 1: Create a Project Folder

Create a new folder on your computer Desktop.

Example:

Thesis_Survey

---

## Step 2: Open the Folder in VS Code

Open **Visual Studio Code**

Go to:

File → Open Folder

Then select the **Thesis_Survey** folder.

---

## Step 3: Create a Python File

Inside VS Code create a new file named:

create_survey.py

Make sure the file extension is **.py**.

---

## Step 4: Paste the Python Code

Copy the Python script and paste it inside:

create_survey.py

Save the file using:

Ctrl + S

---

## Step 5: Insert Your Survey Text

At the bottom of the Python code you will see:

raw_survey_text = """

Paste your full survey text inside the triple quotes.

Example:

raw_survey_text = """
Survey Title

Q1. Question text  
☐ Option 1  
☐ Option 2  

Q2. Another question  
☐ Yes  
☐ No  
"""

Important:

- Do not remove the triple quotes `"""`
- Your entire survey must stay inside them

---

## Step 6: Install Required Library

Open the terminal in VS Code:

Terminal → New Terminal

Run the following command:

pip install python-docx

---

## Step 7: Run the Script

In the terminal run:

python create_survey.py

If it does not work, try:

python3 create_survey.py

---

# Output

If everything works correctly you will see:

Success! Ultimate survey form saved as: BUBT_Survey_Final_Perfect.docx

A formatted **Word survey form (.docx)** will be generated inside your project folder.

---

# Example Project Structure

python-docx-generator

create_survey.py  
README.md  

---

# Author

Majharul Islam  
Civil Engineering Student  
Bangladesh University of Business and Technology (BUBT)

Research Focus:
Transportation Engineering  
Travel Behavior Analysis  
Discrete Choice Modeling
