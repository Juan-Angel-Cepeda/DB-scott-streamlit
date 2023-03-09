import oracledb as oracle
import json
import re

connection = oracle.connect(
 user = "C##SCOTTS",
 password = "admin",
 dsn = "localhost/xepdb1"
)
    
def get(deptno=0):
    cursor = connection.cursor()
    if deptno > 0:
        cursor.execute("SELECT * FROM dept WHERE deptno = {}".format(deptno))
        departments = cursor.fetchall()
        json_data = []
        try:
            json_data.append({"deptno" : departments[0][0], "dname" : departments[0][1], "loc" : departments[0][2]})
        except Exception as err:
            data={
                'message': 'Department not found.',
                'error': re.split(r'\n', '{}'.format(err))
            }
        else:
            data = {
                'message': 'Success',
                'departments': json_data
            }
        return json.dump(data)
    else:
        cursor.execute("SELECT * FROM dept")
        departments = cursor.fetchall()
        json_data = []
        try:
            for dept in departments:
                json_data.append({"deptno" : dept[0], "dname" : dept[1], "loc" : dept[2]})
        except Exception as err:
            data = {
                'message': 'Departments not found.',
                'error': re.split(r'\n', '{}'.format(err))
            }
        else:
            data = {
                'message': 'Success',
                'departments': json_data
            }
        return json.dump(data)

def post(self, request):
    cursor = connection.cursor()
    jd = json.loads(request.body)
    try:
        cursor.callproc('ADD_DEPTO', (jd['deptno'], jd['dname'], jd['loc']))
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
        cursor.close()
    return json.dump(data)

def put(self, request, deptno=0):
    cursor = connection.cursor()
    jd = json.loads(request.body)
    try:
        cursor.callproc('UPDATE_DEPTO', (deptno, jd['atribute'], jd['value']))
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
        cursor.close()
    return json.dump(data)

def delete(self, request, deptno=0):
    cursor = connection.cursor()
    department = [deptno]
    try:
        cursor.callproc('DELETE_DEPTO', department)
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
        cursor.close()
    return json.dump(data)


def get(self, request, empno=0):
    cursor = connection.cursor()
    if empno > 0:
        cursor.execute("SELECT * FROM emp WHERE empno = {}".format(empno))
        employees = cursor.fetchall()
        json_data = []
        try:
            json_data.append({"empno" : employees[0][0], "ename" : employees[0][1], "job" : employees[0][2], "mgr" : employees[0][3], "hiredate" : employees[0][4], "sal" : employees[0][5], "comm" : employees[0][6], "deptno" : employees[0][7]})
        except Exception as err:
            data = {
                'message': 'Employee not found.',
                'error': re.split(r'\n', '{}'.format(err))
            }
        else:
            data = {
                'message': 'Success',
                'employees': json_data
            }
        return json.dump(data)
    else:
        cursor.execute("SELECT * FROM emp")
        employees = cursor.fetchall()
        json_data = []
        try:
            for emp in employees:
                json_data.append({"empno" : emp[0], "ename" : emp[1], "job" : emp[2], "mgr" : emp[3], "hiredate" : emp[4], "sal" : emp[5], "comm" : emp[6], "deptno" : emp[7]})
        except Exception as err:
            data = {
                'message': 'Departments not found.',
                'error': re.split(r'\n', '{}'.format(err))
            }
        else:
            data = {
                'message': 'Success',
                'employees': json_data
            }
        return json.dump(data)

def post(self, request):
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
