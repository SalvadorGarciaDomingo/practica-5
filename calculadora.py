#diferestes funciones de la calculadora
def suma(a: int, b: int):
    suma = a+b
    return suma

def resta(a: int, b: int):
    resta=a-b
    return resta

def multiplicacion(a: int, b: int):
    multi=a*b
    return multi

def division(a: int, b: int):
    if b==0:
        return {"message": "No se puede dividir entre 0"}
    else:
        division=a/b
        return division
    

if __name__ == "__main__":
 print(suma(5, 3))
 print(resta(3, 2))
 print(multiplicacion(3, 2))
 print(division(4, 2), 2)
