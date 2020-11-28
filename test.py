import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({"Gender": ["boy", "boy", "boy", "boy", "boy", "girl", "girl", "girl", "girl"],
                   "Division": ["one", "one", "one", "two", "two",
                                "one", "one", "two", "two"],
                   "Marks": [50, 55, 67, 85, 44, 84, 65, 56, 87]})
#print(df)
