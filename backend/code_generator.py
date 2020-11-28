import json
import openai
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from backend.gpt import set_openai_key
from backend.gpt import GPT
from backend.gpt import Example
set_openai_key()
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)
#df = pd.read_csv("states_all.csv")
df = pd.DataFrame({"Gender": ["boy", "boy", "boy", "boy", "boy", "girl", "girl", "girl", "girl"],
                   "Division": ["one", "one", "one", "two", "two",
                                "one", "one", "two", "two"],
                   "Marks": [50, 55, 67, 85, 44, 84, 65, 56, 87]})
print(df)
gpt.add_example(Example('How many unique values in Division Column?',
                'df["Division"].nunique()'))
gpt.add_example(Example('Find the Division of boy who scored 55 marks',
                'df,loc[(df,loc[:, "Gender"] == "boy") & (df,loc[:, "Marks"] == 55)]'))
gpt.add_example(Example('Find the average Marks scored by Girls',
                'np.mean(df.loc[(df.loc[:, "Gender"] == "girl"), "Marks"])'))

prompt = "Display Division of girl who scored maximum marks"
print(gpt.get_top_reply(prompt))
print(df.loc[(df.loc[:, "Gender"] == "girl") & (df.loc[:, "Marks"] == max(df.loc[:, "Marks"]))])