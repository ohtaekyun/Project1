import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

# import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap'); 

# html, body, [class*="css"] {
#     font-family: 'Roboto', sans-serif; 
#     font-size: 10;
#     font-weight: 500;
#     color: #091747;
# }

# with open( "app\style.css" ) as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.title('방방콕콕')

from search import run_search
from predict import run_predict
from suggestions import run_suggestions

selected3 = option_menu(None, ["🏠Home", "🔎전월세 검색",  "📊전세 시세 예측", '💬건의사항'], 
    # icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#47C83E"},
    }
)

# 홈 탭
if selected3 == "🏠Home":
    st.subheader('가장 HOT한 동네는 어디? (전세+월세 기준)')
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    # st.write(data.head())
    # st.dataframe(data, 200, 100)
    # st.write(data.columns)
    # st.write(data.shape)
    # df_sample = data.loc[0:10, 'SGG_CD', 'FLR_NO', 'CNTRCT_DE']
    # st.dataframe(df_sample)
    # st.write(df_sample['지역구'].unique())
    # df_sample_value.columns = ['a']
    # list1 = df_sample['행정동'].tolist()
    # st.write(df_sample)
    goo = data[['SGG_NM']]
    st.write(goo)
    st.write(goo.type)
    a = data[['SGG_NM', 'BJDONG_NM']]
    st.write(a)

    # b = data.groupby('SGG_NM').BJDONG_NM.value_counts(normalize=True)
    # st.write(b)



    cols = ['SGG_NM', 'BJDONG_NM']
    a['구/동'] = a[cols].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    st.write(a)
    st.write(a['구/동'].value_counts())
    st.write(a['구/동'].head(10))
    a['구/동'].value_counts()
    st.write(a['구/동'].value_counts())
    a['거래횟수'] = a['구/동'].value_counts()
    st.write(a['거래횟수'])
    st.write(a['구/동', '거래횟수'])














                           


    st.write('top1: 강서구 마곡동(8894회)')
    st.write('top2: 노원구 상계동(6000회)')
    st.write('top3: 양천구 신정동(5000회)')
    st.write('top4: 은평구 진관동(4500회)')
    st.write('top5: 송파구 거여동(3200회)')


    df_sample = data[['SGG_NM', 'BJDONG_NM']] 
    st.write(df_sample)
    # st.write(df_sample)
    data2 = {'주소':data[['SGG_NM']],
            '행정동':data[['BJDONG_NM']]
            # 'counts':data[['BJDONG_NM']==data2{'행정동'}].value_counts
            }

    
    st.write(data2)
    st.write(type(data2))
    st.write(df_sample.value_counts())
    df_sample.value_counts().groupby(level=[0,1])
    st.write(df_sample)

    # grouped = df.groupby([df.index.get_level_values(0),'Num']).size()
    
    
    # df = pd.DataFrame(data2)
    # st.write(df)


    # df_sample.columns = ['지역구','행정동']  
    # df = pd.DataFrame(df_sample.value_counts())





    # st.write(type(df_sample))
    # st.write(type(df_sample_value))

     

    

    # st.write(df_sample.loc[0][0])
    # st.write(df_sample.loc[0][1])
    # st.write(df_sample_value.loc[[1],[1]])
    # st.write(df_sample_value.loc[[1],[2]])
    
    
    
    
    



    
    # st.write('count = f'{df_sample['행정동'].count()}'')
    # f'{df_sample['행정동'].count()}
   


# 전월세 검색 탭
elif selected3 == "🔎전월세 검색":
    run_search()

# 전세 시세 예측 탭 
elif selected3 == "📊전세 시세 예측":
    run_predict()

# 건의사항 탭
elif selected3 == "💬건의사항":
    run_suggestions()
else:
    selected3 == "🏠Home"