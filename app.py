import streamlit as st
import pickle
import numpy as np
import pandas as pd




pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl','rb'))

st.title('Laptop Price Predictor')

company = st.selectbox('Brand',df['Company'].unique())
type_name = st.selectbox('Type',df['TypeName'].unique())
Ram = st.selectbox('Ram (in GB)',[2,4,6,8,16,24,32,64])
weight = st.number_input(label='Weight of the Laptop')

ips = st.selectbox('IPS',[0,1])
screen_size = st.slider('Screensize in inches', 10.0, 18.0, 13.0)
resolution = st.selectbox('Resolution',['1366x768','1536x864' ,'1440x900','1280x720',
'1600x900','2560x1440','1920x1080'])
cpu = st.selectbox('CPU',df['cpu brand'].unique())
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])
gpu = st.selectbox('GPU',df['Gpu brand'].unique())
os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):

    ppi = None

    if ips == 'yes':
        ips = 1
    else:
        ips = 0


    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2 + Y_res**2) ** 0.5) / screen_size


    query = pd.DataFrame([{
        'Company': company,
        'TypeName': type_name,
        'Ram': Ram,
        'Weight' : weight,
        'Ips' : ips,
        'Screensize' : screen_size,
        'ppi' : ppi,
        'Resolution' : resolution,
        'cpu brand' : cpu,
        'HDD' : hdd,
        'SSD' : ssd,
        'Gpu brand' : gpu,
        'os' : os

    }])


    st.title("The Predicted Price is : "+ str(int(np.exp(pipe.predict(query)[0]))))












