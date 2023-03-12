import streamlit as st
import conection as cnn
from PIL import Image

fing = Image.open('./sources/logo ingenieria.png')
uach = Image.open('./sources/1200px-Escudo_UACH.png')


    
#conn = conection.startConection()
col1, col2, col3 = st.columns(3)    

with col1:
    st.image(fing,width=100)
with col3:
    st.image(uach,width=100)

st.title("Scott Manager DB Oracle App")    
st.header("Proyecto primer parcial Bases de Datos Avanzadas")
st.subheader("338832 Juan Ángel Cepeda Fernández")
st.text("Bases de datos avanzadas")




        
    
        

        
