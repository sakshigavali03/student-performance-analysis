import pandas as pd
import matplotlib.pyplot as plt

data = {'Student':['A','B','C','D'], 'Marks':[85,72,90,60]}
df = pd.DataFrame(data)
print(df)

plt.bar(df['Student'], df['Marks'])
plt.title('Student Marks Analysis')
plt.xlabel('Student')
plt.ylabel('Marks')
plt.show()
