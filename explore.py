import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def bin_classification(data):
    fig, ax = plt.subplots()
    ax.pie(data.label.value_counts(),labels=['Normal','Abnormal'],autopct='%0.2f%%', startangle=90)
    ax.axis('equal')
    ax.legend(loc=3,prop={'size': 6})
    st.pyplot(fig)

def multi_classificaiton(data):
    label = ["Generic","Analysis","Normal",  "Worms","Reconnaissance","DoS, Backdoor, Exploits, Fuzzers"]
    count = [39496 ,1791 ,19488 ,1731 ,16187 ,2480 ]
    fig, ax = plt.subplots()
    ax.pie(count,labels=label,autopct='%0.2f%%', startangle=90)
    ax.axis('equal')
    ax.legend(loc= 3, prop={'size': 6})
    st.pyplot(fig)

def display_results():
    st.write('##### Prediction values vs real values of a slice of dataset')
    st.image("plots/mlp_real_pred_bin.jpg", use_column_width=True)
    st.write('##### Errors, R2-Socre & Accuracy of the model')
    st.image("images/error.jpg", use_column_width=True)
    st.write('##### Precision, Recall & F1-Score of the model')
    st.image("images/confusion.jpg", use_column_width=True)

def load_data():
    data = pd.read_csv('datasets/UNSW_NB15.csv')
    data['service'].replace('-',np.nan, inplace=True)
    data.dropna(inplace=True)
    return data

data = load_data()

def explore_page():
    st.write('# IDS')

    st.write(
        '## Explorer')
    st.write('##### Explore the dataset and its properties')

    st.write('### Binary Classification:')
    st.write('##### Pie chart distribution with normal and abnormal labels')
    bin_classification(data)
    st.write('### Multi-class Classification:')
    st.write('##### Pie chart distribution of multi-class labels')
    multi_classificaiton(data)

    st.write('### Results of training model:')
    display_results()


