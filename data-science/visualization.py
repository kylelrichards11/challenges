from matplotlib import pyplot as plt

def plot_timestamp_feature(x, y, title="", xlabel="", ylabel="", c=None):
    """ Plots a single feature against the timestamp """
    fig = plt.figure(num=None, figsize=(16, 10))
    ax1 = fig.add_subplot(111)
    ax1.set_title(title)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.plot(x, y, c=c)
    plt.show()

def plot_scatter_2d(x, y, title="", xlabel="", ylabel="", c=None):
    """ Makes a 3D scatter plot for given x, y, and z """
    fig = plt.figure(num=None, figsize=(32, 10))
    ax1 = fig.add_subplot(111)
    ax1.scatter(x, y, c=c)
    ax1.set_title(title)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    plt.show()

def plot_results(data, machine_num):
    """ Plots results splitting the different predictions into their respective colors """
    outliers = data[data["predictions"] == 3]
    data = data[data["predictions"] != 3]
    breaks = data["predictions"].diff().fillna(0)
    breaks.iloc[-1] = 1
    groupings = []
    prev_i = 0
    for i, row in breaks.iteritems():
        if row != 0:
            groupings.append((prev_i, i))
            prev_i = i
    for i in range(4):
        fig = plt.figure(num=None, figsize=(32, 10))
        ax1 = fig.add_subplot(111)
        ax1.set_xlabel("Timestamp")
        ax1.set_ylabel(f"Feature {i} Value")
        ax1.set_title(f"Final Results for Machine {machine_num}, Feature {i}")
        ax1.scatter(outliers["timestamp"], outliers["0"], color="grey", s=2)
        for group in groupings[1:]:
            group_data = data.loc[group[0]:group[1], :]
            ax1.plot(group_data["timestamp"], group_data[f"{i}"], color=group_data["colors"].iloc[0])
        plt.show()