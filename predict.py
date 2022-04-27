import streamlit as st
import pickle
import numpy as np

import random, math


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def load_model():
    model = pickle.load(open('models/mlp_binary.pkl', 'rb'))
    return model


model = load_model()


def predict_page():
    st.write('# IDS')

    st.write(
        '## Predictor')
    st.write('#### This is a simple model that predicts whether a given network log is safe or not.')

    rate = st.number_input("Rate", value=truncate(random.uniform(0, 100000), 2), format="%f", key=None, help="",
                           step=1.0, on_change=None, args=None, kwargs=None, disabled=False)
    sttl = st.number_input("STTL (Source to destination time to live value)", value=random.randint(0, 1000), format="%d",
                           key=None, help="", step=1, on_change=None, args=None, kwargs=None, disabled=False)
    sload = st.number_input("sLoad (Source bits per second)", value=truncate(random.uniform(0, 100000), 2), format="%f", key=None,
                            help="", step=1.0, on_change=None, args=None, kwargs=None, disabled=False)
    dload = st.number_input("dLoad (Destination bits per second)", value=truncate(random.uniform(0, 100000), 2), format="%f", key=None,
                            help="", step=1.0, on_change=None, args=None, kwargs=None, disabled=False)
    ct_srv_src = st.number_input("ct_srv_src (No. of connections that contain the same service and source address in 100 connections according to the last time)",
                                 value=random.randint(0, 1000), format="%d", key=None, help="", step=1, on_change=None, args=None, kwargs=None, disabled=False)
    ct_state_ttl = st.number_input("ct_state_ttl (No. for each state according to specific range of values for source/destination time to live)",
                                   value=random.randint(0, 1000), format="%d", key=None, help="", step=1, on_change=None, args=None, kwargs=None, disabled=False)
    ct_dst_ltm = st.number_input("ct_dst_ltm (No. of connections of the same destination address in 100 connections according to the last time)",
                                 value=random.randint(0, 1000), format="%d", key=None, help="", step=1, on_change=None, args=None, kwargs=None, disabled=False)
    ct_src_dport_ltm = st.number_input("ct_src_dport_ltm (No of connections of the same source address and the destination port in 100 connections according to the last time)",
                                       value=random.randint(0, 1000), format="%d", key=None, help="", step=1, on_change=None, args=None, kwargs=None, disabled=False)
    ct_dst_sport_ltm = st.number_input("ct_dst_sport_ltm (No of connections of the same destination address and the source port in 100 connections according to the last time)",
                                       value=random.randint(0, 1000), format="%d", key=None, help="", step=1, on_change=None, args=None, kwargs=None, disabled=False)
    ct_dst_src_ltm = st.number_input("ct_dst_src_ltm (No of connections of the same source and the destination address in in 100 connections according to the last time )",
                                     value=random.randint(0, 1000), format="%d", key=None, help="", step=1, on_change=None, args=None, kwargs=None, disabled=False)
    ct_src_ltm = st.number_input("ct_src_ltm (No. of connections of the same source address in 100 connections according to the last time)",
                                 value=random.randint(0, 1000), format="%d", key=None, help="", step=1, on_change=None, args=None, kwargs=None, disabled=False)
    ct_srv_dst = st.number_input("ct_srv_dst (No. of connections that contain the same service and destination address in 100 connections according to the last time)",
                                 value=random.randint(0, 1000), format="%d", key=None, help="", step=1, on_change=None, args=None, kwargs=None, disabled=False)
    state_CON = st.number_input("state_CON (Indicates to the state and its dependent protocol as CON)", max_value=1, min_value=0,
                                value=random.randint(0,1), format="%d", key=None, help="", step=1, on_change=None, args=None, kwargs=None, disabled=False)
    state_INT = st.number_input("state_INT (Indicates to the state and its dependent protocol as INT)", max_value=1, min_value=0,
                                value=not state_CON, format="%d", key=None, help="", step=1, on_change=None, args=None, kwargs=None, disabled=False)

    ok = st.button("Analyze network log")
    data = []
    if ok:
        data.append([rate, sttl, sload, dload, ct_srv_src, ct_state_ttl, ct_dst_ltm, ct_src_dport_ltm,
                ct_dst_sport_ltm, ct_dst_src_ltm, ct_src_ltm, ct_srv_dst, state_CON, state_INT])
        data = np.array(data)
        prediction = model.predict(data);
        if(prediction[0] == 0):
            st.header(f"The input network log is Normal")
        else:
            st.header(f"This network activity is a Potential Threat")
