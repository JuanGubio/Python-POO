def mi_decorador(func):
    def wrapper():
        print("Algo se hará antes de la función")
        func()
        print("Algo se hará después de la función")
    return wrapper

@mi_decorador
def mi_funcion():
    print("Esta es la función original")

mi_funcion()
