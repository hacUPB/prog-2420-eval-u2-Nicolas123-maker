from os import system
from random import randint
def main():
  c ="la arepa que vuela"
  titulo = str(input("Como prefiere que nos refiramos hacia usted? (sr. o sra):"))
  nombre = str(input("Ingrese su nombre:"))
  apellido = str(input("Ingrese su apellido:"))
  print(f"Bienvenido a {c}, {titulo} {nombre} {apellido}")
  system("cls")
  origen = str(input("Desde donde iniciara su viaje? (No use tildes por favor):"))
  origen = origen.lower()
  lista_origen = ["Medellin, Bogota, cartagena"]
  if origen not in lista_origen:
    print("lo sentimos, de momento no tenemos sucursal en tu ciudad")
  destino = str(input("hacia donde desea viajar?:"))
  destino = destino.lower()
  if origen == destino:
    print("Por favor introduzca un destino diferente a su ciudad de origen.")
  if destino not in lista_origen:
    print("lo sentimos, aun no tenemos ruta para esa ciudad")
  if origen == "medellin" and destino == "bogota" or origen == "bogota" and destino == "medellin":
    if origen == "medellin" and destino =="bogota":
      print("Excelente elección, recuerde llevar abrigo pal' frio")
    else:
      print("Excelente elección, le recomendamos visitar el jardín botanico")
    d = 240
    print(f"entre las ciudades hay una distancia de {d}.")
  elif origen == "medellin" and destino == "cartagena" or origen == "cartagena" and destino == "medellin":
    d = 461
    if origen == "medellin" and destino == "cartagena":
      print("Excelente elección, recuerde llevar bloqueador pal' sol.")
    else:
      print("Excelente elección, le recomendamos visitar el jardín botanico")
      

          
    
          



pass
        

if __name__ == "__main__":
    main()
