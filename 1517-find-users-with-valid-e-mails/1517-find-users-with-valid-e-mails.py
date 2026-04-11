import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[
        users['mail'].str.fullmatch(r'^[A-Za-z][\w\.\-]*@leetcode\.com')
    ]