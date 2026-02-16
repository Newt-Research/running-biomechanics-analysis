import pandas as pd
import matplotlib.pyplot as plt

# 1. Create Mock Data (Simulating movement profiles)
data = {
    'Runner_ID': [1, 2, 3, 4, 5, 6],
    'Category': ['New', 'Experienced', 'New', 'Experienced', 'New', 'Experienced'],
    'Cadence_BPM': [162, 178, 158, 182, 165, 175]
}

df = pd.DataFrame(data)

# 2. Data Processing (Grouping data for analysis)
averages = df.groupby('Category')['Cadence_BPM'].mean()

# 3. Visualization (Making data accessible for reports)
plt.figure(figsize=(8, 5))
averages.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Average Running Cadence: New vs. Experienced Runners')
plt.ylabel('Cadence (BPM)')
plt.savefig('cadence_chart.png')

print("Analysis complete. Results summarized and chart saved.")
