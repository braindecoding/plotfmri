# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:24:35 2024

@author: rolly
"""
import nibabel as nib
from nilearn import plotting
import matplotlib.pyplot as plt
import os

def plotAll(folder_path,target_extension,target_path,new_extension):
    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(target_extension)]
    
    # Load fMRI data in Analyze format
    
    for file_name in file_list:
        img = nib.load(folder_path+file_name)
        # Plot the functional MRI data
        plotting.plot_roi(img,title=file_name)
        new_filename = os.path.splitext(file_name)[0] + new_extension
        plt.savefig(target_path+new_filename)
        plotting.show()
        
def plotAllMask(folder_path,target_extension,target_path,new_extension):
    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(target_extension)]
    
    # Load fMRI data in Analyze format
    
    for file_name in file_list:
        img = nib.load(folder_path+file_name)
        # Plot the functional MRI data
        plotting.plot_roi(img,title=file_name)
        new_filename = os.path.splitext(file_name)[0] + new_extension
        plt.savefig(target_path+new_filename)
        plotting.show()