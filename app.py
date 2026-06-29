from src.register_faces import register_faces
from src.train_model import train_model
from src.attendance import run_attendance


def main():
    while True:
        print("\nSistema de asistencia con reconocimiento facial")
        print("1. Registrar rostros")
        print("2. Entrenar modelo")
        print("3. Iniciar asistencia")
        print("4. Salir")

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            name = input("Ingresa el nombre de la persona: ").strip()
            if name:
                register_faces(name)
            else:
                print("El nombre no puede estar vacío.")
        elif option == "2":
            train_model()
        elif option == "3":
            run_attendance()
        elif option == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
