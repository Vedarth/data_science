df = pd.read_csv('log.csv')
df

df.fillna?

df = df.set_index('time')
df = df.sort_index()
df

df = df.reset_index()
df = df.set_index(['time', 'user'])
df

df = df.fillna(method='ffill')
df.head()
