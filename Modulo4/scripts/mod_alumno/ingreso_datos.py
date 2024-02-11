
def ingreso_numero_decimal(msg= 'Ingrese un número decimal: '):
    """Validar el ingreso de un número decimal """
    try:
        numero = float(input(msg))
        return numero
    except:
        print('Numero invalido, vuelva a ingresar el dato ...')
        return ingreso_numero_decimal(msg)

def ingreso_numero_entero(msg= 'Ingrese un número entero: '):
    """Validar el ingreso de un número entero """
    try:
        numero = int(input(msg))
        return numero
    except:
        print('Numero invalido, vuelva a ingresar el dato ...')
        return ingreso_numero_entero(msg)

