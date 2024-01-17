import nibabel as nib
from nilearn import plotting
import matplotlib.pyplot as plt
import os

# Config
target_path="img/"
folder_path="data/"
target_extension = '.img'
new_extension = '.png'
file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(target_extension)]

# Load fMRI data in Analyze format

for file_name in file_list:
    img = nib.load(folder_path+file_name)
    # Plot the functional MRI data
    plotting.plot_epi(img)
    new_filename = os.path.splitext(file_name)[0] + new_extension
    plt.savefig(target_path+new_filename)
    plotting.show()


