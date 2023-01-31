import streamlit as st
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import numpy as np

def main():

    st.title('월세 볼래?')
    (" ")
    (" ")
    (" ")
    (" ")
    (" ")
    
    st.info('추천매물1')
    st.success('추천매물2')
    st.error('추천매물3')
    (" ")
    (" ")
    (" ")

    
    st.button('홈으로')
    st.button('다음페이지')
    st.button('건의사항')
    
    
    submenu = st.sidebar.title('시세 검색')

    submenu_lists1 = ["영등포구", '관악구', '구구구']
    submenu = st.sidebar.selectbox('지역', submenu_lists1)

    submenu_lists4 = ["영등포 1동", '영등포 2동', '영등포 3동']
    submenu = st.sidebar.selectbox('동/읍/면', submenu_lists1)

    submenu_lists2 = ["30미만", '30이상 40미만', '40이상 50미만']
    submenu = st.sidebar.selectbox('월세', submenu_lists2)

    submenu_lists3 = ["500미만", '500이상 2000이하', '2000이상 5000미만']
    submenu = st.sidebar.selectbox('보증금', submenu_lists3)

    submenu_lists5 = ["아파트", '오피스텔', '빌라']
    submenu = st.sidebar.selectbox('건물 타입', submenu_lists5)





if __name__ == "__main__":
    main()