import pickle
from pyDes import *
psswd = pickle.load( open("contra.p", "rb"))
def readpsswd():
    wnted = input("¿Qué contraseña buscas?\n")
    cifrado = input("\n¿Cuál es la clave de cifrado?\n")
    wntedpsswd = triple_des(cifrado).decrypt(psswd[wnted], padmode=2)
    print("\nLa contraseñla de "+ wnted +" es "+wntedpsswd.decode("utf-8"))
    input("\nPulsa enter")
def writepsswd():
    wnted = input("¿Qué contraseña quieres añadir o cambiar?\n")
    password = input("\n¿Cuál es la contraseña?\n")
    cifrado = input("\n¿Cuál es la clave de cifrado?\n")
    psswd[wnted] = triple_des(cifrado).encrypt(password, padmode = 2)
    print("\nContraseña añadida/actualizada")
    input("\nPulsa enter")
def guardar():
    pickle.dump(psswd, open("contra.p", "wb"))
    print("\nSe han guardado los cambios")
    input("\nPulsa enter")
while True:
    opc = input("\n¿Qué quieres hacer?\nR: buscar una contraseña.\nW: crear o editar una contraseña.\nS: guardar los cambios realizados\n")
    if opc == "R" or opc == "r":
        readpsswd()
    elif opc == "W" or opc == "w":
        writepsswd()
    elif opc == "S" or opc == "s":
        guardar()