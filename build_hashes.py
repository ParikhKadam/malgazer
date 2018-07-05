from library.utils import Utils
import pandas as pd
import os


pd.set_option('max_colwidth', 64)

binaries_dir = '/Volumes/JONES/Focused Set May 2018/Binaries'
datapoints = 1024
windowsize = 256
datadir = '/Volumes/JONES/Focused Set May 2018/RWE'

# Load data
all_data, raw_data, classifications = Utils.load_features(datadir, 'rwe', windowsize=windowsize, datapoints=datapoints)

# Pick 60k samples, 10k from each classification
trimmed_data = all_data.groupby('classification').head(10000)
# trimmed_data.to_csv(os.path.join(datadir, 'data.csv'))
pd.DataFrame(trimmed_data.index).to_csv(os.path.join(datadir, 'hashes_60k.txt'), header=False, index=False)
