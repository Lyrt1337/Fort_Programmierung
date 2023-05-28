import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

# keywords
# keywords = ["a", "b", "c"]
# keywords = ["a", "b", "c", "d", "e", "f", "g"]
keywords = ["Abra", "Kadabra", "Simsala", "Bim"]

# set up the figure and axes
x_data = np.arange(len(keywords))
y_data = np.arange(len(keywords))

xx, yy = np.meshgrid(x_data, y_data)
x, y = xx.ravel(), yy.ravel()

bottom = np.zeros_like(len(keywords)**2)
width = depth = 1


# ---------
# functions
# ---------
# creating list for all possible pairs [[a, a], [b, a], [b, c], [a, b], ...]
def make_pairs(keywords):
    pair_list = []
    for i in range(0, len(keywords)):
        for j in range(0, len(keywords)):
            temp = [keywords[j], keywords[i]]
            pair_list.append(temp)
    print(pair_list)
    return pair_list


# append pair-list with value = [[a, a, 1], [a, b, 2], ...]
def add_values(pair_list):
    complete_list = pair_list
    for k in range(0, len(pair_list)):
        complete_list[k].append(k+1)
    print(complete_list)
    return complete_list


# take z values from complete list [[a, a, 1], [a, b, 2], ...]
# entspricht dem Value
def get_z_values(complete_list):
    z_values = []
    for i in complete_list:
        z_values.append(i[2])
    print(z_values)
    return z_values


# plot
def plot_3d_bars(x, y, bottom, width, depth, z_values):
    cmap = plt.colormaps.get_cmap('jet')  # Get desired colormap - you can change this!
    max_height = np.max(z_values)  # get range of colorbars so we can normalize
    min_height = np.min(z_values)
    # scale each z to [0,1], and get their rgb values
    rgba = [cmap((k - min_height) / max_height) for k in z_values]

    plt.figure("3D Barchart")
    ax = plt.axes(projection="3d")
    ax.bar3d(x, y, bottom, width, depth, z_values, shade=True, color=rgba, zsort="average")
    ax.set_title(f"Top {len(keywords)} Keyword-Pairs")
    ax.set_xlabel("x", labelpad=12)
    ax.set_ylabel("y", labelpad=12)
    ax.set_zlabel("z", labelpad=12)
    ax.set_xticks(x_data + 0.5)
    ax.set_yticks(y_data + 0.5)
    ax.set_xticklabels(keywords, rotation=0)
    ax.set_yticklabels(keywords, rotation=0)

    # annotation on every bar
    z_index = 0
    for i in range(1, len(keywords)+1):
        for x_1, y_1, z_1 in zip(xx[i-1], yy[i-1], z_values):
            label = f"{z_values[z_index]}"
            ax.text(x_1+0.5, y_1+0.5, z_values[z_index]+1, label,
                    horizontalalignment="center",
                    verticalalignment="center",
                    rotation="vertical"
                    )
            z_index += 1

    plt.show()


pairs = make_pairs(keywords)
complete_list = add_values(pairs)
z_values = get_z_values(complete_list)
plot_3d_bars(x, y, bottom, width, depth, z_values)