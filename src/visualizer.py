import os
import matplotlib.pyplot as plt


def create_charts_folder():
    os.makedirs("charts", exist_ok=True)


def save_and_show(filename):
    create_charts_folder()

    plt.savefig(
        f"charts/{filename}",
        bbox_inches="tight"
    )

    plt.show()
    plt.close()


def plot_subject_averages(df):
    subjects = ["Maths", "Science", "English", "Computer"]

    averages = [
        df["Maths"].mean(),
        df["Science"].mean(),
        df["English"].mean(),
        df["Computer"].mean()
    ]

    plt.figure(figsize=(8, 5))
    plt.bar(subjects, averages)

    plt.title("Subject Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")

    save_and_show("subject_averages.png")


def plot_grade_distribution(df):
    grade_counts = df["Grade"].value_counts()

    plt.figure(figsize=(7, 7))

    plt.pie(
        grade_counts,
        labels=grade_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("Grade Distribution")

    save_and_show("grade_distribution.png")


def plot_marks_histogram(df):
    plt.figure(figsize=(8, 5))

    plt.hist(df["Total"], bins=5)

    plt.title("Distribution of Total Marks")
    plt.xlabel("Total Marks")
    plt.ylabel("Number of Students")

    save_and_show("marks_histogram.png")


def plot_top_students(df, n=5):
    top_students = df.nlargest(n, "Total")

    plt.figure(figsize=(8, 5))

    plt.bar(
        top_students["Name"],
        top_students["Total"]
    )

    plt.title(f"Top {n} Students")
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")

    save_and_show("top_students.png")


def plot_student_performance(df):
    students = df["Name"]

    plt.figure(figsize=(10, 5))

    plt.plot(students, df["Maths"], marker="o", label="Maths")
    plt.plot(students, df["Science"], marker="o", label="Science")
    plt.plot(students, df["English"], marker="o", label="English")
    plt.plot(students, df["Computer"], marker="o", label="Computer")

    plt.title("Student Performance by Subject")
    plt.xlabel("Students")
    plt.ylabel("Marks")

    plt.legend()

    save_and_show("student_performance.png")


def plot_pass_fail_stats(df):
    passed = (df["Percentage"] >= 40).sum()
    failed = (df["Percentage"] < 40).sum()

    plt.figure(figsize=(6, 6))

    plt.pie(
        [passed, failed],
        labels=["Pass", "Fail"],
        autopct="%1.1f%%"
    )

    plt.title("Pass vs Fail")

    save_and_show("pass_fail.png")


def plot_subject_toppers(df):
    subjects = ["Maths", "Science", "English", "Computer"]

    highest_marks = [
        df["Maths"].max(),
        df["Science"].max(),
        df["English"].max(),
        df["Computer"].max()
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(subjects, highest_marks)

    plt.title("Highest Marks in Each Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")

    save_and_show("subject_toppers.png")