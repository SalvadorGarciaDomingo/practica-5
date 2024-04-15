
from fastapi import FastAPI

#instancia de FastApi
app=FastAPI()


#primer endpoint dirigido a la pagina principal de la api
@app.get("/")
def read_root():
    return{"message": "Bienvenidos a mi API"}

#endpoint suma
@app.get("/suma/{a},{b}")
def suma(a: int, b: int):
    suma = a+b
    return suma

#endpoint resta
@app.get("/resta/{a},{b}")
def resta(a: int, b: int):
    resta=a-b
    return resta

#endpoint multiplicacion
@app.get("/multiplicacion/{a},{b}")
def multiplicacion(a: int, b: int):
    multi=a*b
    return multi

#endpoint division
@app.get("/division/{a},{b}")
def division(a: int, b: int):
    if b==0:
        return {"message": "No se puede dividir entre 0"}
    else:
        division=a/b
        return division
    

if __name__ == "__main__":
 print(suma(5, 3))