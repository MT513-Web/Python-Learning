"""
--------Time-Series Analysis (Working with Dates)-------

What are we doing today?
We are working with "Social Media Engagement Data". We will learn how to convert text dates into 
real Python dates and extract specific information like the "Month" or "Day Name" to see when engagement was highest.

Why are we doing this?
In Data Science, dates are often loaded as simple text. To perform analysis (like "Which month had the most likes?"), 
we must convert them into datetime objects.

"""
from re import L

import pandas as pd

def load_social_data():
    """Load the social media dataset"""
    return pd.read_csv('Day_43_social_media_data.csv')

def process_dates(df):
    """Convert text dates to datetime objects and extract month information."""
    # Logic: pd.to_datetime converts string dates into actual date objects
    df['Post_Date'] = pd.to_datetime(df['Post_Date'])
    
    # Logic: .dt.month_name() extracts the name of the month from the date
    df['Month'] = df['Post_Date'].dt.month_name()

    # Logic: .dt.day_name() extracts the day of the week
    df['Day_of_Week'] = df['Post_Date'].dt.day_name()

    return df

def monthly_likes(df):
    """Calculate total likes per month"""
    # Using groupby to summarize likes by month
    summary = df.groupby('Month').agg({'Likes': 'sum'}).reset_index()
    return summary


"""
--- df['Post_Date'] = pd.to_datetime(df['Post_Date']) ---
Why: When you load a CSV, the date "2026-01-15" is just a string (text). You cannot ask Python "What month is this?" 
if it's just text. This line transforms it into a Datetime Object, which is a smart format that understands calendar logic.

--- df['Month'] = df['Post_Date'].dt.month_name() ---
 .dt (Datetime accessor) .month_name() (Get the name of the month).
Why: The .dt is like a key that opens the "Date Folder." Once open, we pull out the month name (January, February, etc.) 
and save it in a new column called 'Month'.

--- df['Day_of_Week'] = df['Post_Date'].dt.day_name() ---
Why: Similar to the month, this pulls out "Monday," "Tuesday," etc. This is very useful for businesses to see if they get more 
engagement on weekends vs. weekdays.

--- summary = df.groupby('Month').agg({'Likes': 'sum'}).reset_index() ---
Why: We are reusing the Day 42 logic. We take our new 'Month' column, group all "January" rows together, and sum up their likes.

"""

