
def main():
    An = float(input("Ingrese la altitud inicial:"))
    As = float(input("ingrese la altitud de seguridad:"))
    K = float(input("Ingrese el coeficiente de arrastre:"))
    d = An
    z = K
    orbita = 1
    while d > As:
        p = K * d
        d = d - p
        z += 0.0001
        orbita += 1
        if d > As:
            print(f"en la orbita {orbita}, se tuvo una altitud de {d} y un coeficiente de arrastre de {z} ")
        if p < 0.000001:
            d = 0
            print(f"El satelite se ha estabilizado despues de {orbita} orbitas")
        elif d < As:
            print(f"El satelite se ha desintegrado en la atmosfera despues de {orbita} orbitas")
            opcion = input("le gustaria conocer la altitud en la que el satelite se desintegro? :")
            opcion = opcion.upper()
            if opcion not in ["SI", "NO"]:
                print("opcion no valida ._.")
            elif opcion == "SI":
                print(f"el satelie se desintegro a una altitud de {d}")
            else:
            
                pass 


if __name__ == "__main__":
    main()
