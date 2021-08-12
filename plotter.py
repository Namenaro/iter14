from utils import *

def visualise_two_samples(uncon_sample, cond_sample):
    probs1, bins = get_hist(uncon_sample, nbins=20)
    probs2, bins = get_hist(cond_sample, nbins=20)
    fig, ax = plt.subplots()
    ax.bar(bins[:-1], probs1, width=5, color=(0.6,0.1,0.2,0.5))
    ax.bar(bins[:-1], probs2, width=5, color=(0.1,0.6,0.2,0.5))
    plt.ylim(0, 1)
    return fig
