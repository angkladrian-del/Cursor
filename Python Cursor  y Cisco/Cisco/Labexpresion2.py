#Operadores reloj
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.


Tt_mins = mins + dura

ex_hors = Tt_mins//60

mins = Tt_mins % 60

hour = (hour + ex_hors)%24

print("Hora ", hour,":",mins, sep="")
