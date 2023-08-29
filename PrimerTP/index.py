

horasTrabajadas = int(input('Ingrese cantidad de horas trabajadas: '))
sueldoBruto = 9576 * horasTrabajadas

descuentoJubilacion = int((sueldoBruto * 11.5) / 100)
print(f"El descuento a aplicar debido a Aportes Jubilatorios es de {descuentoJubilacion} pesos")

descuentoOS = int((sueldoBruto * 4.5) / 100)
print(f"El descuento a aplicar debido a Aportes a la Obra Social es de {descuentoOS} pesos")

impuestoGanancias = 0

if 700000 < sueldoBruto < 800000:
    impuestoGanancias = int((sueldoBruto * 6) / 100)
    print(f"El descuento a aplicar debido a Impuestos a las Ganancias es de {impuestoGanancias} pesos")
else:
    if sueldoBruto >= 800000:
        impuestoGanancias = int((sueldoBruto * 10) / 100)
        print(f"El descuento a aplicar debido a Impuesto a las Ganancias es de {impuestoGanancias} pesos")

sueldoNeto = sueldoBruto - descuentoJubilacion - descuentoOS - impuestoGanancias
print(f"Su sueldo neto es de {sueldoNeto} pesos")
