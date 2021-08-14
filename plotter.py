from utils import *

def visualise_two_samples(uncon_sample, cond_sample):
    probs1, bins = get_hist(uncon_sample, nbins=20)
    probs2, bins = get_hist(cond_sample, nbins=20)
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], probs1, width=10, color=(0.7,0.1,0.2,0.5))
    ax.bar(bins[:-1], probs2, width=5, color=(0.1,0.6,0.2,0.8))
    plt.ylim(0, 1)
    return fig

def plot_points_on_pic_first_red(pic, X,Y, colors=None):
    if colors is None:
        colors = 'green'
    fig, ax = plt.subplots()
    plt.imshow(pic, cmap='gray_r')
    plt.scatter(X[0], Y[0], s=100, c='red', marker='o', alpha=0.4)
    plt.scatter(X[1:], Y[1:], s=100, c=colors, marker='o', alpha=0.4)
    return fig