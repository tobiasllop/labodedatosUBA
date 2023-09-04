## Clase 6 Laboratorio de datos
#### Actividad mapeo de DER
![imagen del der](/../../../../github/labodedatosUBA/main/Clase%206/der.jpg)
Las variables en **negrita** son las claves de las entidades y relaciones.
##### Entidades Fuertes
* Producto(**Codigo**, Descripcion, Tamaño)
* Cliente(Nombre, Apellido, **CUIL**, Email, Codigo Postal, Fecha Nacimiento)
* Factura(**Número**, Fecha, Importe)
* Departamento(**Nombre**, Email)
* Empleado(Nombre, apellido, Salario, **CUIL**, Email)

##### Relaciones 
* Solicita(**Código.producto**, CUIL.cliente, **Número.factura**)
  
  *Este ejercicio estuvo en discusión aparentemente esta mal diseñado.*
  
* Pertenece_a = Empleado(Nombre, Apellido, **CUIL**, Email, Codigo Postal, Fecha Nacimiento, Nombre_dpto)
  
  Nombre_dpto -> Departamento -> Nombre
  
* Es_supervisor_de(CUIL.supervisor, **CUIL.supervisado**)
  
  Cuil.supervisor -> Empleado -> CUIL
  
  Cuil.supervisado -> Empleado -> CUIL
   
* Es_realizado_por(**Cuil_emp**, **código_prod**)
 
  Cuil_emp -> Empleado -> CUIL
  
  Código_prod -> Producto -> Código
