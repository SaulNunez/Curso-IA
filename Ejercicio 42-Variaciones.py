from __future__ import print_function
import sys
PY3 = sys.version_info[0] == 3
if PY3:
    xrange = range
import numpy as np
from numpy import random
import cv2 as cv
def make_gaussians(cluster_n, img_size):
    points=[]
    ref_distrs=[]
    for _i in xrange(cluster_n):
        mean = (0.1 + 0.8 * random.rand(2)) * img_size
        a = (random.rand(2,2)-0.5) * img_size * 0.1
        cov = np.dot(a.T, a) + img_size * 0.05*np.eye(2)
        n = 100 + random.randint(900)
        pts