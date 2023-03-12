import streamlit as st
from PIL import Image
import conection as cnn

st.title("Departments")

st.header("Welcome to departmens, Add, Delete or Updte Departments")

with st.container():
                    
        selectBox = st.selectbox("What do you want to do",['Add Department','Modify Department','Delete Department'])
        
        with st.container():
            
            deptNumber = st.number_input("Department Number",min_value=0)
            #st.json(conection.departmentConection(deptNumber))
            deptName = st.text_input("Department Name")
            deptLocation = st.text_input("Department Location")
            
            botonSendInfoDepts = st.button("Send info")
            botonConsultaBase = st.button("Consultar")
            
            if selectBox == 'Add Department' and botonSendInfoDepts:
                cnn.addDe(deptNumber,deptName,deptLocation)
            
            elif selectBox == 'Modify Department' and botonSendInfoDepts:
                #ejecutar update department 
                pass
            
            elif selectBox == 'Delete Department' and botonSendInfoDepts:
                #ejecutar delete department
                pass
                
            if botonConsultaBase:
                
                st.subheader("Consulta a la base")
                consultarDepartamentos = cnn.departmentConection()
                st.table(consultarDepartamentos)

        
    
    