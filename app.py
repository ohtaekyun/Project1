# 홈
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from search import run_search
from predict import run_predict
from suggestions import run_suggestions

st.title('내방 어디?')
selected3 = option_menu(None, [":집:Home", ":렌즈가_오른쪽_위에_있는_확대경:전월세 검색",  ":막대_차트:전세 예측", ':말풍선:건의사항'],
    # icons=['house', 'cloud-upload', "list-task", 'gear'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#FAFAFA"},
        "icon": {"color": "gray", "font-size": "15px"},
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#47C83E"},
    }
)
# 홈 탭
if selected3 == ":집:Home":
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    st.subheader('실거래 현황')
    data2 = data[['SGG_NM', 'BJDONG_NM', 'RENT_GBN', 'RENT_AREA', 'RENT_GTN', 'RENT_FEE', 'CNTRCT_DE', 'BLDG_NM']]
    data2.columns = ['지역구', '행정동', '구분', '면적(m^2)', '보증금', '월세', '계약일', '건물명']
    data2.index = data2.index + 1
    st.write(data2.head(1000))
    (" ")
    (" ")
    (" ")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('월세 실거래수 지역 순위')
        data_m = data[data['RENT_GBN']=='월세']
        cols = ['SGG_NM', 'BJDONG_NM']
        data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
        data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
        data_addr = data_addr.reset_index(drop=True)
        data_addr.index = data_addr.index+1
        st.write(data_addr.head(10))
    with col2:
        st.subheader('전세 실거래수 지역 순위')
        data_m = data[data['RENT_GBN']=='전세']
        cols = ['SGG_NM', 'BJDONG_NM']
        data_m['주소'] = data_m[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
        data_addr = data_m['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
        data_addr = data_addr.reset_index(drop=True)
        data_addr.index = data_addr.index+1
        st.write(data_addr.head(10))
# 전월세 검색 탭
elif selected3 == ":렌즈가_오른쪽_위에_있는_확대경:전월세 검색":
    run_search()
# 전세 시세 예측 탭
elif selected3 == ":막대_차트:전세 예측":
    run_predict()
# 건의사항 탭
elif selected3 == ":말풍선:건의사항":
    run_suggestions()
else:
    selected3 == ":집:Home"