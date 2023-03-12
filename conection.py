import oracledb as Oracle
import json
import re

##PARA CONECCCION

def startConection():
    try:    
        conn = Oracle.connect(user="C##SCOTTS",
            password = "admin",
            dsn = "localhost/xe")
        return conn

    except Exception as err:
        print("Error",err)
        
        
##PARA DEPARTAMENTOS
    
def departmentConection(deptno=0):
    
    connection = startConection()
    cursor = connection.cursor()
    
    if deptno > 0:
        cursor.execute("SELECT * FROM dept WHERE deptno = {}".format(deptno))
        departments = cursor.fetchall()
        resultados = []
        data = {}
        try:
            resultados.append({"deptno" : departments[0][0], "dname" : departments[0][1], "loc" : departments[0][2]})
        except Exception as err:
            data={
                'message': 'Department not found.',
                'error': re.split(r'\n', '{}'.format(err))
            }
        else:
            data = {
                'message': 'Success',
                'departments': resultados
            }
        cursor.close()
        return resultados
    
    else:
        
        cursor.execute("SELECT * FROM dept")
        departments = cursor.fetchall()
        resultado = []
        data = {}
        try:
            for dept in departments:
                resultado.append({"Department Number" : dept[0], "Department Name" : dept[1], "Location" : dept[2]})
        except Exception as err:
            data = {
                'message': 'Departments not found.',
                'error': re.split(r'\n', '{}'.format(err))
            }
        else:
            data = {
                'message': 'Success',
                'departments': resultado
            }
        cursor.close()
        return resultado
        

def addDe(dept_number,dept_name,dept_location):
    connection = startConection()
    cursor = connection.cursor()
    data = {}

    try:
        cursor.callproc('ADDDEPTO', [dept_number,dept_name,dept_location])
    
    except Exception as err:
        data = {
            'message': 'No department inserted.',
            'error': re.split(r'\n', '{}'.format(err))
        }
    else:
        data = {
            'message': 'Success'
        }
    finally:
        connection.commit()
        cursor.close()
        return "Departamento Agregado Correctamente"
    

def updateDepartment(dept_number,dept_name,dept_location):
    
    connection = startConection()
    cursor = connection.cursor()
    
    try:
        cursor.callproc('UPDATEDEPTO', (dept_number,dept_name,dept_location))
    except Exception as err:
        data = {
            'message': 'No department modified.',
            'error': re.split(r'\n', '{}'.format(err))
        }
    else:
        data = {
            'message': 'Success'
        }
    finally:
        connection.commit()
        cursor.close()
        return "Departamento Actualizado Correctamente"
        

def deleteDepartment(deptno):
    connection = startConection()
    cursor = connection.cursor()
    
    try:
        cursor.callproc('DELETEDEPTO', (deptno))
    
    except Exception as err:
        data = {
            'message': 'No department deleted.',
            'error': re.split(r'\n', '{}'.format(err))
        }
    else:
        data = {
            'message': 'Success'
        }
    finally:
        connection.commit
        cursor.close()
        mensaje = "Departamento Eliminado"
        return mensaje


##PARA EMPLEADOS

def employeesConection(empno=0):
    connection = startConection()
    cursor = connection.cursor()
    if empno > 0:
        cursor.execute("SELECT * FROM emp WHERE empno = {}".format(empno))
        employees = cursor.fetchall()
        empleados = []
        data = {}
        try:
            empleados.append({"Numero de Empleado" : employees[0][0], "Nombre del Empleado" : employees[0][1], 
                              "Puesto" : employees[0][2], "Manager" : employees[0][3],
                              "Fecha de contratacion" : employees[0][4], "Salario" : employees[0][5],
                              "Comision" : employees[0][6], "Numero de departamento" : employees[0][7]})
        except Exception as err:
            data = {
                'message': 'Employee not found.',
                'error': re.split(r'\n', '{}'.format(err))
            }
        else:
            data = {
                'message': 'Success',
                'employees': empleados
            }
        cursor.close()
        return empleados
    else:
        cursor.execute("SELECT * FROM emp")
        employees = cursor.fetchall()
        empleados = []
        try:
            for emp in employees:
                empleados.append({"Numero de empleado" : emp[0], "Nombre del empleado" : emp[1],
                                  "Puesto" : emp[2], "Manager" : emp[3], "Fecha de contratacion" : emp[4],
                                  "Salario" : emp[5], "Comision" : emp[6], "Departamento" : emp[7]})
        except Exception as err:
            data = {
                'message': 'Departments not found.',
                'error': re.split(r'\n', '{}'.format(err))
            }
        else:
            data = {
                'message': 'Success',
                'employees': empleados
            }
        cursor.close()
        return empleados


def post(self, request):
    connection = startConection()
    cursor = connection.cursor()
    jd = json.loads(request.body)
    try:
        cursor.callproc('ADD_EMP', (jd['empno'], jd['ename'], jd['job'], jd['mgr'], jd['hiredate'], jd['sal'], jd['comm'], jd['deptno']))
    except Exception as err:
        data = {
            'message': 'No employee inserted.',
            'error': re.split(r'\n', '{}'.format(err))
        }
    else:
        data = {
            'message': 'Success'
        }
    finally:
        cursor.close()
    return json.dump(data)

def put(self, request, empno=0):
    connection = startConection()
    cursor = connection.cursor()
    jd = json.loads(request.body)
    try:
        cursor.callproc('UPDATE_EMP', (empno, jd['atribute'], jd['value']))
    except Exception as err:
        data = {
            'message': 'No employee modified.',
            'error': re.split(r'\n', '{}'.format(err))
        }
    else:
        data = {
            'message': 'Success'
        }
    finally:
        cursor.close()
    return json.dump(data)

def delete(self, request, empno=0):
    connection = startConection()
    cursor = connection.cursor()
    employee = [empno]
    try:
        cursor.callproc('DELETE_EMP', employee)
    except Exception as err:
        data = {
            'message': 'No employee deleted.',
            'error': re.split(r'\n', '{}'.format(err))
        }
    else:
        data = {
            'message': 'Success'
        }
    finally:
        cursor.close()
    return json.dump(data)

def get(self, request, deptno=0):
    connection = startConection()
    cursor = connection.cursor()
    department = [deptno]
    try:
        result = cursor.callfunc('NOEMP_DEPTO', int, department)
    except Exception as err:
        data = {
            'message': 'Department not found.',
            'error': re.split(r'\n', '{}'.format(err))
        }
    else:
        data = {
            'message': 'Success',
            'no_employees': result
        }
    return json.dump(data)

startConection()