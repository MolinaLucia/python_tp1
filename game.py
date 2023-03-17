from random import choice, randrange
from datetime import datetime


# Operadores posibles
operators = ["+", "-","*","/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
# Inicializo la cantidad de respuestas correctas e incorrectas
total_correctas = 0
total_incorrectas = 0
for i in range(0, times):
  # Se eligen números y operador al azar
  number_1 = randrange(10)
  number_2 = randrange(10)
  operator = choice(operators)
  # Se imprime la cuenta.
  print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
  # Le pedimos al usuario el resultado
  result = float (input(": "))  
  # Se mostrara si la cuenta es correcta o incorrecta
  # eval() es una funcion que evalua cadena de textos que pueden contener expresiones 
  cuenta = eval(f"{number_1} {operator} {number_2}")  
  if result == cuenta:
    print("El resultado es correcto")
    total_correctas += 1
  else:
    print ("El resultado es incorrecto. El resultado deberia ser ",cuenta)
    total_incorrectas += 1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vera en pantalla la cantidad de cuentas acertadas
print("")
print (">> Aciertos totales: ",total_correctas)
print (">> Desaciertos totales: ",total_incorrectas)
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
