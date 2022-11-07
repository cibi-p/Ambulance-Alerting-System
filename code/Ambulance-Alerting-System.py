import numpy as np
import pandas as pd

Graph = {'From':['kandhanchavadi','kandhanchavadi','srp stop'],
        'To':['tidel park','t nagar','tidel park'],
        'Signals':[['s1','s2'],['s1'],['s1','s2','s3']]}

df_graph = pd.DataFrame(Graph)
print(df_graph)
