import numpy as np

def binary_vector(voxelgrid, x_y_z):
    vector = np.zeros(len(voxelgrid))
    vector[np.unique(voxelgrid)] = 1
    return vector.reshape(x_y_z[2], x_y_z[1], x_y_z[0])

def density_vector(voxelgrid, x_y_z):
    vector = np.zeros(len(voxelgrid))
    count = np.bincount(voxelgrid)
    vector[:len(count)] = count
    vector /= len(voxelgrid)
    return vector.reshape(x_y_z[2], x_y_z[1], x_y_z[0])

def plot_feature_vector(feature_vector, cmap="Oranges"):
    fig, axes= plt.subplots(int(np.ceil(feature_vector.shape[0] / 4)), 4, figsize=(8,8))
    plt.tight_layout()
    for i, ax in enumerate(axes.flat):
        if i >= len(feature_vector):
            break
        im = ax.imshow(feature_vector[i], cmap=cmap, interpolation="none")
        ax.set_title("Level " + str(i))
    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    cbar = fig.colorbar(im, cax=cbar_ax)
    cbar.set_label('FEATURE VECTOR')