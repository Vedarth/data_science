df['Gold'] > 0

only_gold = df.where(df['Gold'] > 0)
only_gold.head()

only_gold['Gold'].count()

df['Gold'].count()

only_gold = only_gold.dropna()
only_gold.head()

only_gold = df[df['Gold'] > 0]
only_gold.head()

len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)])

df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]
