def generate_summary_report(df):
    print("\n===== STUDENT PERFORMANCE REPORT =====")

    print(f"Total Students: {len(df)}")

    print(f"Class Average: {df['Average'].mean():.2f}")

    topper = df.loc[df['Total'].idxmax()]
    print(f"Topper: {topper['Name']} ({topper['Total']} marks)")

    lowest = df.loc[df['Total'].idxmin()]
    print(f"Lowest Performer: {lowest['Name']} ({lowest['Total']} marks)")

    print(f"Highest Maths Score: {df['Maths'].max()}")
    print(f"Highest Science Score: {df['Science'].max()}")
    print(f"Highest English Score: {df['English'].max()}")
    print(f"Highest Computer Score: {df['Computer'].max()}")

    print("\nGrade Distribution:")
    print(df['Grade'].value_counts())



def save_report(df):
    df.to_csv("reports/student_report.csv", index=False)
    print("Report saved successfully!")