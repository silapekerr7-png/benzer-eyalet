import streamlit as st
import pandas as pd
import pickle

st.title("Benzer Eyalet Öneri Sistemi :world_map:")
st.write("Kronik hastalık göstergelerine göre seçtiğiniz eyalete en çok benzeyen eyaletler.")
nn=pickle.load(open('eyalet_nn.pkl','rb'))
xs=pickle.load(open('eyalet_veri.pkl','rb'))

eyalet=st.selectbox('Eyalet seçin',sorted(xs.index.tolist()))
n=st.slider('Kaç öneri?',1,10,5)
if st.button('Öner'):
    idx=list(xs.index).index(eyalet)
    uzaklik,indeks=nn.kneighbors(xs.iloc[[idx]].values,n_neighbors=int(n)+1)
    sonuc=pd.DataFrame({'eyalet':xs.index[indeks[0][1:]],'benzerlik':(1-uzaklik[0][1:]).round(3)})
    st.write(sonuc)
