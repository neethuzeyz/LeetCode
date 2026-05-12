
import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort the DataFrame by the 'id' column in ascending order
    person.sort_values(by='id', inplace=True)
    
    # Drop duplicate rows based on the 'email' column, keeping the first occurrence
    person.drop_duplicates(subset=['email'], inplace=True)