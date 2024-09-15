from os import system
from random import randint
def main():
  #conjunto de definición de las variables de control
  c ="la arepa que vuela"
  v1_control = "true"
  v2_control = "true"
  #primer while de control
  while v1_control == "true":
      titulo = str(input("Como prefiere que nos refiramos hacia usted? (sr. o sra):"))
      titulo = titulo.capitalize()
      if titulo not in ["Sr", "Sra"]:
        print("Por favor verifique su respuesta")
      else: v1_control = "false"
  system("cls")
  nombre = str(input("Ingrese su nombre:"))
  nombre = nombre.capitalize()
  apellido = str(input("Ingrese su apellido:"))
  apellido = apellido.capitalize()
  system("cls")
  print(f"Bienvenido a {c}, {titulo}. {nombre} {apellido}")
  Ciudades = ["Medellín", "Bogotá", "Cartagena"]
  #Segundo while de control
  while v2_control == "true":
    print(f"Estas son las ciudades donde tenemos nuestras sucursales actuales: {Ciudades}")
    origen = str(input("Desde donde iniciara su viaje? (No use tildes por favor):"))
    origen = origen.lower()
    lista_origen = ["medellin", "bogota", "cartagena"]
    if origen not in lista_origen:
      print("lo sentimos, de momento no tenemos sucursal en tu ciudad")
    else: v2_control = "false"
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
