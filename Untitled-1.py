#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Pandas'))
	print(os.getcwd())
except:
	pass

#%%
import pandas as pd

df=pd.read_csv("jems.csv")

df.set_index("Film").head()


#%%
import pandas as pd

df=pd.read_csv("jems.csv")

df.ix["Dr. No","Bond actor"]="ANKush"
df.ix["Dr. No"]


