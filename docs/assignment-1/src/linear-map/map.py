# ========================================
# [] File Name : map.py
#
# [] Creation Date : February 2018
#
# [] Created By : Ali Gholami (aligholami7596@gmail.com)
# ========================================

"""
    Implementation of a linear transformation on a multivariate Gaussian distribution.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.stats import multivariate_normal

MEAN_VECTOR = np.array([0,0])

COV_MATRIX = np.array([
    [1, 0],
    [0, 1]
])

# Transformation configuration
A_T = np.array([
    [-5, 5],
    [1, 1]
])

B_T = np.array([0.5, 1])

# Linear transformation
def linear_map(transformation_matrix, bias_matrix, data):
    '''
        Performs a matrix multiplication as a linear map
        also translates the new mean vector and covariance matrix
    '''
    Y = np.matmul(transformation_matrix, np.transpose(data)) + bias_matrix

    return Y

# Function to plot each distribution
def plot_dists(samples):
    '''
        This will plot normal surface for each sample set
    '''

    x = samples[:, 0]
    y = samples[:, 1]
    x, y = np.meshgrid(x, y)
    xy = np.column_stack([x.flat, y.flat])

    # Use multivariate normal as the result for Z
    z = multivariate_normal.pdf(xy, mean=MEAN_VECTOR.tolist(), cov=COV_MATRIX.tolist())
    z = z.reshape(x.shape)

    # Plot
    FIG = plt.figure()
    AX = Axes3D(FIG)

    SURF = AX.plot_surface(x, y, z, cmap=cm.winter)
    FIG.colorbar(SURF, shrink=0.5, aspect=5)

    plt.show()
    
# Generate Gaussian samples and plot the results
GAUSSIAN_SAMPLES = np.random.multivariate_normal(MEAN_VECTOR, COV_MATRIX, size=500)
plot_dists(GAUSSIAN_SAMPLES)

# Transform the Gaussian samples
TRANSFORMED_SAMPLES = np.array([])
for point in GAUSSIAN_SAMPLES:
    TRANSFORMED_SAMPLES = np.append(TRANSFORMED_SAMPLES, linear_map(data=point, transformation_matrix=A_T, bias_matrix=B_T))
    
# Reshape the transformed samples like GAUSSIAN SAMPLES
TRANSFORMED_SAMPLES = TRANSFORMED_SAMPLES.reshape((500, 2))

# Plot the transformed samples
plot_dists(TRANSFORMED_SAMPLES)




