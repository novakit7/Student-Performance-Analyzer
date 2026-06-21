# 🎓 Student Performance Analyzer

A professional Python-based data analysis project that evaluates student academic performance using **Pandas**, **NumPy**, and **Matplotlib**.

The application reads student records from a CSV file, performs statistical analysis, generates performance reports, and visualizes insights through charts and graphs.

---

## ✨ Key Features

### 📊 Performance Analysis

* Calculate total marks for each student
* Calculate percentage scores
* Compute subject-wise averages
* Assign grades automatically
* Rank students based on performance
* Identify toppers and low performers
* Generate pass/fail statistics

### 📈 Data Visualization

The application automatically generates and saves charts including:

* Subject Average Marks
* Grade Distribution
* Marks Distribution Histogram
* Top Students Leaderboard
* Student Performance Comparison
* Pass vs Fail Analysis
* Subject-wise Toppers

### 📄 Report Generation

* Generate detailed performance summaries
* Export processed data to CSV
* Save visual reports as images
* View reports directly from the console

### 🖥️ Interactive Console Interface

Simple menu-driven navigation for analysis and visualization.

---

# 📁 Project Structure

```text
Student_Performance_Analyzer/
│
├── charts/
│   ├── grade_distribution.png
│   ├── subject_average.png
│   └── ...
│
├── data/
│   └── students.csv
│
├── reports/
│   └── student_report.csv
│
├── src/
│   ├── analyzer.py
│   ├── data_loader.py
│   ├── report.py
│   ├── visualizer.py
│   └── main.py
│
├── index.py
├── requirements.txt
└── README.md
```

---

# 📋 Sample Dataset

```csv
RollNo,Name,Maths,Science,English,Computer
101,Aman,88,91,84,95
102,Riya,76,85,89,90
103,Rahul,45,55,62,40
104,Priya,92,95,96,98
105,Karan,60,65,70,72
```

---

# 🛠️ Technologies Used

| Technology | Purpose               |
| ---------- | --------------------- |
| Python     | Core Programming      |
| Pandas     | Data Analysis         |
| NumPy      | Numerical Computation |
| Matplotlib | Data Visualization    |
| CSV        | Data Storage          |

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/novakit7/Student-Performance-Analyzer.git
cd Student_Performance_Analyzer
```

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

## 3. Activate the Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy matplotlib
```

---

# ▶️ Running the Application

1. Place your dataset inside the `data/` folder.
2. Ensure the CSV follows the required format.
3. Run:

```bash
python index.py
```

---

# 📋 Console Menu

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
7. Plot Student Performance Comparison
8. Plot Pass/Fail Statistics
9. Plot Subject Toppers
10. View Dataset
0. Exit
==================================================
```

---

# 📈 Output

### Generated Reports

* Student Rankings
* Grade Analysis
* Percentage Calculations
* Subject-wise Statistics

### Generated Charts

All charts are automatically saved inside the `charts/` directory.

```text
charts/
├── grade_distribution.png
├── marks_histogram.png
├── pass_fail.png
├── subject_average.png
└── ...
```

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Data Cleaning and Preprocessing
* Data Analysis using Pandas
* Statistical Calculations using NumPy
* Data Visualization using Matplotlib
* CSV File Handling
* Modular Python Development
* Report Generation
* Real-World Data Analysis Workflow

---

# 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed as a learning project to practice Python, Data Analysis, and Data Visualization concepts.
