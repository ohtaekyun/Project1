import streamlit as st
import pandas as pd
import matplotlib as mpl
import numpy as np

def main():
    st.title("streamlit 버전: " + str(st.__version__))
    st.title("pandas 버전: " + str(pd.__version__))

if __name__ == "__main__":
    main()