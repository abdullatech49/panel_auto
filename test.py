import os
from datetime import datetime, timedelta

# Define the number of days for commits
total_days = 61

# Current date (adjusted to your query date)
current_date = datetime(2025, 1, 27, 19, 0)

# Loop through each of the past 61 days
for day_offset in range(total_days):
    # Calculate the date for the commit
    commit_date = current_date - timedelta(days=day_offset)
    formatted_date = commit_date.strftime('%Y-%m-%d %H:%M:%S')
    
    # Create a commit for this day
    with open('file.txt', 'a') as file:
        file.write(f"Commit for {formatted_date}\n")
    
    # Stage the file and commit with the specific date
    os.system('git add .')
    os.system(f'git commit --date="{formatted_date}" -m "Commit on {formatted_date}"')

# Push all commits to the main branch
os.system('git push -u origin main')
