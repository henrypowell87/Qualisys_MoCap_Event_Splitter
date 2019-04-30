"""
Author: Henry Powell
Institution: SoBots Lab, Institute of Neuroscience and Psychology, University
of Glasgow, UK.

Python program for splitting a .tsv file into smaller files partioned by event
markers. This code is designed for the conversion of data files exported after
recordings using the Qualisys Miqus system.

Depends on the datafile not being exported to include frame numbers and time
markers.
"""


import pandas as pd
import numpy as np

# Path to raw data file goes here
file = ''

cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

raw_data = pd.read_csv(file, names=cols, engine='python')

data = raw_data["A"]
data = data.str.split('\t', expand=True)
data = data.drop(columns=[9])

events = data.loc[data[0] == 'EVENT']
event_frames = np.array(events[2], dtype=int)

data_start = data.loc[data[0] == 'marker1 X']
data_start = data_start.index.values.astype(int)[0]

data = data[data_start+1:]
data = data.reset_index(drop=True)

print(event_frames)

i = 0
for event in range(len(event_frames)-1):
    movement = data[event_frames[i]:event_frames[i+1]]
    movement = movement.reset_index(drop=True)
    movement.to_csv('movement' + str(i+1))
    i += 1
