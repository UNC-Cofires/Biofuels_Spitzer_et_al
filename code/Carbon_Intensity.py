# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:08:04 2024

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

# Data
categories = ['Diesel','Nanno \n (Baseline)', 'SLA-CO2', 'SLA-NaHCO3', 'SLA-Trona']
#values = [94.17, 68.8, 42.1, 40.01, 40.02] #Old values
values = [94.17, 
          mat_contents['EmiN'].mean(), 
          mat_contents['Emi0'].mean(), 
          mat_contents['Emi1'].mean(), 
          mat_contents['Emi2'].mean()] 
# Create the plot
fig, ax = plt.subplots(figsize=(12, 9))
# Create the bar plot
bars = ax.bar(categories, values, color=['#000000','#1f77b4', '#ff7f0e', '#ffbb33', '#8e44ad'],
              edgecolor='black', linewidth=1)
# Customize the plot
ax.set_ylabel('grams CO2eq/MJ', fontsize=20)
ax.set_xlabel('Pathways', fontsize=20)
ax.set_ylim(0, 100)
ax.tick_params(axis='both', which='major', labelsize=18)


# Adjust layout and display the plot
plt.tight_layout()
plt.savefig('figures\Carbon_Intensity.png', dpi=400)
plt.show()