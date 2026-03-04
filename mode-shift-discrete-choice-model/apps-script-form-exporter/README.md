# Google Form to Google Doc Exporter (Apps Script)

A standalone Google Apps Script that automatically extracts questions and options from a Google Form and formats them into a clean, printable, and professional Google Doc.

This script is highly useful for researchers, civil engineers, and data analysts who need to convert digital survey instruments (like Discrete Choice Model surveys) into hard-copy formats for field distribution.

## Features
* **Automated Formatting:** Converts form titles, descriptions, and questions into a structured document.
* **Smart Typographics:** Uses distinct symbols for Multiple Choice (`○`) and Checkbox (`☐`) questions.
* **Section Handling:** Automatically detects page breaks and converts them into clean section dividers.
* **Standalone Execution:** Runs independently from `script.google.com` by targeting the Form ID.

## How to Use

1. Go to [Google Apps Script](https://script.google.com/) and click **New Project**.
2. Copy the code from `Appscipt_Code.gs` and paste it into the script editor.
3. Open your target Google Form and copy its ID from the URL. 
   *(Example: In `https://docs.google.com/forms/d/1aB2c3D4e5F6g7H8/edit`, the ID is `1aB2c3D4e5F6g7H8`)*
4. Replace `'YOUR_FORM_ID_HERE'` in the script with your copied ID.
5. Click **Run**.
6. Grant the necessary permissions when prompted.
7. Check the **Execution Log** for the direct URL to your newly created Google Doc.

## Use Case
Originally developed for exporting thesis survey questionnaires regarding **Mode Shift Behavior**. It ensures proper indentation and readable scales, eliminating the need for manual copy-pasting.

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
