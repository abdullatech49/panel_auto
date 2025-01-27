import os
from datetime import datetime, timedelta
from random import randint

# Set the number of days to backdate
days_to_backdate = 61

# Get today's date
today = datetime.now()

for day in range(days_to_backdate):
    # Calculate the date for each of the last 61 days
    commit_date = today - timedelta(days=day)
    
    # Generate a random number of commits for that day (1-3)
    num_commits = randint(1, 3)
    
    for _ in range(num_commits):
        # Create a unique message or modify the file content if needed
        with open('file.txt', 'a') as file:
            file.write(f"Commit on {commit_date.strftime('%Y-%m-%d')}\n")
        
        # Format the commit date
        formatted_date = commit_date.strftime('%Y-%m-%d %H:%M:%S')
        
        # Execute the git commands
        os.system('git add .')
        os.system(f'git commit --date="{formatted_date}" -m "Backdated commit"')

# Push changes to the repository
os.system('git push -u origin main')
