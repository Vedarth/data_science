sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s

s.iloc[3]

s.loc['Golf']

s[3]

s['Golf']

sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)

s.iloc[99]

s = pd.Series([100.00, 120.00, 101.00, 3.00])
s

total = 0
for item in s:
    total+=item
print(total)

total = 0
for item in s:
    total+=item
print(total)

s = pd.Series(np.random.randint(0,1000,10000))
s.head()

len(s)

%%timeit -n 100
summary = 0
for item in s:
    summary+=item

%%timeit -n 100
summary = np.sum(s)
