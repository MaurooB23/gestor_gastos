# Gestor de gastos personales
Programa en Python (Pandas) para registrar y analizar gastos personales.
Proyecto final de la Tecnicatura en Desarrollo de Software.

# Campos del Gasto:
- Fecha, Monto, categoria y Descripcion

# Tipo de Dato para cada campo:
- Fecha (date) se guarda como texto en el CSV y se convierte al leerla.
- Monto (float)
- Categoria (String)
- Descripcion (String)

# Categorias:
-  transporte, cuentas y servicios, alquiler, supermercado, entretenimiento(cine, juegos digitales, apps, etc...), otros, salidas y compras(comidas afueras, ropa, etc...)

# Haremos una lista fija de cada categoria

# Validaciones:
-  La Fecha se cargara como AAAA-MM-DD, la idea es que la cargue el usuario para que pueda registar gastos de dias anteriores. Si el ususario carga mal la fecha largar  un cartel de error y que no deje registarar el gasto hasta que coloque bien la fecha
- Que la fecha exista (no vale 2026-02-31).
- Que no sea futura.
- si aprieta Enter sin escribir nada se use la fecha de hoy.
- El Monto Tiene que ser un número (no letras ni vacío). De caso contrario largar  un cartel de error y que no deje registarar el gasto hasta que coloque un numero
- El monto Tiene que ser mayor a 0. De caso contrario largar  un cartel de error y que no deje registarar el gasto hasta que coloque un valor
- La coma la transformamos automaticamente em punto 
- Rechazar valores especiales como nan o inf: Python los acepta como números válidos y te romperían los totales.
- Redondear a 2 decimales.
- pedir confirmación si el monto es muy alto, por si se escribió un cero de más.
- La categoria si o si sera una lista fija
- Cada categoria tendra un numero asignado, por lo cual el usaurio solo debera colocar el numero a la hora de elegir categoria
- Si queda vacia largara  un cartel de error y que no deje registarar el gasto hasta que coloque un numero
- la Descripcion En el caso de que este vacia se guardara como "Sin Descripcion" 
- Quitar espacios sobrantes al principio y al final
- Poner un maxximo de 200 caracteres 
- Si el archivo no existe (primera vez), crearlo con las columnas correctas.
- Si existe pero está vacío o le faltan columnas, avisar en vez de romperse.
- Al leerlo, convertir fecha y monto a sus tipos correctos.
- Guardar con codificación UTF-8 para que las tildes y la ñ no se rompan.
- Si el CSV está abierto en Excel, Windows no deja guardarlo: mostrar un mensaje claro.
- Si el usuario elige una opción que no existe, avisar y volver a mostrar el menú.
- Permitir cancelar una carga sin guardar nada.
- Mostrar un resumen y pedir confirmación antes de guardar.
- avisar si hay un posible duplicado (mismo monto, categoría y día).
