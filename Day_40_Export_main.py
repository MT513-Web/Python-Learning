
import pandas as pd
from Day_40_Export_Logic import get_job_data, clean_and_filter, save_to_file


# Configuration for clean terminal output
pd.set_option('display.max_columns', None)
pd.set_option ('display.width', 1000)

# 1. Load: Fetching raw data
raw_data = get_job_data()


# 2. Process: Cleaning and filtering for the best candidates
shortlisted_devs = clean_and_filter(raw_data)

print("\n--- Shortlisted Candidates Ready for Export ---\n")
print(shortlisted_devs)


# 3. Export: Saving the 'shortlisted' list into a new file
# We are naming the new file 'Day_40_shortlisted_candidates.csv'
status = save_to_file(shortlisted_devs, 'Day_40_shortlisted_candidates.csv')

print ('\n', status)


"""
--- PROJECT SUMMARY & CONCLUSION ---

This project demonstrates a complete Data Engineering pipeline:
1. DATA INGESTION: Loaded raw applicant data from an external CSV file.
2. DATA CLEANING:  Handled missing values (NaN) for 'Experience' and 'Salary' to ensure math accuracy.
3. DATA FILTERING: Used boolean indexing to shortlist 'Python' developers with high experience.
4. DATA EXPORT (CRUD - Create): Successfully exported the refined list into a new file 
   'shortlisted_candidates.csv' for business use.

Final Result: The system automates the hiring process by reducing manual screening time.

"""
