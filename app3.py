# 홈
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
st.title('내방 어디?')
from search import run_search
from predict import run_predict
from suggestions import run_suggestions
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
    st.subheader('홈페이지')
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    cols = ['SGG_NM', 'BJDONG_NM']
    data['주소'] = data[cols].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
    # data['주소']
    data1 = data['주소'].value_counts().rename_axis('주소').reset_index(name='거래 수')
    st.write(data1.head())
    # df_sample = data[['SGG_NM', 'BJDONG_NM']]
    # st.write(df_sample)
    # # st.write(df_sample)
    # data2 = {'주소':data[['SGG_NM']],
    #         '행정동':data[['BJDONG_NM']]
    #         # 'counts':data[['BJDONG_NM']==data2{'행정동'}].value_counts
    #         }
    # st.write(data2)
    # counts = df_sample.value_counts()
    # st.write(counts)
    # # df_sample.value_counts().groupby(level=[0,1])
    # # st.write(df_sample)
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