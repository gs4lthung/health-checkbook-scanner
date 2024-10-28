import pandas as pd


def update_csv(csv_path, extracted_data):
    df = pd.read_csv(csv_path)
    df = df._append(extracted_data, ignore_index=True)
    updated_csv = csv_path.replace('.csv', '_updated.csv')
    df.to_csv(updated_csv, index=False)

    return updated_csv
