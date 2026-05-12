import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
   
    # Group the activity data by 'player_id' and find the minimum 'event_date' for each player
    first_login_df = activity.groupby('player_id')['event_date'].agg(min).reset_index()

    # Rename the resulting column to 'first_login'
    first_login_df = first_login_df.rename(columns={'event_date': 'first_login'})

    return first_login_df