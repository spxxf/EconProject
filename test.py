import pandas as pd 

dict = {1:1, 2:'four', 3: [ 5, 6, 7]}

df = pd.DataFrame(dict, index = [0, 1, 2])
print(df)
