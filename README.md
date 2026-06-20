# 🎓 Student Performance Analyzer

A console-based Python application for analyzing student performance using **Numpy**, **Pandas** and **Matplotlib**.

The project reads student data from a CSV file, calculates performance metrics, generates reports, and creates visualizations.

---

## 🚀 Features

### 📊 Data Analysis

* Calculate total marks
* Calculate percentage
* Calculate average marks
* Assign grades
* Rank students
* Identify toppers and lowest performers

### 📈 Visualizations

* Subject Average Marks
* Grade Distribution
* Marks Histogram
* Top Students Chart
* Student Performance Comparison
* Pass/Fail Statistics
* Subject Toppers Chart

### 📄 Reports

* Generate summary report
* Export processed student data to CSV
* Save generated charts automatically

### 🖥️ Console Menu

Interactive menu-driven application for easy navigation.

---

## 📁 Project Structure

```text
Student_performance_analyser/
│
├── charts/
│   └── grade_distribution.png
│
├── data/
│   └── student.csv
│
├── reports/
│   └── student_report.csv
│
├── src/
│   ├── analyzer.py
│   ├── data_loader.py
│   ├── main.py
│   ├── report.py
│   └── visualizer.py
│
├── index.py
├── requirements.txt
└── README.md
```

---

## 📋 Sample Dataset

```csv
RollNo,Name,Maths,Science,English,Computer
101,Aman,88,91,84,95
102,Riya,76,85,89,90
103,Rahul,45,55,62,40
104,Priya,92,95,96,98
105,Karan,60,65,70,72
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Student_performance_analyser
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install pandas matplotlib
```

---

## ▶️ Running the Project

Svae your csv to the data folder  to analise  
Run the application from the project root:

```bash
python index.py
```

---

## 📊 Console Menu

```text
==================================================
STUDENT PERFORMANCE ANALYZER
==================================================
1. View Summary Report
2. Save Report
3. Plot Subject Averages
4. Plot Grade Distribution
5. Plot Marks Histogram
6. Plot Top Students
7. Plot Student Performance
8. Plot Pass/Fail Statistics
9. Plot Subject Toppers
10. Show Dataset
0. Exit
==================================================
```

---

## 📈 Generated Charts

The application automatically saves charts inside the `charts/` folder.

* Subject Average Marks
* Grade Distribution
* Marks Histogram
* Top Students
* Student Performance
* Pass vs Fail
* Subject Toppers

---

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* CSV Data Processing

---

## 🎯 Learning Outcomes

This project demonstrates:

* Data Cleaning
* Data Analysis
* Data Visualization
* File Handling
* Modular Python Programming
* Pandas DataFrame Operations
* Matplotlib Charting
* Console-Based Application Development

---

## 📜 License

This project is open source and available under the MIT License.
