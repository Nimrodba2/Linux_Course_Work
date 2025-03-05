import pandas as pd

# Load the data
data = pd.read_csv('DOWNLOADS/LINUX_COURSE_WORK-downloads/plants.csv')

# Print first 5 rows to check
print(data.head())

python3 ~/Linux_Course_Work/analyze.py
git add analyze.py
git commit -m "Created analyze.py for analyzing plants data"
git push -u origin main


