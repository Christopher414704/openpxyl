import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Gastos"

print("Ingrese los detalles de sus gastos. Deje en blanco para terminar.")
gastos = []

while True:
    fecha = input("Fecha (DD/MM/AAAA): ")
    if not fecha:
        break
    descripcion = input("Descripción: ")
    monto = float(input("Monto: "))
    
    gastos.append((fecha, descripcion, monto))

sheet.append(["Fecha", "Descripción", "Monto"])
for gasto in gastos:
    sheet.append(gasto)

total_gastos = sum(gasto[2] for gasto in gastos)
gasto_mas_caro = max(gastos, key=lambda x: x[2])
gasto_mas_barato = min(gastos, key=lambda x: x[2])

print("\nResumen de gastos:")
print(f"Número total de gastos: {len(gastos)}")
print(f"Gasto más caro: Fecha: {gasto_mas_caro[0]}, Descripción: {gasto_mas_caro[1]}, Monto: {gasto_mas_caro[2]}")
print(f"Gasto más barato: Fecha: {gasto_mas_barato[0]}, Descripción: {gasto_mas_barato[1]}, Monto: {gasto_mas_barato[2]}")
print(f"Monto total de gastos: {total_gastos:.2f}")

workbook.save("informe_gastos.xlsx")

print("El informe de gastos se ha guardado en informe_gastos.xlsx.")
