import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from search import run_search
from predict import run_predict
from suggestions import run_suggestions


print('pd.ver: ', pd.__version__)
print('st.ver: ', st.__version__)
print('np.ver: ', np.__version__)
# print(option_menu.__version__)
# print(run_search.__version__)
# print(run_predict.__version__)