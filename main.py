import matplotlib.pyplot as plt
import nibabel as nib
from nilearn import plotting
import numpy as np
from helper.plot import plotAllMask


# In[]: Config roi data
target_path="roim/"
folder_path="roi/"
target_extension = '.img'
new_extension = '.png'
sbjId = 's1'
#plot all
plotAllMask(folder_path,target_extension,target_path,new_extension)


# In[]: Config fmri data
target_path="img/"
folder_path="data/"
target_extension = '.img'
new_extension = '.png'
sbjId = 's1'
#plot all
#plotAll(folder_path,target_extension,target_path,new_extension)

# In[]: Load fMRI data in Analyze format
fmri_image  = nib.load(folder_path+'ras1_c0005'+target_extension)
fmri_data = fmri_image.get_fdata()

# In[]: atlas mask https://nilearn.github.io/dev/auto_examples/01_plotting/plot_atlas.html
from nilearn import datasets

dataset_ho = datasets.fetch_atlas_harvard_oxford("cort-maxprob-thr25-2mm")
atlas_ho_filename = dataset_ho.filename
print(f"Atlas ROIs are located at: {atlas_ho_filename}")
# In[]: 
plotting.plot_roi(atlas_ho_filename, title="Harvard Oxford atlas")
plotting.plot_roi(
    atlas_ho_filename,
    view_type="contours",
    title="Harvard Oxford atlas in contours",
)
plotting.show()

# In[]: Plot all brain
plotting.plot_roi(fmri_image)
#plotting.plot_stat_map(fmri_image)
plotting.show()

# In[]:Plot on glass brain with visual cortex activation
plotting.plot_glass_brain(fmri_image, threshold=3.0, colorbar=True, plot_abs=False, display_mode='lyrz')

# You can also add anatomical or functional atlases to highlight visual cortices
#plotting.add_atlas_to_plot(atlas_name='Harvard-Oxford Visual Cortices', threshold=1, colorbar=True)

# Show the plot
plotting.show()

# In[]: Load into fMRI Visual Cortex, Plot the loaded image on a glass brain view

# Load ROI masks
roi_mask1 = nib.load('roi/unq_s1_BAIC3T_LH_ang_d-1to2mm_fmr.img')
roi_mask2 = nib.load('roi/unq_s1_BAIC3T_RH_ang_d-1to2mm_fmr.img')

plotting.plot_roi(roi_mask1,title="Miyawaki atlas in contours")
#plotting.plot_stat_map(fmri_image)
plotting.show()
plotting.plot_roi(roi_mask2)
#plotting.plot_stat_map(fmri_image)
plotting.show()
# In[]: Plot data within ROIs
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(roi_data1, label='ROI 1')
plt.title('Data within ROI 1')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(roi_data2, label='ROI 2', color='orange')
plt.title('Data within ROI 2')
plt.legend()

plt.tight_layout()
plt.show()




