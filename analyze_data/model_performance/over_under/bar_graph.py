import matplotlib.pyplot as plt
import numpy as np

labels = ['MAE', 'RMSE', '$R^2$ (%)']
all_games = [10.3112, 13.0427, 9.296]
close_games = [10.4589, 13.1658, 9.552]
competitive_games = [8.7902, 11.2083, 17.752]

# 2. Set up the bar positions
x = np.arange(len(labels))  # label locations
width = 0.25  # width of the bars

# 3. Create the bars
plt.bar(x - width, all_games, width, label='All Games', color='#95a5a6')
plt.bar(x, close_games, width, label='Close Games (Spread <= 8)', color='#3498db')
plt.bar(x + width, competitive_games, width, label='Competitive Games (8-16)', color='#2ecc71')

# 4. Add formatting and labels
plt.ylabel('Points / Percentage')
plt.title('Over Under Predicted Accuracy Metrics: Comparison by Predicted Game Type')
plt.xticks(x, labels)
plt.ylim(5, 20)  # Focus the Y-axis on the relevant data range
plt.legend(loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.6)

# 5. Finalize the layout and save
plt.tight_layout()
plt.show()
#plt.savefig('regression_metrics_chart.png')