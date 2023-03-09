create or replace PROCEDURE addDepto(
    idDept DEPT.DEPTNO%TYPE,
    deptName DEPT.DNAME%TYPE,
    deptLocation DEPT.LOC%TYPE
)
IS
    verificacionNotNull EXCEPTION;
    verificacionUnico EXCEPTION;
    PRAGMA EXCEPTION_INIT(verificacionNotNUll, -02290);
    PRAGMA EXCEPTION_INIT(verificacionUnico, -0001);

BEGIN
    INSERT INTO DEPT(
        deptno,
        dname,
        loc
    )VALUES(
        idDept,
        deptName,
        deptLocation
    );
    DBMS_OUTPUT.PUT_LINE('Departameto Agregado');
EXCEPTION
    WHEN verificacionNotNull THEN
        DBMS_OUTPUT.PUT_LINE('No se pueden insertar datos Nulos');
    WHEN verificacionUnico THEN
        DBMS_OUTPUT.PUT_LINE('Este Valor ya existe');
COMMIT;
END;

create or replace PROCEDURE addEmployee(
    idEmployee EMP.EMPNO%TYPE,
    employeeName EMP.ENAME%TYPE,
    employeeJob EMP.JOB%TYPE,
    employeeManager  EMP.MGR%TYPE,
    employeeHireDate EMP.HIREDATE%TYPE,
    employeeSalary EMP.SAL%TYPE,
    employeeCommission EMP.COMM%TYPE,
    employeeDepartment EMP.DEPTNO%TYPE
)   
    
IS
    
    e_sin_departamento EXCEPTION;  
    verificacionSalario EXCEPTION;
    verificacionNotNull EXCEPTION;
    verificacionUnico EXCEPTION;
    PRAGMA EXCEPTION_INIT(verificacionNotNUll, -02290);
    PRAGMA EXCEPTION_INIT(verificacionUnico, -0001);

BEGIN

    INSERT INTO EMP(
        EMPNO,
        ENAME,
        JOB,
        MGR,
        HIREDATE,
        SAL,
        COMM,
        DEPTNO
    )VALUES(
        idEmployee,
        employeeName,
        employeeJob,
        employeeManager,
        employeeHireDate,
        employeeSalary,
        employeeCommission,
        employeeDepartment

    );
    IF SQL%NOTFOUND THEN
        RAISE e_sin_departamento;
    END IF;
    DBMS_OUTPUT.PUT_LINE('Empleado Agregado');
EXCEPTION        
    WHEN verificacionNotNull THEN
        DBMS_OUTPUT.PUT_LINE('No se pueden insertar datos Nulos');
    WHEN verificacionUnico THEN
        DBMS_OUTPUT.PUT_LINE('Este Valor ya existe');
    WHEN e_sin_departamento THEN
        DBMS_OUTPUT.PUT_LINE('El departamento al que se quiere agregar
        el empleado no existe');
COMMIT;
END;

create or replace PROCEDURE deleteDepto(
    idDepto DEPT.DEPTNO%TYPE
)
IS
    e_registros_dep EXCEPTION;
    PRAGMA EXCEPTION_INIT(e_registros_dep,-02292);
BEGIN
    DELETE FROM DEPT
    WHERE DEPTNO = idDepto;
    COMMIT;
EXCEPTION
    WHEN e_registros_dep THEN
        DBMS_OUTPUT.PUT_LINE('El departamento tiene empleados
        asignados');
END;


create or replace PROCEDURE deleteEmp(
    idEmp EMP.EMPNO%TYPE
)
IS
    e_emp_no_encontrado EXCEPTION;

BEGIN
    DELETE FROM EMP 
    WHERE EMPNO = idEmp;
    IF SQL%NOTFOUND THEN
        RAISE e_emp_no_encontrado;
    END IF;
    COMMIT;
EXCEPTION
    WHEN e_emp_no_encontrado THEN
        DBMS_OUTPUT.PUT_LINE('El empleado no existe');
END;


create or replace PROCEDURE UpdateDepto(
    idDept DEPT.DEPTNO%TYPE,
    deptName DEPT.DNAME%TYPE,
    deptLocation DEPT.LOC%TYPE
)
IS
    sin_departamento EXCEPTION;
    verificacionNotNull EXCEPTION;
    verificacionUnico EXCEPTION;
    PRAGMA EXCEPTION_INIT(verificacionNotNUll, -02290);
    PRAGMA EXCEPTION_INIT(verificacionUnico, -0001);

BEGIN
    UPDATE DEPT SET DNAME = deptName, loc = deptLocation WHERE deptno = idDept;
    IF SQL%NOTFOUND THEN
        RAISE sin_departamento;
    END IF;
    DBMS_OUTPUT.PUT_LINE('Departameto Actualizado');
EXCEPTION
    WHEN verificacionNotNull THEN
        DBMS_OUTPUT.PUT_LINE('No se pueden insertar datos Nulos');
    WHEN verificacionUnico THEN
        DBMS_OUTPUT.PUT_LINE('Este Valor ya existe');
    WHEN sin_departamento THEN
        DBMS_OUTPUT.PUT_LINE('El departamento que intentas actualizar, no existe');
COMMIT;
END;

create or replace PROCEDURE updateEmployee(
    idEmployee EMP.EMPNO%TYPE,
    employeeName EMP.ENAME%TYPE,
    employeeJob EMP.JOB%TYPE,
    employeeManager  EMP.MGR%TYPE,
    employeeHireDate EMP.HIREDATE%TYPE,
    employeeSalary EMP.SAL%TYPE,
    employeeCommission EMP.COMM%TYPE,
    employeeDepartment EMP.DEPTNO%TYPE
)   
    
IS
    e_sin_departamento EXCEPTION;  
    verificacionSalario EXCEPTION;
    verificacionNotNull EXCEPTION;
    verificacionUnico EXCEPTION;

    PRAGMA EXCEPTION_INIT(verificacionNotNUll, -02290);
    PRAGMA EXCEPTION_INIT(verificacionUnico, -0001);

BEGIN

    UPDATE EMP SET
        ENAME = employeeName,
        JOB = employeeJob,
        MGR = employeeManager,
        HIREDATE = employeeHireDate,
        SAL = employeeSalary,
        COMM = employeeCommission,
        DEPTNO = employeeDepartment
        WHERE EMPNO = idEmployee;

    IF SQL%NOTFOUND THEN
        RAISE e_sin_departamento;
    END IF;
    DBMS_OUTPUT.PUT_LINE('Empleado Actualizado');
    COMMIT;
EXCEPTION        
    WHEN verificacionNotNull THEN
        DBMS_OUTPUT.PUT_LINE('No se pueden insertar datos Nulos');
    WHEN verificacionUnico THEN
        DBMS_OUTPUT.PUT_LINE('Este Valor ya existe');
    WHEN e_sin_departamento THEN
        DBMS_OUTPUT.PUT_LINE('El departamento al que se quiere agregar
        el empleado no existe');
END;


create or replace FUNCTION noEmp_depto(
    idEmp EMP.EMPNO%TYPE
)RETURN VARCHAR2
IS
    department_name VARCHAR2(45);

BEGIN
    SELECT DNAME INTO department_name
    FROM DEPT WHERE DEPTNO = (
        SELECT DEPTNO FROM EMP WHERE EMPNO = idEmp
    );
    RETURN department_name;
END noEmp_depto;



