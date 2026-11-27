


ARCHIVO_CSV = "gastos.csv"
MONTO_ALTO = 1000000    
MAX_DESCRIPCION = 200


CATEGORIAS = {
    1: "Transporte",
    2: "Cuentas y servicios",
    3: "Alquiler",
    4: "Supermercado",
    5: "Entretenimiento",
    6: "Salidas y compras",
    7: "Otros",
}


def pedir_monto():
    monto = 0
    while monto <= 0:

        try:
            texto_monto = input("Ingrese el monto que gasto: ").strip()
            if texto_monto == "":
                print("Error: Debe ingresar un monto.")
                continue

           
            texto_monto = texto_monto.replace(",", ".")

           
            monto = float(texto_monto)

            if monto < 0:
                print("El monto ingresado no puede ser negativo")

            if monto == 0:
                print("El monto debe ser mayor a 0")

            elif monto >= MONTO_ALTO:
                print(F"El monto no puede superar los {MONTO_ALTO}")
                monto = 0
            else:
               
                monto = round(monto, 2)

        except ValueError:
            print("Error: Debe ingresar un número, no letras.")

    return monto
       
monto_ingresado = pedir_monto()
print(f"El monto ingresado es de ${monto_ingresado:.2f}")



def pedir_categoria():

    for numero, nombre in CATEGORIAS.items():
                print(f"{numero} - {nombre}")

    while True:


        texto_cat = input("Seleccione una categoría: ").strip()

        if texto_cat == "":
            print("Error: La categoría no puede estar vacía")
            continue

        try:
            cat = int(texto_cat)

            if cat not in CATEGORIAS:
                print("Error: La categoría seleccionada no existe")
                continue

            return CATEGORIAS[cat]

        except ValueError:
            print("Error: Debe ingresar un número válido.")


categoria_ingresada = pedir_categoria()

print(f"La categoría seleccionada es: {categoria_ingresada}")
