# Funciones: argumentos por omisión (funciones que pueden ser llamadas con menos argumentos)
def confirmar(indicador, intentos = 4, queja = 'sí o no'):
    while 1:
        respuesta = input(indicador)
        if respuesta in ('s', 'si', 'sí'):
            return 1
        elif respuesta in ('n', 'no'):
            intentos = intentos - 1
        if intentos < 0:
            raise(IOError, 'Usuario rechazado')
        print(queja)

confirmar('todo ok')
confirmar('desea continuar?', 2)



