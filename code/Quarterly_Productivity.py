# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:59:50 2024

@author: amonkar

Code to plot the quarterly productivity for both strains. 

"""

# Set the working directory
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Set the working directory
script_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(os.path.dirname(script_path))
os.chdir(parent_directory)
print("Current working directory set to:", os.getcwd())

#%%

def load_and_process_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path, header=None)
    
    # Create a list of column names that repeat Q1, Q2, Q3, Q4
    num_columns = len(df.columns)
    column_names = ['Q1', 'Q2', 'Q3', 'Q4'] * (num_columns // 4)
    
    # Assign these column names to the dataframe
    df.columns = column_names[:num_columns]
    
    # Melt the dataframe to long format
    df_melted = df.melt(var_name='Quarter', value_name='Productivity')
    
    return df_melted


df_nano = load_and_process_data('data/quarterlyprod_Nano18March.csv')



def plot_quarterly_productivity(nano_file, sla04_file):
    df_nano = load_and_process_data(nano_file)
    df_sla04 = load_and_process_data(sla04_file)

    fig, axes = plt.subplots(2, 2, figsize=(25, 15))
    axes = axes.flatten()

    for i, quarter in enumerate(['Q1', 'Q2', 'Q3', 'Q4']):
        ax = axes[i]
        sns.histplot(data=df_nano[df_nano['Quarter'] == quarter], x='Productivity', 
                     color='#ff7f0e', kde=False, ax=ax, stat='count', label='N. Oceanica',
                     binwidth=5, alpha=0.9)
        sns.histplot(data=df_sla04[df_sla04['Quarter'] == quarter], x='Productivity', 
                     color='#1f77b4', kde=False, ax=ax, stat='count', label='SLA-04',
                     binwidth=5, alpha=0.9)
        
        
        # Add quarter label to upper left corner
        ax.text(0.05, 0.95, quarter, transform=ax.transAxes, 
                fontsize=28, fontweight='bold', va='top', ha='left')
        
        
        # Set x-axis label only for bottom subplots
        if i >= 2:
            ax.set_xlabel('Productivity (g m⁻² qtr⁻¹)', fontsize=28)
        else:
            ax.set_xlabel('')
        
        # Set y-axis label only for left subplots
        if i % 2 == 0:
            ax.set_ylabel('Frequency', fontsize=28)
        else:
            ax.set_ylabel('')
            
        ax.set_xlim(150, 1500)
        ax.set_ylim(0, 1750)
        
        
        # Increase size of x and y axis ticks and numbers
        ax.tick_params(axis='both', which='major', labelsize=20)
        ax.tick_params(axis='both', which='minor', labelsize=20)
        
        # Remove legend if it exists
        legend = ax.get_legend()
        if legend:
            legend.remove()

    # Add legend to upper right corner of lower right panel
    handles, labels = axes[-1].get_legend_handles_labels()
    axes[-1].legend(handles, labels, loc='upper right', fontsize=28)
    
    plt.tight_layout()
    plt.savefig('figures/Productivity.png', dpi=300)
    plt.show()


# Usage:
plot_quarterly_productivity('data/quarterlyprod_Nano18March.csv', 'data/quarterlyprod_SLA04_318.csv')



