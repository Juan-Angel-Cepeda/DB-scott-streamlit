import streamlit as st
import conection as cnn
st.title("Employees")


st.header("Welcome to employees, Add, Delete or Update Employees")

with st.container():
    
    selectBoxEmployees = st.selectbox("What do you want to do",['Add employee','Modify Employee',
                                                                'Delete Employee', 'Search Employee'])
    
    with st.container():  

        employeeNumber = st.number_input('Employee Id Number',min_value=0)
        employeeName = st.text_input("Employee Name")
        employeeJob = st.text_input("Employee Job")
        employeeManager = st.number_input("Employee Manager Id",min_value=0)
        employeeHireDate = st.date_input("Hire date")
        employeeSalary = st.number_input("Employee Salary")
        employeeCommision = st.number_input("Employee Percentage Commission")
        employeeDepartmentNumber = st.text_input("Employee Department Number")
        
    
    col1, col2 = st.columns(2)
    
    with col1:
        ejecutarButton = st.button('Ejecutar')
    with col2:
        consultarBaseBoton = st.button('Consultar')
        
    if selectBoxEmployees == 'Add employee' and ejecutarButton:
        pass
    elif selectBoxEmployees == 'Modify Employee' and ejecutarButton:
        pass
    elif selectBoxEmployees == 'Delete Employee' and ejecutarButton:
        pass
    
    elif selectBoxEmployees == 'Search Employee' and ejecutarButton:
        response = cnn.employeesConection(employeeNumber)
        st.table(response)
    
    if consultarBaseBoton:
        
        st.subheader("Consulta a la base")
        consultarDepartamentos = cnn.employeesConection()
        st.table(consultarDepartamentos)
    