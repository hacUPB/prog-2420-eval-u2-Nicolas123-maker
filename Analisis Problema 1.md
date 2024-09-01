# Sistema de reserva de vuelos.
### Procedimiento para el análisis:
Para comprender mejor el problema planteado y hacer mas visible su solución, he definido las variables y constantes que interactúan en el problema y posterior a esto he hecho un escrito con mis palabras explicando lo que el problema plantea, añadiendo notas en perentesis que considero pertinentes a la hora de escribir el código de la solución.

## Definición de variables:
- Título del usuario (sr. o sra.).
- Nombre del usuario.
- Apellido del usurio.
- Origen y destino.
- Día de la semana y día del mes.
- Precio del tiquete.
- Preferencia de asiento.

## Definición de constantes:
- Distancia entre ciudades.
- Precios segun el día y la distancia.
- Número aleatorio entre el rango definido.
- Nombre de la aerolinea.

## Escrito del problema:
Como punto de partida, el sistema debe pedirle al usuario su genero o título, su nombre y apellido. Despues de esto generara un saludo personalizado con la siguiente estructura: 
- Mensaje predeterminado + Título-genero + nombre + apellido.

Despues de mostrar lo anterior, procederá a preguntarle al usuario desde que ciudad desea viajar y cuál será su destino; luego le preguntará la fecha del viaje de la siguiente forma:
- En que día de la semana viajará: ...
- En que día viajará: ...
- En que mes viajará: ...

Dependiendo de la distancia entre ciudades y el día y mes de viaje, el tiquete tomará un valo definido.
Por ultimo se le preguntará al usuario por su preferencia de asiento (Pasillo, ventana, sin preferencia) y luego se formara un numero aleatorio (que indica el numero del asiento) en un rango definido.
Como salida final del sistema, se le mostrará al usuario lo siguiente:
- Tu vuelo desde (ciudad origen) hacia (ciudad destino) el (día de la semana) del (día) de (mes) con precio de tiquete (precio tiquete), quedo reservado en el asiento (Preferencia + numero aleatorio)

### Definición de letras y palabras usadas en el pseudocódigo:
- c = Nombre de la aerolinea
- título = sr. o sra
- origen = ciudad de origen
- destino = ciudad destino
- d = distancia entre ciudades
- día_s = día de la semana
- a = Dias de la semana de lunes a jueves
- b = Dias de la semana de viernes a domingo
- p = Precio del tiquete
- z = Numero de asiento
- preferencia_usuario = preferencia de asiento del usuario
## Pseudocódigo:
```
Inicio
c = "la arepa que vuela"
Leer título
Leer nombre
leer apellido
imprimir "Bienvenido a {c}, {titulo}{nombre}{apellido}"
Leer origen
Leer destino
si origen = destino :
  imprimir "Seleciona un destino diferente a tu ciudad de origen"
sino 
    si origen =M and destino = B :
      d = 240
    sino
      si origen = M and destino = C :
        d = 461
      sino
        si origen = B and destino = C :
          d = 657
        fin si
      fin si
    fin si 
fin si
Leer día_s
Leer día 
Leer mes
a = [lunes, martes, miercoles, jueves]
b = [viernes, sabado, domingo]
si d < 400 and día_s not in a :
  P = $ 119,990
sino
  si d < 400 and día_s not in b :
    P = $79,990
  sino
    si d > 400 and día_s not in a :
      P = $214,000
    sino
      si d > 400 and día_s not in b :
        P = $160,000
      fin si
    fin si
  fin si
fin si
Leer preferencia_usuario
z = random.randint(1,32)
imprimir " Tu vuelo desde {origen} hacia {destino} el {díá_s}, {día} de {mes}, con precio de tiquete {P}, quedo reservado en el asiento {z}{preferencia usuario}"
imprimir "Gracias por volar en {c}"
Fin
```
