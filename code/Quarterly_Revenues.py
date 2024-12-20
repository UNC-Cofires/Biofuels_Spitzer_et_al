# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:17:14 2024

@author: amonkar

Figure to create quarterly revenues across different pathways.
"""

# Set the working directory
import os
import scipy.io
from scipy.io import loadmat, matlab
import warnings
import matplotlib.pyplot as plt
import numpy as np

#Set the working directory
script_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(os.path.dirname(script_path))
os.chdir(parent_directory)
print("Current working directory set to:", os.getcwd())

# Load the matlab results file
file_path = "data\ResultsData-3_2024.12.06.mat"
mat_contents = scipy.io.loadmat(file_path)

#%%

# Load the datasets
datasets = {
    'Nanno (Baseline)': mat_contents['net_cashflowN']/10**6,
    'SLA-CO2': mat_contents['net_cashflow0']/10**6,
    'SLA-NaHCO3': mat_contents['net_cashflow1']/10**6,
    'SLA-Trona': mat_contents['net_cashflow2']/10**6,
    'SLA-Trona-LCFS': mat_contents['net_cashflow3']/10**6
}

plt.figure(figsize=(16, 8))
colors = ['#1f77b4', '#ff7f0e', '#ffbb33', '#8e44ad', '#A1B665']

for (name, data), color in zip(datasets.items(), colors):
    # Flatten the numpy array directly
    values = data.flatten()
    values = values[~np.isnan(values)]
    
    plt.hist(values, bins=100, alpha=0.7, label=name, color=color, edgecolor='black')
    mean_value = np.mean(values)
    plt.axvline(mean_value, color=color, linestyle='dashed', linewidth=3)

plt.xlabel('$ Millions', fontsize=24)
plt.ylabel('Number of Quarters', fontsize=24)
plt.legend(fontsize=22)
plt.grid(True, alpha=0.3)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.tight_layout()
plt.savefig('figures\Quarterly_Revenues.png', dpi=400)
plt.show()