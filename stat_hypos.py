import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import wasserstein_distance, epps_singleton_2samp, ks_2samp
from scipy.spatial.distance import jensenshannon
from scipy.spatial import distance


def measure_samples_difference(sample1, sample2):
    #return epps_singleton_2samp(sample1, sample2)[1]
    return ks_2samp(sample1, sample2, alternative='two-sided', mode='auto')[1]

def measure_hist_difference1(probs1,probs2):
    return wasserstein_distance(probs1,probs2)

def measure_hist_difference2(probs1, probs2):
    return jensenshannon(probs1, probs2, base=2)

def measure_hist_difference3(probs1, probs2):
    return distance.euclidean(probs1, probs2)

