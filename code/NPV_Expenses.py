# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:46:32 2024

@author: amonkar
"""

# Set the working directory
import os
import scipy.io
from scipy.io import loadmat, matlab
import warnings
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

#Set the working directory
script_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(os.path.dirname(script_path))
os.chdir(parent_directory)
print("Current working directory set to:", os.getcwd())

# Load the matlab results file
file_path = "data\ResultsData-3_2024.12.06.mat"
mat_contents = scipy.io.loadmat(file_path)



#%%
# Categories/pathways
categories = ['Nanno\n(Baseline)', 'SLA-CO2', 'SLA-NaHCO3', 'SLA-Trona']

# Calculate the values for all expenses (total)
total_expenses = [
    mat_contents['pvexpenseN'].mean()/mat_contents['fuelProdN'].sum(axis=1).mean(),
    mat_contents['pvexpense0'].mean()/mat_contents['fuelProd0'].sum(axis=1).mean(),
    mat_contents['pvexpense1'].mean()/mat_contents['fuelProd1'].sum(axis=1).mean(),
    mat_contents['pvexpense2'].mean()/mat_contents['fuelProd2'].sum(axis=1).mean()
]

# Calculate values for operating expenses
operating_expenses = [
    mat_contents['pvopexN'].mean()/mat_contents['fuelProdN'].sum(axis=1).mean(),
    mat_contents['pvopex0'].mean()/mat_contents['fuelProd0'].sum(axis=1).mean(),
    mat_contents['pvopex1'].mean()/mat_contents['fuelProd1'].sum(axis=1).mean(),
    mat_contents['pvopex2'].mean()/mat_contents['fuelProd2'].sum(axis=1).mean()
]

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Bar positions
x = np.arange(len(categories))
width = 0.35  # narrower width to allow for side-by-side bars

# Colors matching your original plot
colors = ['#1f77b4', '#ff7f0e', '#ffbb33', '#8e44ad']

# Create the bars for total expenses (shifted slightly left)
bars_total = ax.bar(x - width/2, total_expenses, width, color=colors, 
                    edgecolor='black', linewidth=1, label='Total Expenses')

# Create the bars for operating expenses (shifted slightly right)
bars_opex = ax.bar(x + width/2, operating_expenses, width, color=colors, 
                   edgecolor='black', linewidth=1, hatch='///', 
                   label='Operating Expenses')

# Add labels and title
ax.set_ylabel('NPV - Expenses\n($ / Gallon)', fontsize=24)
ax.set_xlabel('Scenarios', fontsize=24)
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.tick_params(axis='both', which='major', labelsize=20)

# Set y-axis limit to match the original first plot
ax.set_ylim(0, 8)

# Add a legend
# Create custom legend elements with white background instead of colored backgrounds
legend_elements = [
    Patch(facecolor='white', edgecolor='black', label='Total Expenses'),
    Patch(facecolor='white', hatch='///', edgecolor='black', label='Operating Expenses')
]
ax.legend(handles=legend_elements, fontsize=16)

# Adjust layout
plt.tight_layout()

# Save and show
plt.savefig('figures/NPV_Expenses.png', dpi=400)
plt.show()
