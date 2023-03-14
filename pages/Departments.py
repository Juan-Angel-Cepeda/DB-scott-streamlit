import streamlit as st
import conection as cnn

st.title("Departments")

st.header("Welcome to departmens, Add, Delete or Updte Departments")

with st.container():
                    
        selectBox = st.selectbox("What do you want to do",['Add Department','Modify Department','Delete Department','Search a Department'])
        
        with st.container():
            
            
            
            deptNumber = st.number_input("Department Number",min_value=0)
            deptName = st.text_input("Department Name")
            deptLocation = st.text_input("Department Location")
            
            col1, col2 = st.columns(2)
            with col1:
                botonSendInfoDepts = st.button("Ejecutar")
            with col2:
                botonConsultaBase = st.button("Consultar")
            
            if selectBox == 'Add Department' and botonSendInfoDepts:
                message = cnn.addDe(deptNumber,deptName,deptLocation)
                st.metric(label="status",value=message,delta="added")
            
            elif selectBox == 'Modify Department' and botonSendInfoDepts:
                message = cnn.updateDepartment(deptNumber,deptName,deptLocation)
                st.metric(label="status",value=message,delta="Updated")
            
            elif selectBox == 'Delete Department' and botonSendInfoDepts:
                message = cnn.deleteDepartment(deptNumber)
                st.metric(label="status",value=message,delta="Deleted")
            
            elif selectBox == 'Search a Department' and botonSendInfoDepts:
                
                response = cnn.departmentConection(deptNumber)
                st.table(response)
                
            if botonConsultaBase:
                
                st.subheader("Consulta a la base")
                consultarDepartamentos = cnn.departmentConection()
                st.table(consultarDepartamentos)

with st.container():
    
    st.subheader('Consulta a que departamento pertenece un empleado')
    employeeNumber = st.text_input('Numero de empleado')
    boton_empDept = st.button('Consultar',3)
    if boton_empDept:
        response = cnn.empInDept(employeeNumber)
        st.table(response)
        
    
    