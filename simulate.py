from time import sleep
import streamlit as st
import pandas as pd
import random, math


from predict import load_model

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


model = load_model()

def start_simulation():
    col = ["rate","sttl","sload","dload","ct_srv_src","ct_state_ttl","ct_dst_ltm","ct_src_dport_ltm","ct_dst_sport_ltm","ct_dst_src_ltm","ct_src_ltm","ct_srv_dst","state_CON","state_INT", "Prediction"]
    df = pd.DataFrame(columns=col)
    while(True):
        rate = truncate(random.uniform(0, 100000), 2)
        sttl = random.randint(0, 1000)
        sload = truncate(random.uniform(0, 100000), 2)
        dload = truncate(random.uniform(0, 100000), 2)
        ct_srv_src = random.randint(0, 1000)
        ct_state_ttl = random.randint(0, 1000)
        ct_dst_ltm = random.randint(0, 1000)
        ct_src_dport_ltm = random.randint(0, 1000)
        ct_dst_sport_ltm = random.randint(0, 1000)
        ct_dst_src_ltm = random.randint(0, 1000)
        ct_src_ltm = random.randint(0, 1000)
        ct_srv_dst = random.randint(0, 1000)
        state_CON = random.randint(0,1)
        state_INT = (state_CON + 1)%2

        data = [rate, sttl, sload, dload, ct_srv_src, ct_state_ttl, ct_dst_ltm, ct_src_dport_ltm, ct_dst_sport_ltm, ct_dst_src_ltm, ct_src_ltm, ct_srv_dst, state_CON, state_INT]
        
        prediction = model.predict([data])

        if(prediction[0]==0):
            prediction = "Normal"
        else:
            prediction = "Abnormal"

        data.append(prediction)

        sleep(1)

        df = df.append(pd.Series(data, index=col), ignore_index=True)
        # df = pd.DataFrame([data], columns=col)
        
        st.write(df)

def simulate_page():
    st.write('# IDS')

    st.write(
        '## Simulator')
    st.write('##### Explore real time simulation of IDS')
    start = st.button("Start Simulation")

    if(start):
        start_simulation()




 
