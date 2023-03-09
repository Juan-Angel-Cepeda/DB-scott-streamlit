import streamlit as st
import conection 

st.title("Scott Manager DB Oracle App")

with st.sidebar:
    st.write("What do you want to manipulate")
    botonDepartamentos = st.button("Departments",1,on_click=None)
    botonEmpleados = st.button("Employees",2,on_click=None)

if botonDepartamentos:
    
    st.header("Welcome to departmens, Add, Delete or Updte Departments")
    selectBoxDepartments = st.selectbox("What do you want to do",('Add Department','Modify Department','Delete Department'),index=0)    
    
    deptNumber = st.number_input("Department Number",min_value=0)
    deptName = st.text_input("Department Name")
    deptLocation = st.text_input("Department Location")
    


if botonEmpleados:
    
    st.header("Welcome to employees, Add, Delete or Update Employees")
    
    selectBoxEmployees = st.selectbox("What do you want to do",('Add employee','Modify Employee','Delete Employee'),index=1)
        
    employeeNumber = st.number_input('Employee Id Number',min_value=0)
    employeeName = st.text_input("Employee Name")
    employeeJob = st.text_input("Employee Job")
    employeeManager = st.number_input("Employee Manager Id",min_value=0)
    employeeHireDate = st.date_input("Hire date")
    employeeSalary = st.number_input("Employee Salary")
    employeeCommision = st.number_input("Employee Percentage Commission")
    employeeDepartmentNumber = st.text_input("Employee Department Number")
    saveAddEmployeeButton = st.button('Save Employee')
    
    params_to_send = [employeeNumber,employeeName,employeeJob,employeeManager,employeeHireDate,employeeSalary,
                          employeeCommision,employeeDepartmentNumber
                          ]
    
    
        
    
        

        
