# whereU
## Mile 1 -> RAW IP 

## Mile 2 -> Dedecoding IP Headers
Definimos una clase IP para almacenar los datos del header que recibimos. El primer 'dato' que recibimos es "<" que especifica el orden de los bytes dentro de un número binario,
el byte menos significativo está en la dirección m´s baja y la más signifacante en la alta. Y la siguiente que tenemos son las partes individuales del header.

Del Primer byte que recibimos solo queremos asignar a 'ver' solo el nybble de mayor orden, la forma típica de hacer esto es moviendo a la derecha, que viene 
siendo poner 4 ceros delante del byte y nos deja con el byte más alto.

Queremos asignar a la variable 'ihl' el byte de orden bajo, la forma tipica de realizar esto es con la operación AND con 0xF, y así asiganmos el byte de orden más bajo

A partir de aquí ya tenemos la cabecera decodificada y solo tenemos que asignar cada parte de la cabecera a una variable hacer un poco de limpieza y encontrar una forma de 
mostrar por pantalla de forma legible el protocolo y las direcciones origen/destino y que el codigo se ejecute hasta que el usuario lo pare con cualquier tecla.

Resultado: 

![Decoded Headers](https://github.com/chinijo21/whereU/blob/master/snif%20snif/imgs/decoded%20ip%20header.PNG)
