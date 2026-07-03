from data_manager import leer_json, guardar_json
from auditoria import registrar_auditoria


RUTA_PRESUPUESTOS = "data/presupuestos.json"
RUTA_GASTOS = "data/gastos.json"


def crear_presupuesto(usuario_actual):
    print("\n===== CREAR PRESUPUESTO =====")

    categoria = input("Categoria del presupuesto: ")
    mes = input("Mes del presupuesto: ")

    try:
        monto = float(input("Monto presupuestado: Q"))
    except ValueError:
        print("El monto debe ser numerico.")
        return False

    if categoria == "" or mes == "" or monto <= 0:
        print("Categoria, mes y monto valido son obligatorios.")
        return False

    presupuestos = leer_json(RUTA_PRESUPUESTOS)

    presupuesto = {
        "categoria": categoria,
        "mes": mes,
        "monto": monto,
        "creado_por": usuario_actual["usuario"]
    }

    presupuestos.append(presupuesto)
    guardar_json(RUTA_PRESUPUESTOS, presupuestos)

    registrar_auditoria(
        usuario_actual,
        "Creacion de presupuesto",
        "Se creo presupuesto de Q" + str(monto) + " para " + categoria + "."
    )

    print("Presupuesto creado correctamente.")
    return True


def listar_presupuestos():
    presupuestos = leer_json(RUTA_PRESUPUESTOS)

    print("\n===== PRESUPUESTOS =====")

    if len(presupuestos) == 0:
        print("No hay presupuestos registrados.")
        return

    contador = 1

    for presupuesto in presupuestos:
        print("--------------------------------")
        print(contador, ".", presupuesto["categoria"])
        print("Mes:", presupuesto["mes"])
        print("Monto: Q", presupuesto["monto"])
        print("Creado por:", presupuesto["creado_por"])
        contador = contador + 1


def gasto_real_por_categoria(categoria):
    gastos = leer_json(RUTA_GASTOS)
    total = 0

    for gasto in gastos:
        if gasto["categoria"].lower() == categoria.lower():
            total = total + gasto["monto"]

    return total


def comparar_presupuestos():
    presupuestos = leer_json(RUTA_PRESUPUESTOS)

    print("\n===== PRESUPUESTO VS REALIDAD =====")

    if len(presupuestos) == 0:
        print("No hay presupuestos registrados.")
        return

    for presupuesto in presupuestos:
        gasto_real = gasto_real_por_categoria(presupuesto["categoria"])
        diferencia = presupuesto["monto"] - gasto_real

        print("--------------------------------")
        print("Categoria:", presupuesto["categoria"])
        print("Mes:", presupuesto["mes"])
        print("Presupuesto: Q", presupuesto["monto"])
        print("Gasto real: Q", gasto_real)
        print("Diferencia: Q", diferencia)

        if diferencia < 0:
            print("Alerta: se supero el presupuesto.")
        elif diferencia == 0:
            print("Estado: presupuesto utilizado exactamente.")
        else:
            print("Estado: dentro del presupuesto.")


def menu_presupuestos(usuario_actual):
    while True:
        print("\n===== MODULO DE PRESUPUESTOS =====")
        print("1. Crear presupuesto")
        print("2. Listar presupuestos")
        print("3. Comparar presupuesto vs realidad")
        print("0. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            crear_presupuesto(usuario_actual)
        elif opcion == "2":
            listar_presupuestos()
        elif opcion == "3":
            comparar_presupuestos()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida.")