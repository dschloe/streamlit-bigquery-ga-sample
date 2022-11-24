# -*- coding:utf-8 -*-
import streamlit as st 
import streamlit.components.v1 as stc 
from iris_utils.eda_app import run_eda_app
from iris_utils import utils

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">IRIS 머신러닝 모형</h1>
		</div>
		"""

dec_temp ="""
### IRIS 예측 모델 개발
- IRIS 데이터를 활용하여 간단한 EDA 및 예측 모델을 구현한다. 
#### 데이터
    + https://www.kaggle.com/datasets/saurabh00007/iriscsv
"""

def main():
    stc.html(html_temp)

    menu = ["HOME", "탐색적 자료 분석", "머신러닝", "About"]
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == "HOME":
        st.subheader("Home")
        st.markdown(dec_temp, unsafe_allow_html=True)
    elif choice == "탐색적 자료 분석":
        run_eda_app()
    elif choice == "머신러닝":
        pass
    else: 
        st.subheader("About")

if __name__ == "__main__":
    main()