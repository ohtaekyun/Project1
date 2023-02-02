# 홈
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from search import run_search
from predict import run_predict
from suggestions import run_suggestions

st.title('서울 방방콕콕')
selected3 = option_menu(None, ["🏠 Home", "🔎 전월세 검색",  "📊 전세 예측", '💬 건의사항'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "1!important", "background-color": "#ede3d5"},
        "icon": {"color": "gray", "font-size": "15px"},
        "nav-link": {"font-size": "15px", "padding": "5px", "text-align": "left", "margin":"5px", "--hover-color": "#f0afa3"},
        "nav-link-selected": {"margin":"5px", "padding": "5px", "background-color": "#47C83E"},
    }
)

# 홈 탭
if selected3 == "🏠 Home":
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    st.subheader('실거래 현황')
    data2 = data[['SGG_NM', 'BJDONG_NM', 'RENT_GBN', 'RENT_AREA', 'RENT_GTN', 'RENT_FEE', 'CNTRCT_DE', 'BLDG_NM']]
    data2.columns = ['지역구', '행정동', '구분', '면적(m^2)', '보증금', '월세', '계약일', '단지명']
    data2.index = data2.index + 1
    st.write(data2.head(1000))
    (" ")
    (" ")
    (" ")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('월세 실거래수 TOP10')
        
        data_m = data[data['RENT_GBN']=='월세']
        # data_apart = data_m[data_m['HOUSE_GBN_NM']=='아파트']
        
        cols = ['SGG_NM', 'BJDONG_NM']        
        
        data_addr = data_m[cols].value_counts().reset_index(name='거래량')
        data_addr = data_addr.reset_index(drop=True)
        data_addr.index = data_addr.index+1        
        st.write(data_addr.head(10))

    with col2:
        st.subheader('전세 실거래수 TOP10')
        data_m = data[data['RENT_GBN']=='전세']
        cols = ['SGG_NM', 'BJDONG_NM']
        data_addr = data_m[cols].value_counts().reset_index(name='거래량')
        data_addr = data_addr.reset_index(drop=True)
        data_addr.index = data_addr.index+1
        st.write(data_addr.head(10))


# 전월세 검색 탭
elif selected3 == "🔎 전월세 검색":
    run_search()
# 전세 시세 예측 탭
elif selected3 == "📊 전세 예측":
    run_predict()
# 건의사항 탭
elif selected3 == "💬 건의사항":
    run_suggestions()
else:
    selected3 == "🏠 Home"