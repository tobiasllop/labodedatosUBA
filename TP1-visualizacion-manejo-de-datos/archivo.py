# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Trabajo práctico 1
Autores : Tobias Llop, Felipe Pasquet, Delfina Stabile
"""

#Importamos bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from inline_sql import sql, sql_val

#Importamos nuestros datos
carpeta = "..."

stablmnt = pd.read_csv(carpeta + "/tablasoriginales/distribucion_establecimientos_productivos_sexo.csv")
oper_org = pd.read_csv( carpeta + "/tablasoriginales/padron-de-operadores-organicos-certificados.csv")
claedict = pd.read_csv(carpeta + '/tablasoriginales/clae_agg.csv')
localidades = pd.read_csv( carpeta + '/tablasoriginales/localidad_bahra.csv')
localidadesExtra = pd.read_csv(carpeta + '/tablasoriginales/departamentos.csv')
rubro_clae2 = pd.read_csv(carpeta + '/tablasoriginales/rubro_clae2.csv')

 # =============================================================================
 # Creamos los datasets que utilizaremos
 # =============================================================================

#Entidades
clae2 = pd.DataFrame({'codigo':[],'descripcion':[], 'letra':[]})
Letra= pd.DataFrame({'letra':[]})
op_organicos = pd.DataFrame({'razon_social':[],'establecimiento':[], 'id_depto': [], 'nombre_rubro':[]})
est_productivos = pd.DataFrame({'id':[],'porcentaje_mujeres':[], 'id_depto': [], 'cod_clae2':[]})
provincia = pd.DataFrame({'id':[], 'nombre':[]})
depto = pd.DataFrame({ 'id' :[], 'nombre':[], 'id_provincia': []})
producto = pd.DataFrame({'nombre': []})

#Relaciones
op_organico_produce = pd.DataFrame({'razon_social':[], 'establecimiento':[], 'producto':[]})

 # =============================================================================
 # Consultas GQM
 # =============================================================================

##GQM claeDict proporción  de datos repetidos
print(sql^("""
            WITH Repetidos AS (
                SELECT clae2, clae2_desc, letra, COUNT(*) as cuenta
                FROM claedict
                GROUP BY clae2, clae2_desc, letra
                HAVING COUNT(*) > 1
            )

            SELECT
                (CAST((SUM(cuenta) - COUNT(*)) AS FLOAT) / CAST((SELECT COUNT(*) FROM claedict) AS FLOAT) * 100) AS ProporcionRepetidosClae
            FROM Repetidos;

        """))

##GQM localidades_Bahra proporción  de datos repetidos
print(sql^("""
            WITH Repetidos AS (
                SELECT nombre_departamento, codigo_indec_departamento, nombre_provincia, codigo_indec_provincia, COUNT(*) as cuenta
                FROM localidades
                GROUP BY nombre_departamento, codigo_indec_departamento, nombre_provincia, codigo_indec_provincia
                HAVING COUNT(*) > 1
            )

            SELECT
            (CAST((SUM(cuenta) - COUNT(*)) AS FLOAT) / CAST((SELECT COUNT(*) FROM localidades) AS FLOAT) * 100) AS ProporcionRepetidosLoc
            FROM Repetidos;

        """))

##GQM padron-de-operadores-organicos-certificados proporción de datos nulos y repetidos
cantidad_de_ncs = sql^("""
                        SELECT COUNT(establecimiento)
                        FROM oper_org
                        WHERE establecimiento = 'NC'
                       """)
cantidad_total = sql^("""
                      SELECT COUNT(establecimiento)
                      FROM oper_org
                      """)
print("proporción de NC's: \n", cantidad_de_ncs/cantidad_total * 100)

#Fuente operadores orgánicos sin NCs
oper_org_2 = oper_org.copy()
for i in range(len(oper_org_2['establecimiento'])):
  if oper_org_2['establecimiento'][i] == 'NC':
      oper_org_2.at[i, 'establecimiento'] = oper_org_2['razón social'][i]
  i+=1

print(sql^("""
            WITH Repetidos AS (
                SELECT pais_id, pais, provincia_id, provincia, departamento, localidad, rubro, productos, categoria_id, categoria_desc, Certificadora_id, certificadora_deno, 'razón social', establecimiento, COUNT(*) as cuenta
                FROM oper_org_2
                GROUP BY pais_id, pais, provincia_id, provincia, departamento, localidad, rubro, productos, categoria_id, categoria_desc, Certificadora_id, certificadora_deno, 'razón social', establecimiento
                HAVING COUNT(*) > 1
            )

            SELECT
            (CAST((SUM(cuenta) - COUNT(*)) AS FLOAT) / CAST((SELECT COUNT(*) FROM oper_org_2) AS FLOAT) * 100) AS ProporcionRepetidosOper_org
            FROM Repetidos;

        """))

 # =============================================================================
 # Limpieza de datos
 # =============================================================================

#Localidades
localidades['nombre_departamento'] = localidades['nombre_departamento'].str.split(',')
localidades['codigo_indec_departamento'] = localidades['codigo_indec_departamento'].str.split(',')
localidades = localidades.explode(['nombre_departamento', 'codigo_indec_departamento'])
departamentosTierraDelFuego = sql^("SELECT DISTINCT id, nombre, provincia_id as id_provincia FROM localidadesExtra WHERE provincia_id = '94'")

#Operadores Organicos
oper_org_cop = oper_org.copy()
#Reemplazamos los NC por el nombre del establecimiento
for i in range(len(oper_org_cop['establecimiento'])):
  if oper_org_cop['establecimiento'][i] == 'NC':
      oper_org_cop.at[i, 'establecimiento'] = oper_org_cop['razón social'][i]
  i+=1

#Eliminamos elementos duplicados
oper_org_cop = sql^("SELECT DISTINCT * FROM oper_org_cop")

 # =============================================================================
 # Agregamos datos a nuestros datasets
 # =============================================================================
 
#Clae2
clae2['codigo'] = claedict['clae2']
clae2['descripcion'] = claedict['clae2_desc']
clae2['letra'] = claedict['letra']

#Eliminamos tuplas duplicadas
clae2 = sql^("SELECT DISTINCT * FROM clae2")

#Letra
Letra = sql^("SELECT DISTINCT letra FROM clae2")

#establecimientos productivos
est_productivos['id'] = stablmnt['ID']
est_productivos['porcentaje_mujeres'] = stablmnt['proporcion_mujeres']
est_productivos['id_depto'] = stablmnt['in_departamentos']
est_productivos['cod_clae2'] = stablmnt['clae2']
est_productivos = sql^("SELECT DISTINCT * FROM est_productivos")

#Departamento
depto['id'] =  localidades['codigo_indec_departamento']
depto['nombre'] = localidades['nombre_departamento']
depto['id_provincia'] = localidades['codigo_indec_provincia']
depto = sql^("SELECT DISTINCT * FROM depto UNION SELECT DISTINCT * FROM departamentosTierraDelFuego")
depto = depto.drop_duplicates()

consultaIdDepto = """
                        SELECT id, nombre
                        FROM depto
                        INNER JOIN oper_org_cop
                        ON UPPER(depto.nombre) = UPPER(oper_org_cop.departamento)
                        """
idnombre_oper = sql^consultaIdDepto

#Operadores Organicos
op_organicos['razon_social'] = oper_org_cop['razón social']
op_organicos['establecimiento'] = oper_org_cop['establecimiento']
op_organicos['id_depto']= idnombre_oper['id']
op_organicos['nombre_rubro']= oper_org_cop['rubro']

#Provincia
provincia['id'] = sql^("SELECT DISTINCT codigo_indec_provincia FROM localidades")
provincia['nombre'] = sql^("SELECT DISTINCT nombre_provincia FROM localidades")
provincia = sql^("SELECT DISTINCT * FROM provincia")

#Op_organico_produce
op_organico_produce['razon_social'] = oper_org_cop['razón social']
op_organico_produce['establecimiento'] = oper_org_cop['establecimiento']
op_organico_produce['producto'] = oper_org_cop['productos']
op_organico_produce['producto'] = op_organico_produce['producto'].str.split(',')
op_organico_produce = op_organico_produce.explode('producto')

op_organico_produce = sql^("SELECT DISTINCT * FROM op_organico_produce")

#Producto
producto['nombre'] = sql^("SELECT DISTINCT producto FROM op_organico_produce")


 # =============================================================================
 # Reportes y consultas SQL
 # =============================================================================
 
 
 
 # =============================================================================
 # Consulta productos en mas provincias
 # =============================================================================

 consultaProductosProvincia = """
                             SELECT DISTINCT p.producto, o.id_depto
                             FROM op_organico_produce as p
                             INNER JOIN op_organicos as o
                             ON o.razon_social = p.razon_social AND o.establecimiento = p.establecimiento
                             """
productprov1 = sql^consultaProductosProvincia

consultaProductosProvincia2 ="""
                             SELECT p.producto, d.id_provincia
                             FROM productprov1 as p
                             INNER JOIN depto as d
                             ON p.id_depto = d.id
                             """
productprov2 = sql^consultaProductosProvincia2

consultaProductosProvincia3 = """
                             SELECT DISTINCT p.producto, d.nombre as provincia
                             FROM productprov2 as p
                             INNER JOIN provincia as d
                             ON p.id_provincia = d.id
                             """
productprov3 = sql^consultaProductosProvincia3
resultado =sql^("""
            SELECT producto, provincia
            FROM productprov3
            ORDER BY 
              (SELECT COUNT(producto) 
              FROM productprov3 AS sub 
              WHERE sub.producto = productprov3.producto) DESC, producto, provincia
            """)


# =============================================================================
# Consulta Clae mas comun
# =============================================================================

claemascomun= sql^("""
                   SELECT tabla1.codigo, c.descripcion, tabla1.cantidad_de_apariciones
                    FROM
                    (SELECT DISTINCT cod_clae2 as codigo, COUNT(cod_clae2) AS cantidad_de_apariciones
                    FROM est_productivos
                    GROUP BY cod_clae2
                    ORDER BY cantidad_de_apariciones DESC) as tabla1
                    INNER JOIN clae2 AS c
                    ON tabla1.codigo = c.codigo
                """)

# =============================================================================
# Consulta producto más producido
# =============================================================================

#Seleccionamos la cantidad de producciones de cada producto
consulta1_prod = sql^("""
                 SELECT producto, COUNT(*) AS producciones
                 FROM op_organico_produce
                 GROUP BY producto
                 ORDER BY producciones DESC;
                 """)

consulta2_prod = sql^("""
                      SELECT p.producto, p.producciones, o.razon_social, o.establecimiento
                      FROM consulta1_prod AS p
                      INNER JOIN op_organico_produce AS o
                      ON p.producto=o.producto
                      ORDER BY producciones DESC;
                      """)

consulta3_prod = sql^("""
                      SELECT p.producto, p.producciones, p.razon_social, p.establecimiento, o.id_depto, 
                      FROM consulta2_prod AS p
                      INNER JOIN op_organicos AS o
                      ON p.razon_social=o.razon_social AND p.establecimiento=o.establecimiento
                      ORDER BY producciones DESC;
                      """)

consulta4_prod = sql^("""
                      SELECT p.producto, p.producciones, p.id_depto, d.nombre AS departamento, d.id_provincia
                      FROM consulta3_prod AS p
                      INNER JOIN depto AS d
                      ON p.id_depto=d.id 
                      ORDER BY producciones DESC;
                      """)

consulta5_prod = sql^("""
                      SELECT DISTINCT p.producto, p.producciones, p.departamento, p.id_provincia, pro.nombre AS provincia
                      FROM consulta4_prod AS p
                      INNER JOIN provincia AS pro
                      ON p.id_provincia=pro.id 
                      ORDER BY producciones DESC;
                      """)

consulta_max_producciones = sql^("""
                                 SELECT MAX(producciones) AS max
                                 FROM consulta5_prod;
                                 """)

consulta_final_prod = sql^("""
                    SELECT DISTINCT c.producto, m.max AS producciones, c.provincia, c.departamento
                    FROM consulta5_prod AS c
                    INNER JOIN consulta_max_producciones as m
                    ON c.producciones = m.max
                    ORDER BY provincia, departamento DESC;
                    """)

# =============================================================================
# Consulta departamentos sin operadores orgánicos
# =============================================================================

#Listado de departamentos sin Operadores Organicos
consulta_depto_sinOP = sql^ ("""SELECT nombre, 
FROM  depto
WHERE id NOT IN (SELECT DISTINCT id_depto FROM op_organicos)   
""")

#Cantidad de departamentos sin operadores organicos
cantidad = sql^(""" SELECT COUNT(*),
FROM consulta_depto_sinOP""")

# =============================================================================
# Consulta tasa promedio de participación de mujeres
# =============================================================================

tasa_promedio_mujeres_provincia = sql^("""
                                       SELECT AVG(e.porcentaje_mujeres) as tasa_mujeres, p.nombre as provincia
                                        FROM
                                            (SELECT e.id, e.porcentaje_mujeres, d.id_provincia
                                            FROM est_productivos as e
                                            INNER JOIN depto as d
                                            ON e.id_depto = d.id) as e
                                        INNER JOIN provincia as p
                                        ON e.id_provincia = p.id
                                        GROUP BY provincia
                                        ORDER BY provincia
                                       """)
#Calculamos el promedio a nivel nacional
promedio_nacional = sql^("SELECT AVG(tasa_mujeres) AS promedio_nacional FROM tasa_promedio_mujeres_provincia")

#Tabla comparativa
tasa_mujeres_provincia_contra_nacional = sql^("""
                                            SELECT provincia, tasa_mujeres,
                                            CASE WHEN tasa_mujeres > 0.3346911181
                                            THEN true
                                            ELSE false
                                            END AS mayor_a_promedio_nacional 
                                            FROM tasa_promedio_mujeres_provincia
 
                                            """)

#Calculamos el desvio de los promedios de todas las provincias
def desvio(df):
    res = 0
    for i in range(0, len(df['provincia'])):
         res += (df['tasa_mujeres'][i] - promedio_nacional)**2
    return np.sqrt(res/len(df['provincia']))

desvio_promedio_mujeres_provincial = desvio(tasa_promedio_mujeres_provincia)

# =============================================================================
# Consulta cantidad de establecimientos productivos y emprendimientos orgánicos por provincia-departamento
# =============================================================================

est_productivos_por_departamento = sql^("""SELECT d.nombre AS nombre_depto,d.id AS id_depto, d.id_provincia AS id_provincia, COUNT(*) AS cant_est_productivos
FROM est_productivos AS e
INNER JOIN depto AS d
ON e.id_depto=d.id
GROUP BY d.nombre, d.id_provincia, d.id
ORDER BY d.nombre
""")

op_organicos_por_departamento = sql^("""SELECT d.nombre AS nombre_depto,d.id AS id_depto, d.id_provincia AS id_provincia, COUNT(*) AS cant_op_organicos
FROM op_organicos AS o
INNER JOIN depto AS d
ON o.id_depto=d.id
GROUP BY d.nombre, d.id_provincia, d.id
ORDER BY d.nombre
""")

##ahora junto todo en una tabla
op_y_est_productivos = sql^("""SELECT e.nombre_depto, e.id_depto, e.id_provincia, o.cant_op_organicos, e.cant_est_productivos
FROM est_productivos_por_departamento AS e
INNER JOIN op_organicos_por_departamento AS o
ON e.id_depto = o.id_depto
""")

# =============================================================================
# Visualización
# =============================================================================


# =============================================================================
# Histograma de cantidad de establecimiento productivos por provincia
# =============================================================================


est_productivos_por_provincia = sql^("""SELECT p.nombre AS nombre_provincia, COUNT(*) AS cant_est_productivos
FROM est_productivos AS e
INNER JOIN depto AS d
ON e.id_depto=d.id
INNER JOIN provincia AS p
ON d.id_provincia=p.id
GROUP BY p.nombre
ORDER BY p.nombre
""")

#Grafico
sns.barplot(data = est_productivos_por_provincia, x = 'nombre_provincia' , y = 'cant_est_productivos').set(xlabel = 'provincia' , ylabel='cantidad de establecimientos productivos')
plt.xticks(rotation=90)
plt.title('Cantidad de establecimientos productivos por provincia')


# =============================================================================
# Boxplot, cantidad de productos por operador en cada provincia
# =============================================================================

cant_productos_por_operador_por_provincia = sql^("""SELECT o.razon_social, o.establecimiento, COUNT(producto) AS cant_productos, p.nombre AS nombre_provincia
FROM op_organico_produce as o
INNER JOIN op_organicos AS oo
ON o.razon_social = oo.razon_social AND o.establecimiento = oo.establecimiento
INNER JOIN depto AS d
ON oo.id_depto = d.id
INNER JOIN provincia AS p 
ON d.id_provincia = p.id
GROUP BY o.razon_social, o.establecimiento, p.nombre
""")

#Grafico
sns.boxplot(x = 'nombre_provincia', y = 'cant_productos', whis=(0, 100),data = cant_productos_por_operador_por_provincia).set(xlabel = 'provincia', ylabel='cantidad de productos')
plt.title('cantidad de productos por operador en cada provincia')
plt.xticks(rotation=90)

# =============================================================================
#  Scatterplot relación entre cantidad de establecimientos de operadores orgánicos certificados de cada provincia y la proporción de mujeres empleadas en establecimientos productivos de dicha provincia.
# =============================================================================
#Creamos nuestra tabla de equivalencia entre Letra de Clae2 y rubro
consulta1_tabequiv = sql^("""
                 SELECT c.codigo, c.letra
                 FROM clae2 AS c
                 INNER JOIN Letra AS l
                 ON c.letra = l.letra
                 ORDER BY c.codigo, c.letra;
                 """)

tabequiv = sql^("""
                         SELECT c.letra, r.rubro
                         FROM consulta1_tabequiv as c
                         INNER JOIN rubro_clae2 AS r
                         ON c.codigo = r.clae2
                         ORDER BY c.codigo, c.letra; 
                         """)

#Promedio de porcentaje de mujeres empleadas por establecimientos productivos por provincia
consulta1_prom_muj_prov = sql^("""
                        SELECT d.id_provincia, e.porcentaje_mujeres, e.cod_clae2
                        FROM est_productivos AS e
                        INNER JOIN depto AS d
                        ON d.id = e.id_depto
                       """)
consulta2_prom_muj_prov = sql^("""
                        SELECT cl.letra, c.id_provincia, c.porcentaje_mujeres
                        FROM consulta1_prom_muj_prov AS c
                        INNER JOIN clae2 as cl
                        ON c.cod_clae2 = cl.codigo
                        """)

consulta3_prom_muj_prov = sql^("""
                        SELECT p.nombre, p.id, c.porcentaje_mujeres, c.letra 
                        FROM consulta2_prom_muj_prov AS c
                        INNER JOIN provincia as p
                        ON p.id = c.id_provincia
                        """)
promedio_mujeres_provincia = sql^("""
                                SELECT p.nombre as provincia, p.id, c.letra, AVG(c.porcentaje_mujeres) as promedio_porcentaje_mujeres
                                FROM  consulta3_prom_muj_prov as c
                                INNER JOIN provincia as p 
                                ON p.id = c.id
                                GROUP BY p.nombre, p.id, c.letra
                       """)

#Cantidad de operadores organicos por provincia

consulta1_op_org_prov = sql^("""
                        SELECT o.razon_social, o.establecimiento, o.nombre_rubro AS rubro, d.id_provincia
                        FROM op_organicos AS o
                        INNER JOIN depto AS d
                        ON d.id = o.id_depto
                       """)
consulta2_op_org_prov = sql^("""
                        SELECT p.nombre, p.id, c.razon_social, c.establecimiento, c.rubro
                        FROM consulta1_op_org_prov AS c
                        INNER JOIN provincia as p
                        ON p.id = c.id_provincia
                        """)
consulta3_op_org_prov = sql^("""
                            SELECT c.nombre as provincia, c.id, c.rubro, COUNT(*) as cantidad_operadores_organicos
                            FROM consulta2_op_org_prov as c
                            GROUP BY c.nombre, c.id, c.rubro
                            """)
op_organicos_provincia = sql^("""
                            SELECT c.provincia, c.id, t.letra , SUM(c.cantidad_operadores_organicos) AS cantidad_operadores_organicos
                            FROM consulta3_op_org_prov as c
                            INNER JOIN tabequiv as t
                            ON c.rubro = t.rubro
                            GROUP BY c.provincia, c.id, t.letra
                            """)

#Unimos las dos tablas anteriores a través de la letra del Clae2 
tabla_final = sql^("""
                SELECT opp.provincia, opp.cantidad_operadores_organicos, pmp.promedio_porcentaje_mujeres AS porcentaje_mujeres
                FROM op_organicos_provincia AS opp
                INNER JOIN promedio_mujeres_provincia AS pmp
                ON opp.id = pmp.id AND opp.letra = pmp.letra
                 """)

#Graficamos
sns.scatterplot(data = tabla_final ,  x = 'porcentaje_mujeres', y = 'cantidad_operadores_organicos', hue='provincia').set(ylabel='Cantidad de operadores orgánicos', xlabel= 'proporción de mujeres empleadas')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('cantidad de establecimientos de operadores orgánicos de cada provincia \n VS la proporción de mujeres empleadas en establecimientos \n productivos de dicha provincia.')
plt.show()
plt.close()

# =============================================================================
#  Violin plot Distribución de los datos correspondientes a la proporción de mujeres empleadas en establecimientos productivos en Argentina
# =============================================================================
#Utilizaremos la tabla anterior de promedio_mujeres_provincia para armar el gráfico
sns.violinplot(data = promedio_mujeres_provincia ,
               x = 'provincia' , y = 'promedio_porcentaje_mujeres' )
plt.xticks(rotation=90)
plt.title('Distribución de la proporción de mujeres empleadas en establecimientos productivos en Argentina')
plt.show()
plt.close()

# =============================================================================
#  Gráficos de conclusiones
# =============================================================================
#Utilizaremos la tabla_final anterior para realizar una regresion lineal  y buscar una relación entre ambas variables
sns.lmplot(data=tabla_final, x='porcentaje_mujeres', y='cantidad_operadores_organicos').set(title = 'regresion lineal Desarrollo de la actividad orgánica \n vs la proporción de mujeres empleadas en establecimientos productivos \n de las provincias')
plt.show()
plt.close()

#Ahora veremos si hay una relación si miramos los datos por departamento en vez de provincia
df_4 = sql^("""
            SELECT AVG(e.porcentaje_mujeres) as promedio_porcentaje_mujeres, e.nombre as depto, e.id, c.letra
            FROM
                (SELECT d.id,d.nombre, e.porcentaje_mujeres, e.cod_clae2 as clae2
                FROM est_productivos as e
                INNER JOIN depto as d
                ON e.id_depto = d.id) as e
            INNER JOIN clae2 as c
            ON c.codigo = e.clae2
            GROUP BY depto, e.id, c.letra
            ORDER BY depto
            """)

consulta1_op_org_dep = sql^("""
                        SELECT o.razon_social, o.establecimiento, o.nombre_rubro AS rubro, d.id, d.nombre
                        FROM op_organicos AS o
                        INNER JOIN depto AS d
                        ON d.id = o.id_depto
                       """)

consulta3_op_org_dep = sql^("""
                            SELECT c.nombre as departamento, c.id, c.rubro, COUNT(*) as cantidad_operadores_organicos
                            FROM consulta1_op_org_dep as c
                            GROUP BY c.nombre, c.id, c.rubro
                            """)
op_organicos_depto = sql^("""
                            SELECT c.departamento, c.id, t.letra , SUM(c.cantidad_operadores_organicos) AS cantidad_operadores_organicos
                            FROM consulta3_op_org_dep as c
                            INNER JOIN tabequiv as t
                            ON c.rubro = t.rubro
                            GROUP BY c.departamento, c.id, t.letra
                            """)

#Promedio de porcentaje de mujeres empleadas por establecimientos productivos por departamento
consulta1_prom_muj_dep = sql^("""
                        SELECT d.id, d.nombre, e.porcentaje_mujeres, e.cod_clae2
                        FROM est_productivos AS e
                        INNER JOIN depto AS d
                        ON d.id = e.id_depto
                       """)
consulta2_prom_muj_dep = sql^("""
                        SELECT c.nombre, cl.letra, c.id, c.porcentaje_mujeres
                        FROM consulta1_prom_muj_dep AS c
                        INNER JOIN clae2 as cl
                        ON c.cod_clae2 = cl.codigo
                        """)

promedio_mujeres_depto = sql^("""
                                SELECT nombre as departamento, id, letra, AVG(porcentaje_mujeres) as promedio_porcentaje_mujeres
                                FROM  consulta2_prom_muj_dep
                                
                                GROUP BY nombre, id, letra
                      """)
                      
tabla_final_depto = sql^("""
                SELECT opp.departamento, opp.cantidad_operadores_organicos, pmp.promedio_porcentaje_mujeres AS porcentaje_mujeres
                FROM op_organicos_depto AS opp
                INNER JOIN df_4 AS pmp
                ON opp.id = pmp.id AND opp.letra = pmp.letra
                 """)

#Grafico
sns.lmplot(data=tabla_final_depto, x='porcentaje_mujeres', y='cantidad_operadores_organicos').set(title = 'regresion lineal Desarrollo de la actividad orgánica \n vs la proporción de mujeres empleadas en establecimientos productivos \n de los departamentos')
plt.show()
plt.close()


#Promedio de porcentaje de empleadas mujeres vs relacion operador_organico/establecimientos_productivos
consulta_est_prov = sql^("""
SELECT DISTINCT count(*) as cantidad_establecimientos, d.id_provincia
FROM est_productivos
INNER JOIN depto as d
ON est_productivos.id_depto = d.id
GROUP BY d.id_provincia
""")

establecimientos_provincia = sql^("""	
SELECT c.cantidad_establecimientos, p.nombre as provincia
FROM consulta_est_prov as c
INNER JOIN provincia as p
ON c.id_provincia = p.id
""")

tabla_relacion = sql^("""
SELECT p.cantidad_operadores_organicos/e.cantidad_establecimientos as relacion_operadores_establecimientos, p.provincia, p.porcentaje_mujeres
FROM establecimientos_provincia as e
INNER JOIN tabla_final as p
ON e.provincia = p.provincia
""")

#Grafico
sns.lmplot(data=tabla_relacion, y='porcentaje_mujeres', x='relacion_operadores_establecimientos').set(title = 'regresion lineal Desarrollo de la actividad orgánica \n en relacion a los establecimientos productivos \n vs la relacion operadores_organicos vs total de establecimientos')
plt.xlabel('relación operadores organicos/establecimientos productivos')
plt.ylabel('Tasa de mujeres')
plt.show()
plt.close()

