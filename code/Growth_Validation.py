# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:35:16 2024

Figure 3 - Plot of the growth model validation

@author: amonkar
"""

# Set the working directory
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Set the working directory
script_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(os.path.dirname(script_path))
os.chdir(parent_directory)
print("Current working directory set to:", os.getcwd())



#%%
# Read the CSV file
df = pd.read_csv('data/SLA-04_Experimental and Modelled Concentration of Growth_2024.09.17.csv', header=None)

# Extract the data
modelled = df[0].values
experimental = df[1].values

# Create the scatter plot
plt.figure(figsize=(10, 8))
plt.scatter(modelled, experimental, color='blue', alpha=0.7, edgecolors='none', s = 75)

# Calculate and plot the line of best fit
coeffs = np.polyfit(modelled, experimental, 1)
line = np.poly1d(coeffs)
plt.plot(modelled, line(modelled), color='red', label='Line of best fit')

# Calculate R-squared
correlation_matrix = np.corrcoef(modelled, experimental)
r_squared = correlation_matrix[0, 1]**2

# Set labels and title
plt.xlabel('Modelled Concentration at Harvest', fontsize=20)
plt.ylabel('Experimental Concentration at Harvest', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=18)

# Add legend and R-squared value
plt.legend(fontsize = 20)
plt.text(0.05, 0.9, f'R² = {r_squared:.2f}', transform=plt.gca().transAxes, 
         verticalalignment='top', fontsize = 20)

# Set axis limits
plt.xlim(0.15, 1.7)
plt.ylim(0.15, 1.7)

# Show the plot
plt.tight_layout()
plt.savefig('figures\Growth_Validation.png', dpi=400)
plt.show()