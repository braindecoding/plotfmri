import nibabel as nib
from nilearn import plotting

# Load fMRI data in Analyze format
img = nib.load('data/ras1_a0005.img')

# Plot the functional MRI data
plotting.plot_epi(img)
plotting.show()
