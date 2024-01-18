#from helper.plot import plotAll
import nibabel as nib
from nilearn import plotting, image, regions

# Config
target_path="img/"
folder_path="data/"
target_extension = '.img'
new_extension = '.png'


# Load fMRI data in Analyze format
img = nib.load(folder_path+'ras1_a0005'+target_extension)


# Create a mask defining the ROI (for example, a sphere) based on the ROI HDR file
sphere_roi = regions.sphere(affine=img.affine)

# Plot the ROI
plotting.plot_roi(sphere_roi, title='ROI Visualization', display_mode='ortho', cut_coords=[40, 40, 40])

# Show the plot
plotting.show()



#plot all
#plotAll(folder_path,target_extension,target_path,new_extension)


