import pandas as pd

def load_data():
    data = pd.read_csv("data/student.csv")
    print(data)

def load_data():
    try:
        data = pd.read_csv("data/student.csv")
        if data.empty:
            print("Dataset is empty")
            return None

        data = data.drop_duplicates()

        return data

    except FileNotFoundError:
        print("CSV file not found")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def dataset_info(df):
    print(df.info())
    print(df.describe())