import pandas as pd

df = pd.concat([df, new_row], ignore_index=True)

for column, series in df.items():
    print(column)
