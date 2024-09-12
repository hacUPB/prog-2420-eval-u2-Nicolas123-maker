
def main():
    An = float(input("Ingrese la altitud inicial:"))
    As = float(input("ingrese la altitud de seguridad:"))
    K = float(input("Ingrese el coeficiente de arrastre"))
    d = An
    orbita = 1
    while d > As:
        p = K * d
        d = d - p
        k += 0.0001
        orbita += 1
        print(f"en la orbita {orbita}, se tuvouna altitud de {d} y un coeficiente de arrastre de {k} ")
        if p < 0.000001:
            d = 0
            print(f"El satelite se ha estabilizado despues de {orbita} orbitas")
        elif d < As:
            print(f"El satelite se ha desintegrado en la atmosfera despues de {orbita} orbitas")
        else:
            pass # borra esta línea cuando con inicies tu código


if __name__ == "__main__":
    main()
