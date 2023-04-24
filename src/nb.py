import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

# pandas load our data
df = pd.read_csv('../data/ransom.csv')

# matplotlib plots and displays
plt.plot(df.letter, df.frequency)
plt.show()
