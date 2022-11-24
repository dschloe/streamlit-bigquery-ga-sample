import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px 
import iris_utils.utils as utils
from utils import client

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    df = client.query(query).to_dataframe()
    return df

@st.cache
def load_data(query):
    
    df = run_query(query)
    return df 

def run_eda_app():
    st.subheader("탐색적 자료 분석")
    with st.expander("데이터셋 정보"):
        st.markdown(utils.attrib_info)

    # 데이터셋 불러오기
    query = "SELECT * FROM `streamlit-bigquery-ga.datasets.iris`"
    iris_df = load_data(query)

    # 메뉴 지정
    submenu = st.sidebar.selectbox("Submenu", ['기술통계량', '그래프'])
    if submenu == '기술통계량':
        st.dataframe(iris_df)

        with st.expander("Data Types"):
            df2 = pd.DataFrame(iris_df.dtypes).transpose()
            df2.index = ['구분']
            st.dataframe(df2)
        
        with st.expander("기술 통계량"):
            st.dataframe(pd.DataFrame(iris_df.describe()).transpose())
        
        with st.expander("타겟분포 "):
            st.dataframe(iris_df['species'].value_counts())
 
        
    elif submenu == "그래프":
        st.subheader('Plots')
        
        with st.expander("산점도"): 

            # Plotly 그래프
            fig1 = px.scatter(iris_df, x="sepal_width", y="sepal_length",
            color="species", size='petal_width', hover_data=['petal_length'], 
            title='산점도')
            st.plotly_chart(fig1)

        # Layouts 
        col1, col2 = st.columns(2)
        with col1: 
            with st.expander("박스플롯 with Seaborn"): 

                # Seaborn 그래프
                fig, ax = plt.subplots()
                sns.boxplot(iris_df, x = 'species', y = 'sepal_length', ax=ax)
                st.pyplot(fig)
        
        with col2:
            with st.expander("히스토그램 with Matplotlib"):

                # Matplotlib
                fig, ax = plt.subplots()
                ax.hist(iris_df['sepal_length'], color = 'green')
                st.pyplot(fig)

        # Tabls 
        tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])
        with tab1:
            st.write("Tab 1")
            val_species = st.selectbox('종 선택', ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'))
            st.write('종 선택:', val_species)

            result = iris_df[iris_df['species'] == val_species]
            fig1 = px.scatter(result, x="sepal_width", y="sepal_length",
                                      size='petal_width', hover_data=['petal_length'])
            st.plotly_chart(fig1)

        with tab2:
            st.write("Tab 2")