import numpy as np
s = pd.Series(np.random.uniform(size=100))
fig = pd.plotting.bootstrap_plot(s)
