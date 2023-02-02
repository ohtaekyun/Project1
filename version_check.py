import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from search import run_search
from predict import run_predict
from suggestions import run_suggestions


# print('pd.ver: ', pd.__version__)
# print('st.ver: ', st.__version__)
# print('np.ver: ', np.__version__)
# print(option_menu.__version__)
# print(run_search.__version__)
# print(run_predict.__version__)


data = pd.read_csv('data/bds_data.csv', encoding='cp949')
# data2 = data[['SGG_NM', 'BJDONG_NM', 'RENT_GBN', 'RENT_AREA']]
# data3 = data[data2['RENT_GBN']=='월세']
# data4 = data2[data2['RENT_AREA']>=100]
# data5 = data4[data4['BJDONG_NM']=='오금동']
# st.write(data5)
# address1 = data5['RENT_AREA']
# st.write(address1)
# data5['ad'] = address1
# st.write(data5)



data_m = data[data['RENT_GBN']=='월세']
# data_apart = data_m[data_m['HOUSE_GBN_NM']=='아파트']

cols = ['SGG_NM', 'BJDONG_NM']   
st.write(cols)     
st.write(type(cols))
data_addr = data_m[cols]
st.write(data_addr)     
st.write(type(data_addr))
st.write(data_addr.shape)

st.write(data)
st.write(data.shape)

data_addr = data_m[cols].value_counts().reset_index()
st.write(data_addr)
data_addr.columns = ['지역구', '행정동', '거래량']
st.write(data_addr)
st.write(type(data_addr))
# data_addr = data_addr.reset_index(drop=True)
# data_addr.index = data_addr.index+1        
# st.write(data_addr.head(10))

# st.write(data)
# st.write(data2)
# st.write(data3)
# st.write(data4)
# st.title(type(data4))
# st.write(data5)
# st.write(data6)
# st.title(type(address1))