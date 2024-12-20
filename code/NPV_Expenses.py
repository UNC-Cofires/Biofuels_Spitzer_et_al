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

#Set the working directory
script_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(os.path.dirname(script_path))
os.chdir(parent_directory)
print("Current working directory set to:", os.getcwd())

# Load the matlab results file
file_path = "data\ResultsData-3_2024.12.06.mat"
mat_contents = scipy.io.loadmat(file_path)

#%%

# Data for the first plot (NPV of all Expense)
categories1 = ['Nanno \n (Baseline)', 'SLA-CO2', 'SLA-NaHCO3', 'SLA-Trona']
#values1 = [692.25, 336, 296, 290]
values1 =  [mat_contents['pvexpenseN'].mean()/mat_contents['fuelProdN'].sum(axis=1).mean(),
            mat_contents['pvexpense0'].mean()/mat_contents['fuelProd0'].sum(axis=1).mean(),
            mat_contents['pvexpense1'].mean()/mat_contents['fuelProd1'].sum(axis=1).mean(),
            mat_contents['pvexpense2'].mean()/mat_contents['fuelProd2'].sum(axis=1).mean()]  

# Data for the second plot (NPV of OPEX)
categories2 = categories1  # Same categories
#values2 = [65.5, 80.9, 26.69, 26.59]  
values2 = [mat_contents['pvopexN'].mean()/mat_contents['fuelProdN'].sum(axis=1).mean(), 
           mat_contents['pvopex0'].mean()/mat_contents['fuelProd0'].sum(axis=1).mean(),
           mat_contents['pvopex1'].mean()/mat_contents['fuelProd1'].sum(axis=1).mean(), 
           mat_contents['pvopex2'].mean()/mat_contents['fuelProd2'].sum(axis=1).mean()]  



# Create the plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# First plot (NPV of all Expense)
bars1 = ax1.bar(categories1, values1, color=['#1f77b4', '#ff7f0e', '#ffbb33', '#8e44ad'],
                edgecolor='black', linewidth=1)
ax1.set_ylabel('NPV - All Expenses \n ($ / Gallon)', fontsize=24)
ax1.set_xlabel('Pathways', fontsize=24)
ax1.set_ylim(0, 8)
ax1.tick_params(axis='both', which='major', labelsize=20)
ax1.text(0.02, 0.98, 'A', transform=ax1.transAxes, fontsize=24, fontweight='bold', va='top')

# Second plot (NPV of OPEX)
bars2 = ax2.bar(categories2, values2, color=['#1f77b4', '#ff7f0e', '#ffbb33', '#8e44ad'],
                edgecolor='black', linewidth=1)
ax2.set_ylabel('NPV - Operating Expenses \n ($ / Gallon)', fontsize=24)
ax2.set_xlabel('Pathways', fontsize=24)
ax2.set_ylim(0, 1)
ax2.tick_params(axis='both', which='major', labelsize=20)
ax2.text(0.02, 0.98, 'B', transform=ax2.transAxes, fontsize=24, fontweight='bold', va='top')

# Adjust layout and display the plot
plt.tight_layout()
plt.savefig('figures/NPV_Expenses.png', dpi=400)
plt.show()
