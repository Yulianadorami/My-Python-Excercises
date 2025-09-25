def convertToBase13(num):
    base13_digits = "0123456789ABC"
    if num == 0: 
        return "0"

    negativo = num < 0
    n = abs(num)
    resultado = "" 

    while n>0:
        residuo = n%13
        digito = base13_digits[residuo]
        resultado = digito + resultado
        n //= 13
    if negativo:
        resultado = "-"+resultado
    return resultado

print(convertToBase13(49))