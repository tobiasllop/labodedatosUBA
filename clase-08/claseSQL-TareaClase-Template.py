# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase.
Autor  : Pablo Turjanski
Fecha  : 2023-03-07
"""

# Importamos bibliotecas
import pandas as pd
from inline_sql import sql, sql_val

def main():

    print()
    print("# =============================================================================")
    print("# Creamos/Importamos los datasets que vamos a utilizar en este programa")
    print("# =============================================================================")

    carpeta = "~/Descargas/clase-08/"
    
    # Ejercicios AR-PROJECT, SELECT, RENAME
    empleado       = get_empleado()
    # Ejercicios AR-UNION, INTERSECTION, MINUS
    alumnosBD      = get_alumnosBD()
    alumnosTLeng   = get_alumnosTLeng()
    # Ejercicios AR-CROSSJOIN
    persona        = get_persona_ejemploCrossJoin()
    nacionalidades = get_nacionalidades()
    # Ejercicios ¿Mismos Nombres?
    se_inscribe_en=get_se_inscribe_en_ejemploMismosNombres()
    materia       =get_materia_ejemploMismosNombres()
    vuelo      = pd.read_csv("vuelo.csv")    
    aeropuerto = pd.read_csv("aeropuerto.csv")    
    pasajero   = pd.read_csv("pasajero.csv")    
    reserva    = pd.read_csv("reserva.csv")    
    # Ejercicio JOIN tuplas espúreas
    empleadoRol= pd.read_csv(carpeta+"empleadoRol.csv")    
    rolProyecto= pd.read_csv(carpeta+"rolProyecto.csv")    
    # Ejercicios funciones de agregación, LIKE, Elección, Subqueries y variables de Python
    examen     = pd.read_csv(carpeta+"examen.csv")
    # Ejercicios de manejo de valores NULL
    examen03 = pd.read_csv(carpeta+"examen03.csv")
    
    
    print()
    print("# =============================================================================")
    print("# Ejemplo inicial")
    print("# =============================================================================")
    
    print(empleado)

    consultaSQL = """
                   SELECT DISTINCT DNI, Salario
                   FROM empleado;
                  """


    dataframeResultado = sql^ consultaSQL
    
    print(dataframeResultado)


    print()
    print("# =============================================================================")
    print("# Ejercicios AR-PROJECT <-> SELECT")
    print("# =============================================================================")
    
    consigna    = "a.- Listar DNI y Salario de empleados "
    consultaSQL = """
                   SELECT DISTINCT DNI, Salario
                   FROM empleado;
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    
    
    # -----------
    consigna    = "b.- Listar Sexo de empleados "
    consultaSQL = """
                   SELECT DISTINCT Sexo,
                   FROM empleado;
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "c.- Listar Sexo de empleados (sin DISTINCT)"
    consultaSQL = """
                   SELECT Sexo,
                   FROM empleado;
                  """                   SELECT DISTINCT *
                   FROM empleado
                   WHERE Sexo = 'F'
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    

    print()
    print("# =============================================================================")
    print("# Ejercicios AR-SELECT <-> WHERE")
    print("# =============================================================================")
    
    consigna    = "a.- Listar de EMPLEADO sólo aquellos cuyo sexo es femenino"
    consultaSQL = """
                   SELECT DISTINCT *
                   FROM empleado                   SELECT DISTINCT *
                   FROM empleado
                   WHERE Sexo = 'F'
                   WHERE Sexo = 'F'
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "b.- Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000"
    consultaSQL = """
                   SELECT DISTINCT *
                   FROM empleado
                   WHERE Sexo = 'F' AND Salario > 15000
                  """
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    
    
    print()
    print("# =============================================================================")
    print("# Ejercicios AR-RENAME <-> AS")
    print("# =============================================================================")
    
    consigna    = """a.- Listar DNI y Salario de EMPLEADO, y renombrarlos como id e Ingreso"""
    consultaSQL = """
                   
                  """
    
    imprimirEjercicio(consigna, [empleado], consultaSQL, sql^consultaSQL)    
 
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    INICIO -->           EJERCICIO Nro. 01                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    # IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

    print()
    print("# =============================================================================")
    print("# EJERCICIOS PARA REALIZAR DE MANERA INDIVUDUAL --> EJERCICIO Nro. 01")
    print("# =============================================================================")

    
    consigna    = "Ejercicio 01.1.- Retornar Codigo y Nombre de los aeropuertos de Londres"
    consultaSQL = """
                  SELECT DISTINCT Codigo, Nombre
                  FROM aeropuerto WHERE Ciudad = 'Londres';
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 01.2.- ¿Qué retorna \n     SELECT DISTINCT Ciudad AS City \n     FROM aeropuerto \n     WHERE Codigo='ORY' OR Codigo='CDG'; ?"
    consultaSQL = """
                  SELECT DISTINCT Ciudad AS City
                  FROM aeropuerto
                  WHERE Codigo='ORY' OR Codigo='CDG';
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 01.3.- Obtener los números de vuelo que van desde CDG hacia LHR"
    consultaSQL = """
                   SELECT numero
                   FROM vuelo
                   WHERE (Origen = 'CDG' AND Destino='LHR');
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 01.4.- Obtener los números de vuelo que van desde CDG hacia LHR o viceversa"
    consultaSQL = """
                   SELECT numero
                   FROM vuelo
                   WHERE (Origen = 'CDG' AND Destino='LHR') OR (Origen = 'LHR' AND Destino='CDG');
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 01.5.- Devolver las fechas de reservas cuyos precios son mayores a $200"
    consultaSQL = """
                   SELECT fecha
                   FROM reserva
                   WHERE precio > 200;
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    
   
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    FIN -->              EJERCICIO Nro. 01                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    
    print()
    print("# =============================================================================")
    print("# Ejercicios AR-UNION, INTERSECTION, MINUS <-> UNION, INTERSECTION, EXCEPT")
    print("# =============================================================================")

    consigna    = """a1.- Listar a los alumnos que cursan BDs o TLENG"""
    
    consultaSQL = """
                   
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL, sql^consultaSQL)    


    # -----------
    consigna    = """a2.- Listar a los alumnos que cursan BDs o TLENG (usando UNION ALL)"""
    
    consultaSQL = """
                   
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL, sql^consultaSQL)    


    # -----------
    consigna    = """b.- Listar a los alumnos que cursan simultáneamente BDs y TLENG"""
    
    consultaSQL = """
                   
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL, sql^consultaSQL)    

    
    # -----------
    consigna    = """c.- Listar a los alumnos que cursan BDs y no cursan TLENG """
    
    consultaSQL = """
                   
                  """

    imprimirEjercicio(consigna, [alumnosBD, alumnosTLeng], consultaSQL, sql^consultaSQL)    


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    INICIO -->           EJERCICIO Nro. 02                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    # IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

    print()
    print("# =============================================================================")
    print("# EJERCICIOS PARA REALIZAR DE MANERA INDIVUDUAL --> EJERCICIO Nro. 02")
    print("# =============================================================================")

    
    consigna    = "Ejercicio 02.1.- Devolver los números de vuelo que tienen reservas generadas (utilizar intersección)"
    consultaSQL = """
                   
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 02.2.- Devolver los números de vuelo que aún no tienen reservas"
    consultaSQL = """
                   
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 02.3.- Retornar los códigos de aeropuerto de los que parten o arriban los vuelos"
    consultaSQL = """
                   
                  """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    



    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    FIN -->              EJERCICIO Nro. 02                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

   
    
    print("# =============================================================================")
    print("# Ejercicios AR-... JOIN <-> ... JOIN")
    print("# =============================================================================")

    consigna    = """a1.- Listar el producto cartesiano entre las tablas persona y nacionalidades"""
    
    consultaSQL = """
                   SELECT DISTINCT *
                   FROM persona
                   CROSS JOIN
                   nacionalidades;
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """a2.- Listar el producto cartesiano entre las tablas persona y nacionalidades (sin usar CROSS JOIN)"""
    
    consultaSQL = """
                   
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)


    # ---------------------------------------------------------------------------------------------- 
    # Carga los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUTER JOIN
    # ----------------------------------------------------------------------------------------------
    persona        = get_persona_ejemplosJoin()
    # ----------------------------------------------------------------------------------------------
    
    
    consigna    = """b1.- Vincular las tablas persona y nacionalidades a través de un INNER JOIN"""
    
    consultaSQL = """
                   SELECT * 
                   FROM persona
                   INNER JOIN nacionalidades
                   ON Nacionalidad=IDN;
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b2.- Vincular las tablas persona y nacionalidades (sin usar INNER JOIN)"""
    
    consultaSQL = """
                   
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """c.- Vincular las tablas persona y nacionalidades a través de un LEFT OUTER JOIN"""
    
    consultaSQL = """
                   SELECT DISTINCT * 
                   FROM persona
                   LEFT OUTER JOIN nacionalidades
                   ON NACIONALIDAD=IDN;
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)
    

    print("# =============================================================================")
    print("# Ejercicios SQL - ¿Mismos Nombres?")
    print("# =============================================================================")

    consigna    = """a.- Vincular las tablas Se_inscribe_en y Materia. Mostrar sólo LU y Nombre de materia"""
    
    consultaSQL = """
                   SELECT DISTINCT LU, Nombre
                   FROM se_inscribe_en
                   INNER JOIN materia
                   ON se_inscribe_en.codigo_materia=materia.codigo_materia
                  """

    imprimirEjercicio(consigna, [persona, nacionalidades], consultaSQL, sql^consultaSQL)
    
    
    
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    INICIO -->           EJERCICIO Nro. 03                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    # IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

    print()
    print("# =============================================================================")
    print("# EJERCICIOS PARA REALIZAR DE MANERA INDIVUDUAL --> EJERCICIO Nro. 03")
    print("# =============================================================================")
    
    consigna    = "Ejercicio 03.1.- Devolver el nombre de la ciudad de partida del vuelo número 165"

    consultaSQL = """
                    SELECT A.ciudad FROM aeropuerto AS A
                    INNER JOIN vuelo as V ON V.origen = A.codigo
                    WHERE V.numero=165;
                  """

    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 03.2.- Retornar el nombre de las personas que realizaron reservas a un valor menor a $200"

    consultaSQL = """
                    SELECT DISTINCT nombre
                    FROM reserva
                    INNER JOIN pasajero
                    ON reserva.DNI = pasajero.DNI
                    WHERE precio < 200
                  """

    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    

    # -----------
    consigna    = "Ejercicio 03.3.- Obtener Nombre, Fecha y Destino del Viaje de todos los pasajeros que vuelan desde Madrid"


    consulta1 = """
                  SELECT *
                  FROM reserva 
                  INNER JOIN pasajero
                  ON reserva.dni = pasajero.dni;
                  """
    tabla1=sql^consulta1
    
    consultaSQL = """
                    SELECT Nombre, Fecha, Destino
                    FROM vuelo
                    INNER JOIN tabla1
                    ON vuelo.numero = tabla1.NroVuelo
                    WHERE vuelo.origen='MAD';
                """
    imprimirEjercicio(consigna, [vuelo, aeropuerto, pasajero, reserva], consultaSQL, sql^consultaSQL)    


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # #                                                                     # #
    # #    FIN -->              EJERCICIO Nro. 03                             # #
     # #                                                                     # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
     # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    
    print("# =============================================================================")
    print("# Ejercicios SQL - Join de varias tablas en simultáneo")
    print("# =============================================================================")

    consigna    = """a.- Vincular las tablas Reserva, Pasajero y Vuelo. Mostrar sólo Fecha de reserva, hora de salida del vuelo y nombre de pasajero."""
    
    consultaSQL = """
                   SELECT DISTINCT r.Fecha, v.Salida, p.Nombre
                   FROM reserva AS r, pasajero AS  p, vuelo AS v
                   WHERE r.DNI = p.DNI AND r.NroVuelo = v.Numero
                  """

    imprimirEjercicio(consigna, [reserva, pasajero, vuelo], consultaSQL, sql^consultaSQL)

    
    print("# =============================================================================")
    print("# Ejercicios SQL - Tuplas espúreas")
    print("# =============================================================================")

    consigna    = """a.- Vincular (JOIN)  EmpleadoRol y RolProyecto para obtener la tabla original EmpleadoRolProyecto"""
    
    consultaSQL = """
                   SELECT DISTINCT er.empleado, er.rol, rolProyecto.proyecto
                   FROM empleadoRol AS er
                   INNER JOIN rolProyecto
                   ON er.rol=rolProyecto.rol;
                  """

    imprimirEjercicio(consigna, [empleadoRol, rolProyecto], consultaSQL, sql^consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Funciones de agregación")
    print("# =============================================================================")

    consigna    = """a.- Usando sólo SELECT contar cuántos exámenes fueron rendidos (en total)"""
    
    consultaSQL = """
                    SELECT count(*) AS CantidadDEExamenes
                    FROM examen
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b1.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia"""
    
    consultaSQL = """
                    SELECT instancia, count(*) AS Asistieron
                    FROM examen
                    GROUP BY instancia;
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b2.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia (ordenado por instancia)"""
    
    consultaSQL = """
               SELECT instancia, count(*) AS Asistieron
                    FROM examen
                    GROUP BY instancia
                    ORDER BY instancia ASC;
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """b3.- Ídem ejercicio anterior, pero mostrar sólo las instancias a las que asistieron menos de 4 Estudiantes"""
    
    consultaSQL = """
                    SELECT instancia, count(*) AS Asistieron
                    FROM examen
                    GROUP BY instancia
                    HAVING asistieron < 4
                    ORDER BY instancia ASC;
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """c.- Mostrar el promedio de edad de los estudiantes en cada instancia de examen"""
    
    consultaSQL = """
                    SELECT instancia, AVG(Edad) as PromedioEdad
                    FROM examen
                    GROUP BY instancia
                    ORDER BY instancia ASC
                    
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - LIKE")
    print("# =============================================================================")

    consigna    = """a1.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial."""
    
    consultaSQL = """
                    SELECT instancia, AVG(Edad) as PromedioEdad
                    FROM examen
                    GROUP BY instancia
                    HAVING instancia='Parcial-01' or instancia='Parcial-02'
                    ORDER BY instancia ASC
                    
                 """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)



    print("# =============================================================================")
    print("# Ejercicios SQL - LIKE")
    print("# =============================================================================")


    # -----------
    consigna    = """a2.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial. Esta vez usando LIKE."""
    
    consultaSQL = """
                    SELECT instancia, AVG(Edad) as PromedioEdad
                    FROM examen
                    GROUP BY instancia
                    HAVING instancia LIKE 'Parcial%' 
                    ORDER BY instancia ASC
                    
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Eligiendo")
    print("# =============================================================================")

    consigna    = """a1.- Listar a cada alumno que rindió el Parcial-01 y decir si aprobó o no (se aprueba con nota >=4)."""
    
    consultaSQL = """
                 SELECT Nombre,
                     Nota,
                     CASE WHEN Nota >= 4
                         THEN 'APROBÓ'
                         ELSE 'NO APROBÓ'
                     END AS Estado,
                     Nota >= 4 AS chequeoDeNuevo
                     FROM examen
                     WHERE Instancia='Parcial-01'
                     ORDER BY NOMBRE
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """a2.- Modificar la consulta anterior para que informe cuántos estudiantes aprobaron/reprobaron en cada instancia."""
    
    consultaSQL = """
                 SELECT instancia,
                    CASE WHEN Nota >= 4
                         THEN 'APROBÓ'
                         ELSE 'NO APROBÓ'
                     END AS Estado,
                     count(*) AS Cantidad
                     FROM examen
                     GROUP BY instancia, Estado
                     ORDER BY instancia, Estado
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Subqueries")
    print("# =============================================================================")

    consigna    = """a.- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia"""
    
    promedios = sql^ """
                        
    SELECT instancia, AVG(Nota) AS Valor
    FROM examen
    GROUP BY instancia
                    """
    examenConPromedio = sql^  """
    SELECT e.*, p.Valor
            FROM examen as e
            INNER JOIN promedios AS p
            ON e.instancia=p.instancia

    """
    consultaSQL = """
                        SELECT NOMBRE, Instancia, Nota
                        From examenConPromedio
                        WHERE Nota >= Valor                            
                  """
    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    consultaSQL2 = """
                    SELECT e1.Nombre, e1.Instancia, e1.Nota
                    FROM examen AS e1
                    WHERE e1.Nota >(
                        SELECT AVG(e2.nota)
                        FROM examen AS e2
                        WHERE e2.Instancia = e1.Instancia)
                    ORDER BY Instancia ASC, Nota DESC;
            """


    # -----------
    consigna    = """b.- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia"""
    
    consultaSQL = """
                    SELECT e1.Nombre, e1.Instancia, e1.Nota
                    FROM examen AS e1
                    WHERE e1.Nota = (
                        SELECT MAX(e2.nota)
                        FROM examen AS e2
                        WHERE e2.Instancia = e1.Instancia)
                    ORDER BY Instancia ASC, Nota DESC;
            """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """c.- Listar el nombre, instancia y nota sólo de los estudiantes que no rindieron ningún Recuperatorio"""
    
    consultaSQL = """
                        SELECT e1.Nombre, e1.Instancia, e1.Nota 
                        FROM examen as e1
                        WHERE NOT EXISTS (
                            SELECT *
                            FROM examen AS e2
                            WHERE e2.Nombre = e1.Nombre AND
                                e2.Instancia LIKE 'Recuperatorio%')
                       ORDER BY e1.Instancia ASC, e1.Nombre ASC;
                    """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Integrando variables de Python")
    print("# =============================================================================")

    consigna    = """a.- Mostrar Nombre, Instancia y Nota de los alumnos cuya Nota supera el umbral indicado en la variable de Python umbralNota"""
    
    umbralNota = 7
    
    consultaSQL = """
                        SELECT e1.Nombre, e1.Instancia, e1.Nota 
                        FROM examen as e1
                        WHERE Nota > $umbralNota;
                  """

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)


    print("# =============================================================================")
    print("# Ejercicios SQL - Manejo de NULLs")
    print("# =============================================================================")

    consigna    = """a.- Listar todas las tuplas de Examen03 cuyas Notas son menores a 9"""
    
    consultaSQL = """
                    SELECT * 
                    FROM examen03 as e3
                    WHERE Nota < 9;
                  """

    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)

    # -----------
    consigna    = """b.- Listar todas las tuplas de Examen03 cuyas Notas son mayores o iguales a 9"""
    
    consultaSQL = """
                    SELECT * 
                    FROM examen03 as e3
                    WHERE Nota >= 9;
                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """c.- Listar el UNION de todas las tuplas de Examen03 cuyas Notas son menores a 9 y las que son mayores o iguales a 9"""
    
    consultaSQL = """
                  SELECT * 
                  FROM examen03 as e1
                  WHERE Nota < 9
                  UNION (SELECT * FROM examen03 as e2
                         WHERE Nota >= 9)
                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """d1.- Obtener el promedio de notas"""
    
    consultaSQL = """
                  SELECT AVG(Nota) as promedio 
                  FROM examen03 as e3
                  
                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)


    # -----------
    consigna    = """d2.- Obtener el promedio de notas (tomando a NULL==0)"""
    
    consultaSQL = """
                  SELECT AVG(CASE WHEN Nota is Null THEN 0 ELSE Nota END) as promedio 
                  FROM examen03 as e3
                  """


    imprimirEjercicio(consigna, [examen03], consultaSQL, sql^consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Desafío")
    print("# =============================================================================")

    consigna    = """a.- Mostrar para cada estudiante las siguientes columnas con sus datos: Nombre, Sexo, Edad, Nota-Parcial-01, Nota-Parcial-02, Recuperatorio-01 y , Recuperatorio-02"""
    
    # ... Paso 1: Obtenemos los datos de los estudiantes
    consultaSQL = """
                    SELECT DISTINCT Nombre, Sexo, Edad
                    FROM examen 
                  """

    datosEstudiantes = sql^ consultaSQL
    
    # ... Paso 2: Agregamos las notas del Parcial-01
    consultaSQL = """
                     SELECT e.*, p.Nota AS Parcial_01
                     FROM datosEstudiantes AS e
                     LEFT OUTER JOIN examen as p
                     ON e.Nombre=p.Nombre AND instancia='Parcial-01'

                  """

    datosHastaParcial01 = sql^ consultaSQL

    # ... Paso 3: Agregamos las notas del Parcial-02
    consultaSQL = """
                     SELECT e.*, p.Nota AS Parcial_02
                     FROM datosHastaParcial01 AS e
                     LEFT OUTER JOIN examen as p
                     ON e.Nombre=p.Nombre AND instancia='Parcial-02'
                  """

    datosHastaParcial02 = sql^ consultaSQL

    # ... Paso 4: Agregamos las notas del Recuperatorio-01
    consultaSQL = """
                     SELECT e.*, p.Nota AS Recuperatorio_01
                     FROM datosHastaParcial02 AS e
                     LEFT OUTER JOIN examen as p
                     ON e.Nombre=p.Nombre AND instancia='Recuperatorio-01'
                  """

    datosHastaRecuperatorio01 = sql^ consultaSQL

    # ... Paso 5: Agregamos las notas del Recuperatorio-02
    consultaSQL = """
                     SELECT e.*, p.Nota AS Recuperatorio_02
                     FROM datosHastaRecuperatorio01 AS e
                     LEFT OUTER JOIN examen as p
                     ON e.Nombre=p.Nombre AND instancia='Recuperatorio-02'
                  """

    datosHastaRecuperatorio02 = sql^ consultaSQL

    desafio_01 = datosHastaRecuperatorio02

    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)

    # -----------
    consigna    = """b.- Agregar al ejercicio anterior la columna Estado, que informa si el alumno aprobó la cursada (APROBÓ/NO APROBÓ). Se aprueba con 4."""
    
    consultaSQL = """
                   SELECT d.*,
                   CASE WHEN ( (Parcial_01>=4 OR Recuperatorio_01>=4)
                   AND
                   (Parcial_02 >= 4 OR Recuperatorio_02 >= 4)
                   )
                   THEN
                          'APROBO'
                   ELSE
                           'NO APOBO'
                   END AS Estado
                   FROM desafio_01 as d
                  """

    desafio_02 = sql^ consultaSQL
    
    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)

    # -----------
    consigna    = """c.- Generar la tabla Examen a partir de la tabla obtenida en el desafío anterior."""
    
    consultaSQL = """
                        SELECT Nombre, Sexo, Edad, 'Parcial-01' AS Instancia, Parcial_01 AS Nota
                        FROM desafio_02
                        WHERE Parcial_01 IS NOT NULL
                        UNION
                        SELECT Nombre, Sexo, Edad, 'Parcial-02' AS Instancia, Parcial_02 AS Nota
                        FROM desafio_02
                        WHERE Parcial_02 IS NOT NULL
                        UNION
                        SELECT Nombre, Sexo, Edad, 'Recuperatorio-01' AS Instancia, Recuperatorio_01 AS Nota
                        FROM desafio_02
                        WHERE Recuperatorio_01 IS NOT NULL
                        UNION
                        SELECT Nombre, Sexo, Edad, 'Recuperaorio-02' AS Instancia, Recuperatorio_02 AS Nota
                        FROM desafio_02
                        WHERE Recuperatorio_02 IS NOT NULL
                  """

    desafio_03 = sql^ consultaSQL
    
    imprimirEjercicio(consigna, [examen], consultaSQL, sql^consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Reemplazos")
    print("# =============================================================================")

    consigna    = """a.- Consigna: En la descripción de los roles de los empleados reemplazar las ñ por ni"""
    
    consultaSQL = """
                    SELECT empleado, REPLACE(rol, 'ñ', 'ni') as rol
                    FROM empleadoRol
                  """

    imprimirEjercicio(consigna, [empleadoRol], consultaSQL, sql^consultaSQL)

    print("# =============================================================================")
    print("# Ejercicios SQL - Mayúsculas/Minúsculas")
    print("# =============================================================================")

    consigna    = """a.- Consigna: Transformar todos los caracteres de las descripciones de los roles a mayúscula"""
    
    consultaSQL = """
                    SELECT empleado, UPPER(rol) as rol
                    FROM empleadoRol
    

                  """

    imprimirEjercicio(consigna, [empleadoRol], consultaSQL, sql^consultaSQL)

    # -----------
    consigna    = """b.- Consigna: Transformar todos los caracteres de las descripciones de los roles a minúscula"""
    
    consultaSQL = """
                  SELECT empleado, LOWER(rol) as rol
                  FROM empleadoRol
    

                  """

    imprimirEjercicio(consigna, [empleadoRol], consultaSQL, sql^consultaSQL)

    # -----------


# =============================================================================
# FUNCIONES PARA LA GENERACIÓN DE DATAFRAMES 
# =============================================================================
def get_empleado():
    # Genera el dataframe "empleado" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. DNI
        # 2. Nombre
        # 3. Sexo
        # 4. Salaro
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    empleado = pd.DataFrame(columns = ['DNI', 'Nombre', 'Sexo', 'Salario'])
    # ... Agregamos cada una de las filas al dataFrame
    empleado = pd.concat([empleado,pd.DataFrame([
        {'DNI' : 20222333, 'Nombre' : 'Diego' , 'Sexo' : 'M', 'Salario' : 20000.0},
        {'DNI' : 33456234, 'Nombre' : 'Laura' , 'Sexo' : 'F', 'Salario' : 25000.0},
        {'DNI' : 45432345, 'Nombre' : 'Marina', 'Sexo' : 'F', 'Salario' : 10000.0}
                                                ])
                        ])
    return empleado


def get_alumnosBD():
    # Genera el dataframe "alumnosBD" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. ID
        # 2. Nombre
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    alumnosBD = pd.DataFrame(columns = ['ID', 'Nombre'])
    # ... Agregamos cada una de las filas al dataFrame
    alumnosBD = pd.concat([alumnosBD,pd.DataFrame([
        {'ID' : 1, 'Nombre' : 'Diego' },
        {'ID' : 2, 'Nombre' : 'Laura' },
        {'ID' : 3, 'Nombre' : 'Marina'}
                                                    ])
                        ])
    return alumnosBD


def get_alumnosTLeng():
    # Genera el dataframe alumnosTLeng que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. ID
        # 2. Nombre
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    alumnosTLeng = pd.DataFrame(columns = ['ID', 'Nombre'])
    # ... Agregamos cada una de las filas al dataFrame
    alumnosTLeng = pd.concat([alumnosTLeng,pd.DataFrame([
        {'ID' : 2, 'Nombre' : 'Laura'    },
        {'ID' : 4, 'Nombre' : 'Alejandro'}
                                                        ])
                        ])
    return alumnosTLeng


def get_persona_ejemploCrossJoin():
    # Genera el dataframe "persona" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. Nombre
        # 2. Nacionalidad
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    persona = pd.DataFrame(columns = ['Nombre', 'Nacionalidad'])
    # ... Agregamos cada una de las filas al dataFrame
    persona = pd.concat([persona,pd.DataFrame([
        {'Nombre' : 'Diego'   , 'Nacionalidad' : 'AR'    },
        {'Nombre' : 'Laura'   , 'Nacionalidad' : 'BR'    },
        {'Nombre' : 'Marina'  , 'Nacionalidad' : 'AR'    }
                                              ])
                        ])
    return persona


def get_persona_ejemplosJoin():
    # Genera el dataframe "persona" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. Nombre
        # 2. Nacionalidad
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    persona = pd.DataFrame(columns = ['Nombre', 'Nacionalidad'])
    # ... Agregamos cada una de las filas al dataFrame
    persona = pd.concat([persona,pd.DataFrame([
        {'Nombre' : 'Diego'   , 'Nacionalidad' : 'BR'    },
        {'Nombre' : 'Laura'   , 'Nacionalidad' : None    },
        {'Nombre' : 'Marina'  , 'Nacionalidad' : 'AR'    },
        {'Nombre' : 'Santiago', 'Nacionalidad' : 'UY'    }
                                              ])
                        ])
    return persona


def get_se_inscribe_en_ejemploMismosNombres():
    # Genera el dataframe "se_inscribe_en" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. LU
        # 2. Codigo_materia
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    se_inscribe_en = pd.DataFrame(columns = ['LU','Codigo_materia'])
    # ... Agregamos cada una de las filas al dataFrame
    se_inscribe_en = pd.concat([se_inscribe_en,pd.DataFrame([
        {'LU':'123/09','Codigo_materia': 1},
        {'LU':' 22/10','Codigo_materia': 1},
        {'LU':' 22/10','Codigo_materia': 2},
        {'LU':'344/09','Codigo_materia': 1}
                                              ])
                        ])
    return se_inscribe_en

def get_materia_ejemploMismosNombres():
    # Genera el dataframe "materia" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. Codigo_materia
        # 2. Nombre
        
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    materia = pd.DataFrame(columns = ['Codigo_materia','Nombre'])
    # ... Agregamos cada una de las filas al dataFrame
    materia = pd.concat([materia,pd.DataFrame([
        {'Codigo_materia': 1, 'Nombre':'Laboratorio de Datos'   },
        {'Codigo_materia': 2, 'Nombre':'Análisis II'   },
        {'Codigo_materia': 3, 'Nombre':'Probabilidad'   }
                                              ])
                        ])
    return materia


def get_nacionalidades():
    # Genera el dataframe "nacionalidades" que contiene las siguientes columnas 
    # (en el orden mencionado):
        # 1. IDN (Id Nacionalidad)
        # 2. Detalle
    
    # ... Creamos el dataframe vacío (sólo con los nombres de sus columnas)
    nacionalidades = pd.DataFrame(columns = ['IDN', 'Detalle'])
    # ... Agregamos cada una de las filas al dataFrame
    nacionalidades = pd.concat([nacionalidades,pd.DataFrame([
        {'IDN' : 'AR', 'Detalle' : 'Agentina'},
        {'IDN' : 'BR', 'Detalle' : 'Brasilera'},
        {'IDN' : 'CH', 'Detalle' : 'Chilena'}
                                                          ])
                        ])
    return nacionalidades

# =============================================================================
# DEFINICION DE FUNCIÓN DE IMPRESIÓN EN PANTALLA
# =============================================================================
# Imprime en pantalla en un formato ordenado:
    # 1. Consigna
    # 2. Cada dataframe de la lista de dataframes de entrada
    # 3. Query
    # 4. Dataframe de salida
def imprimirEjercicio(consigna, listaDeDataframesDeEntrada, consultaSQL, dataframeResultadoDeConsultaSQL):
    
    print("# -----------------------------------------------------------------------------")
    print("# Consigna: ", consigna)
    print("# -----------------------------------------------------------------------------")
    print()
    for i in range(len(listaDeDataframesDeEntrada)):
        print("# Entrada 0",i,sep='')
        print("# -----------")
        print(listaDeDataframesDeEntrada[i])
        print()
    print("# SQL:")
    print("# ----")
    print(consultaSQL)
    print()
    print("# Salida:")
    print("# -------")
    print(dataframeResultadoDeConsultaSQL)
    print()
    print("# -----------------------------------------------------------------------------")
    print("# -----------------------------------------------------------------------------")
    print()
    print()


# =============================================================================
# EJECUCIÓN MAIN
# =============================================================================

if __name__ == "__main__":
    main()
