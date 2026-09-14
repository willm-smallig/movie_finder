"""
- Crear un programa con 3 opciones
1. Registrar usuario: Email y contraseña.
2. Verificar credenciales
3. Salir
- El programa debe guardar las credenciales en un fichero .txt
- Al registrar, las credenciales deben de ser validas:
    - Email valido (regex)
    - Contraseña valida:
        - Minimo 8 caracteres.
        - Al menos una mayuscula.
        - Al menos un numero.
        - Al menos un caracter especial.
- Crear una funcion para crear el hash de la contraseña y otra para verificarlo.
"""
import hashlib
import os
import re

REGEX_EMAIL = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
REGEX_PASSWORD = r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,}$"
FILE_NAME = "credenciales.txt"


def validar_email(email):
    return bool(re.match(REGEX_EMAIL, email))


def validar_password(password):
    return bool(re.match(REGEX_PASSWORD, password))


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def registrar_usuario(email: str, hash_pw: str) -> None:
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{email};{hash_pw}\n")


def obtener_credenciales(email: str) -> str | None:
    if not os.path.exists(FILE_NAME):
        return None

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                credenciales = line.split(";")
                if len(credenciales) == 2 and credenciales[0] == email:
                    return credenciales[1]
    return None


def guardar_usuario():
    print("\n--- Registro de usuario ---")
    email = input("Introduce email: ").strip()
    if not validar_email(email):
        print("Error: Email invalido")
        return

    if obtener_credenciales(email) is not None:
        print("Error: El usuario ya existe.")
        return

    password = input("Introduce tu contraseña: ")
    if not validar_password(password):
        print(
            "Error: La contraseña debe tener mín. 8 caracteres, una mayúscula, un número y un símbolo."
        )
        return

    hashed_pw = hash_password(password)
    registrar_usuario(email, hashed_pw)
    print("Usuario registrado correctamente\n")


def verificar_credenciales():
    print("\n--- Verificación de credenciales ---")
    email = input("Introduce tu email: ").strip()
    password = input("Introduce tu contraseña: ").strip()

    hash_guardado = obtener_credenciales(email)
    hash_ingresado = hash_password(password)

    if hash_guardado is not None and hash_guardado == hash_ingresado:
        print("\n Credenciales correctas, adelante...")
        print("--- Credenciales Guardadas ---")
        print(f"Email: {email}")
        print(f"Hash en fichero: {hash_guardado}")
    else:
        print("Error: Credenciales incorrectas o usuario no registrado.")


def mostrar_menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar usuario")
        print("2. Verificar credenciales")
        print("3. Salir")

        opcion = input("Selecciona una opción: (1-3): ").strip()
        if opcion == "1":
            guardar_usuario()
        elif opcion == "2":
            verificar_credenciales()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción incorrecta. Inténtalo de nuevo.")


if __name__ == "__main__":
    mostrar_menu()