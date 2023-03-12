import streamlit as st
st.title("Employees")


st.header("Welcome to employees, Add, Delete or Update Employees")

with st.container():
    
    selectBoxEmployees = st.selectbox("What do you want to do",['Add employee','Modify Employee','Delete Employee'])
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
    