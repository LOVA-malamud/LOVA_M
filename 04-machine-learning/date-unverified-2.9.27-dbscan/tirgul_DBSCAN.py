import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from sklearn.cluster import DBSCAN

DATA_DIR = Path(__file__).resolve().parent
moons = pd.read_csv(DATA_DIR / 'cluster_moons.csv')

print(moons.head())
