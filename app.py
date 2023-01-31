import streamlit as st
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import plotly as plot
import sklearn as sk
import numpy as np

def main():
    st.title("streamlit 버전: " + str(st.__version__))
    st.title("pandas 버전: " + str(pd.__version__))
    st.title("matplotlib 버전: " + str(mpl.__version__))
    st.title("seaborn 버전: " + str(sns.__version__))
    st.title("plotly 버전: " + str(plot.__version__))
    st.title("sklearn 버전: " + str(sk.__version__))
    st.title("numpy 버전: " + str(np.__version__))

if __name__ == "__main__":
    main()