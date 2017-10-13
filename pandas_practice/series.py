import pandas as pd
animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)

numbers = [1, 2, 3]
pd.Series(numbers)

import numpy as np
np.nan == None

np.nan == np.nan

np.isnan(np.nan)

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s

s.index

s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
s
