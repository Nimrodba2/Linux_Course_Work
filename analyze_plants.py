import pandas as pd

data  = pd.read_csv('DOWNLOADS/LINUX_COURSE_WORK-downloads/plants.csv')


data['Height'] = pd.to_numeric(data['Height'], errors='coerce')


data['Average Height'] = data[['Height']].mean(axis=1)
print(data)


data.to_csv('DOWNLOADS/LINUX_COURSE_WORK-downloads/plant_analysis.csv', index=False)
