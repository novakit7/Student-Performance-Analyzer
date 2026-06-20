from data_loader import load_data
from report import generate_summary_report, save_report
from analyzer import (
    calculate_percentage,
    calculate_grade,
    calculate_student_average,
    rank_students
)
from visualizer import (
    plot_grade_distribution,
    plot_marks_histogram,
    plot_pass_fail_stats,
    plot_student_performance,
    plot_subject_averages,
    plot_subject_toppers,
    plot_top_students
)


def prepare_data():
    data = load_data()

    data = calculate_percentage(data)
    data = calculate_student_average(data)
    data = calculate_grade(data)
    data = rank_students(data)

    return data


def display_menu():
    print("\n" + "=" * 50)
    print("STUDENT PERFORMANCE ANALYZER")
    print("=" * 50)
    print("1. View Summary Report")
    print("2. Save Report")
    print("3. Plot Subject Averages")
    print("4. Plot Grade Distribution")
    print("5. Plot Marks Histogram")
    print("6. Plot Top Students")
    print("7. Plot Student Performance")
    print("8. Plot Pass/Fail Statistics")
    print("9. Plot Subject Toppers")
    print("10. Show Dataset")
    print("0. Exit")
    print("=" * 50)


def main():
    data = prepare_data()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_summary_report(data)

        elif choice == "2":
            save_report(data)

        elif choice == "3":
            plot_subject_averages(data)

        elif choice == "4":
            plot_grade_distribution(data)

        elif choice == "5":
            plot_marks_histogram(data)

        elif choice == "6":
            plot_top_students(data)

        elif choice == "7":
            plot_student_performance(data)

        elif choice == "8":
            plot_pass_fail_stats(data)

        elif choice == "9":
            plot_subject_toppers(data)

        elif choice == "10":
            print(data)

        elif choice == "0":
            print("Thank you for using Student Performance Analyzer!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()