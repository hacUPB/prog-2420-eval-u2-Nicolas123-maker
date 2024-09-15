# Cálculos de orbitas de un satélite.
### Procedimiento para el analisis:
Para comprender mejor el problema planteado y hacer mas visible su solución, he definido las variables y constantes que interactúan en el problema y posterior a esto he hecho un escrito con mis palabras explicando lo que el problema plantea, añadiendo notas en perentesis que considero pertinentes a la hora de escribir el código de la solución.

## Definición de variables :
- Altitud inicial del satelite.
- Coeficiente de arrastre.
- Altitud minima de seguridad
## Definición de constantes :
- Número que simula el aumento en el coeficiente de arrastre.
### Escrito del problema :
Nos piden calcular y simular la perdida de altitud de un satelite que está orbitando la tierra, teniendoo en cuenta los siguientes datos:
- Altitud inicial
- Altitud de seguridad
- Coeficiente de arrastre (aumentará conforme el satélite pierda altitud)

Haremos esto con unos bucles que simularán las órbitas y nos dirán en que órbita el cohete se estabilizó ó se desintegro en la atmosfera.
Para estos cálculos usaremos las siguientes formúlas:

$$
Altitud perdida =Coeficiente de arrastre *altitud
actual
$$

$$
Altitud de orbita= altitud actual - altitud perdida
$$

## Definición de letras y palabras usadas en el pseudocódigo:
- An = Altitud inicial
- As = Altitud de seguridad
- k = Coeficiente de arrastre
- p = Altitud perdida
- d = Altitud actual
 
## Pseudocódigo
```
Inicio
Leer An
Leer As
Leer k
d = An
Orbita = 1
mientras d > as
  p = k*d
  d = d-p
  k += 0.001
  orbita += 1
  imprimir"en la orbita {orbita}, se tuvo una altitud de {d} y un coeficiente de arrastre de {k}"
  si P < 0,000001
    d = 0
    imprimir"el satelite se ha estabilizado despues de {orbita} orbitas"
  sino
    si d < as
      imprimir "El satelite se ha desintegrado en la atmosfera despues de {orbita} orbitas"
    fin si
  fin si
Fin mientras
Fin
```