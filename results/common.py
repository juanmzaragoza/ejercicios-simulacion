from matplotlib import pyplot

def plot_hist(l, bins = 100):
    pyplot.hist(l, bins = 100)
    pyplot.show()