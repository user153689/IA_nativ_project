import numpy as np
from keras import Sequential, layers

model = Sequential([
    keras_input := layers.Input(shape=(1,)),
    layers.Dense(units=3),
    layers.Dense(units=64),
    layers.Dense(units=1),
])

entree = np.array([[1], [2], [3], [4], [5]], dtype=np.float32)
sortie = np.array([[2], [4], [6], [8], [10]], dtype=np.float32)

model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(x=entree, y=sortie, epochs=2000)

while True:
    try:
        x = float(input("Entrez un nombre (ou q pour quitter) : "))
        prediction = model.predict(np.array([[x]], dtype=np.float32), verbose=0)
        print("nombre *2 :", prediction[0][0])
    except ValueError:
        print("Au revoir !")
        break