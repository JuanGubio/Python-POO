class Circulo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        if radio >= 0:
            self._radio = radio
        else:
            raise ValueError("El radio no puede ser negativo")

circulo = Circulo(5)
print(circulo.radio)  # 5
circulo.radio = 10
print(circulo.radio)  # 10
