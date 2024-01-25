import matplotlib.pyplot as plt
import nibabel as nib
from nilearn import plotting

# In[]: Config
target_path="img/"
folder_path="data/"
target_extension = '.img'
new_extension = '.png'
sbjId = 's1'


# In[]: Load fMRI data in Analyze format
fmri_image  = nib.load(folder_path+'ras1_c0005'+target_extension)
fmri_data = fmri_image.get_fdata()
# In[]: Plot all brain
plotting.plot_epi(fmri_image)
plotting.show()

# In[]:Plot on glass brain with visual cortex activation
plotting.plot_glass_brain(fmri_image, threshold=3.0, colorbar=True, plot_abs=False, display_mode='lyrz')

# You can also add anatomical or functional atlases to highlight visual cortices
plotting.add_atlas_to_plot(atlas_name='Harvard-Oxford Visual Cortices', threshold=1, colorbar=True)

# Show the plot
plotting.show()

# In[]: Load into fMRI Visual Cortex, Plot the loaded image on a glass brain view
from scipy.io import loadmat
#roiBaseName = sprintf('s1_BAIC3T_%s_ang_dm1to2_%s_', 'LH', 'LH');
#roiOrder = {'V1v', 'V2v', 'VP', 'V4v', 'V1d', 'V2d', 'V3', 'V3A'};
#roiBaseName = sprintf('s1_BAIC3T_%s_ang_dm1to2_%s_', 'RH', 'RH');
#roiOrder = {'V1v', 'V2v', 'VP', 'V4v', 'V1d', 'V2d', 'V3', 'V3A'};
roifolder="roi/"
roilname="unq_s1_BAIC3T_LH_ang_dm1to2_%s_"
# Load the MAT-file containing ROI masks
mat_data = loadmat('roi/VOX_s1_BAIC3T_LH_ang_dm1to2_LH_V1v.mat')
mat_data2 = loadmat('roi/VOX_s1_BAIC3T_RH_ang_dm1to2_RH_V1v.mat')
# In[]:
# Access the ROI masks from the loaded dictionary
roi_mask1 = mat_data['VOX_HU071119_BAIC3T_LH_ang_dm1to2_LH_V1v']
roi_mask2 = mat_data2['VOX_HU071119_BAIC3T_RH_ang_dm1to2_RH_V1v']
# In[]:
roi_mask1 = nib.load('roi/roi_mask1.img').get_fdata()
roi_mask2 = nib.load('roi/roi_mask2.img').get_fdata()

# In[]:Extract data within ROIs
roi_data1 = fmri_data[:,roi_mask1 > 0]
roi_data2 = fmri_data[:,roi_mask2 > 0]

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

#plot all
#plotAll(folder_path,target_extension,target_path,new_extension)


