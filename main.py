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


# In[]: Load into fMRI Visual Cortex, Plot the loaded image on a glass brain view
plotting.view_img(fmri_image, threshold=None, cmap='viridis', symmetric_cmap=False,
                  title='fMRI Data on Glass Brain')
plt.savefig('output_plot.png')
plotting.show()


#plot all
#plotAll(folder_path,target_extension,target_path,new_extension)


