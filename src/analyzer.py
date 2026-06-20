def calculate_percentage(df):
    df["Total"] = (
        df["Maths"] +
        df["Science"] +
        df["English"] +
        df["Computer"]
    )

    df["Percentage"] = (df["Total"] / 400) * 100

    return df


def calculate_grade(df):
    def grade(percentage):
        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "F"

    df["Grade"] = df["Percentage"].apply(grade)

    return df


def calculate_student_average(df):
    df["Average"] = (
        df["Maths"] +
        df["Science"] +
        df["English"] +
        df["Computer"]
    ) / 4

    return df


def get_topper(df):
    return df.loc[df["Percentage"].idxmax()]


def get_lowest_performer(df):
    return df.loc[df["Percentage"].idxmin()]


def calculate_subject_averages(df):
    return {
        "Maths": df["Maths"].mean(),
        "Science": df["Science"].mean(),
        "English": df["English"].mean(),
        "Computer": df["Computer"].mean()
    }


def calculate_pass_fail_stats(df):
    passed = (df["Percentage"] >= 40).sum()
    failed = (df["Percentage"] < 40).sum()

    return {
        "Passed": passed,
        "Failed": failed
    }


def rank_students(df):
    df["Rank"] = df["Percentage"].rank(
        ascending=False,
        method="dense"
    )

    return df