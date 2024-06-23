import random
import turtle
import matplotlib.pyplot as plt


class SistemaDeGestionDeBiblioteca:
    def __init__(self, lista_de_libros):
        self.lista_de_libros = lista_de_libros
        self.libros_dict = {}
        self.cargar_libros()

    def cargar_libros(self):
        id = 101
        for libro in self.lista_de_libros:
            self.libros_dict[str(id)] = {
                'titulo_libro': libro[0],
                'autor': libro[1],
                'ano': libro[2]
            }
            id += 1

    def mostrar_libros(self):
        def obtener_titulo_libro(item):
            return item[1]['titulo_libro'].lower()

        libros_ordenados = sorted(self.libros_dict.items(), key=obtener_titulo_libro)
        print("------------------------Lista de Libros---------------------")
        print("ID del Libro\tTitulo\t\t\tAutor\t\tAno")
        print("------------------------------------------------------------------")
        for key, value in libros_ordenados:
            print(f"{key}\t\t{value['titulo_libro']}\t\t{value['autor']}\t\t{value['ano']}")

    def agregar_libros(self):
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        ano = input("Ingrese el ano de publicacion del libro: ")
        if self.validar_datos_libro(titulo, autor, ano):
            nuevo_id = str(int(max(self.libros_dict.keys())) + 1)
            self.libros_dict[nuevo_id] = {
                'titulo_libro': titulo,
                'autor': autor,
                'ano': ano
            }
            print(f"El libro '{titulo}' ha sido agregado con exito!!!")

    def validar_datos_libro(self, titulo, autor, ano):
        if not titulo or not autor or not ano:
            print("El titulo, autor y ano del libro no pueden estar vacios.")
            return False
        if not ano.isdigit() or len(ano) != 4:
            print("Por favor ingrese un ano de publicacion valido (4 digitos).")
            return False
        if titulo in [libro['titulo_libro'] for libro in self.libros_dict.values()]:
            print("Este libro ya existe en la biblioteca.")
            return False
        if len(titulo) > 20:
            print("El titulo del libro es demasiado largo!!! El limite es de 20 caracteres.")
            return False
        return True

    def buscar_libro(self):
        termino_busqueda = input("Ingrese el titulo o autor del libro a buscar: ").lower()
        libros_encontrados = [details for details in self.libros_dict.values() if
                              termino_busqueda in details['titulo_libro'].lower() or termino_busqueda in details[
                                  'autor'].lower()]
        if libros_encontrados:
            print("Libros encontrados:")
            for book in libros_encontrados:
                print(f"Titulo: {book['titulo_libro']}, Autor: {book['autor']}, Ano: {book['ano']}")
        else:
            print("No se encontraron libros con ese termino de busqueda.")

    def eliminar_libros(self):
        titulo_libro = input("Ingrese el titulo del libro a eliminar: ")
        found = False
        for book_id, details in list(self.libros_dict.items()):
            if details['titulo_libro'].lower() == titulo_libro.lower():
                del self.libros_dict[book_id]
                found = True
                print(f"El libro '{titulo_libro}' ha sido eliminado con exito!!!")
                break
        if not found:
            print("Libro no encontrado!!!")


def calcular_imc():
    peso = float(input("Peso en KG: "))
    altura = float(input("Altura en CMS: ")) / 100

    imc = peso / (altura ** 2)
    print(f"Tu IMC: {imc:.2f}")

    if imc < 18.5:
        print("Bajo peso")
    elif 18.5 <= imc < 25:
        print("Peso normal")
    elif 25 <= imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidad")


def calcular_interes_compuesto():
    capital_inicial = float(input("Capital inicial?: "))
    tasa_interes = float(input("Tasa de interes?: ")) / 100

    ano = 1
    while ano <= 5:
        capital_inicial *= (1 + tasa_interes)
        print(f"Ano {ano}: {capital_inicial:.2f}")
        ano += 1


def dibujar_diagrama_pastel(valores, etiquetas):
    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
    plt.title('Diagrama de Pastel')
    plt.show()


def obtener_entradas():
    while True:
        try:
            A = float(input("Ingrese el valor de A: "))
            B = float(input("Ingrese el valor de B: "))
            C = float(input("Ingrese el valor de C: "))
            if A <= 0 or B <= 0 or C <= 0:
                print("Solo valores positivos")
                continue
            return [A, B, C], ['A', 'B', 'C']
        except ValueError:
            print("Solo valores validos")


def dibujar_formas():
    numero_formas = int(input("Ingrese el numero de formas que desea dibujar: "))

    turtle.speed(0)

    def dibujar_triangulo(x, y, tamano, color):
        turtle.color(color)
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        for _ in range(3):
            turtle.forward(tamano)
            turtle.left(120)

    def dibujar_cuadro(x, y, tamano, color):
        turtle.color(color)
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        for _ in range(4):
            turtle.forward(tamano)
            turtle.left(90)

    def dibujar_pentagono(x, y, tamano, color):
        turtle.color(color)
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        for _ in range(5):
            turtle.forward(tamano)
            turtle.left(72)

    def dibujar_hexagono(x, y, tamano, color):
        turtle.color(color)
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        for _ in range(6):
            turtle.forward(tamano)
            turtle.left(60)

    formas = [dibujar_triangulo, dibujar_cuadro, dibujar_pentagono, dibujar_hexagono]
    colores = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']

    for _ in range(numero_formas):
        forma = random.choice(formas)
        color = random.choice(colores)
        tamano = random.randint(20, 100)
        x = random.randint(10, 200)
        y = random.randint(10, 200)
        cuadrantes = [(x, y), (-x, y), (-x, -y), (x, -y)]
        for cuadrantex, cuadrantey in cuadrantes:
            forma(cuadrantex, cuadrantey, tamano, color)

    turtle.done()


def menu_principal():
    libros_de_ejemplo = [
        ("libro_de_ejemplo1", "autor_de_ejemplo1", "2001"),
        ("libro_de_ejemplo2", "autor_de_ejemplo2", "2002"),
        ("libro_de_ejemplo3", "autor_de_ejemplo3", "2003"),
        ("libro_de_ejemplo4", "autor_de_ejemplo4", "2004"),
        ("libro_de_ejemplo5", "autor_de_ejemplo5", "2005")
    ]
    biblioteca = SistemaDeGestionDeBiblioteca(libros_de_ejemplo)

    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Biblioteca")
        print("2. Calcular IMC")
        print("3. Calcular Interés Compuesto")
        print("4. Crear Gráfico de Pastel")
        print("5. Dibujar Formas Geométricas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                print("\n--- Gestión de Biblioteca ---")
                print("A. Mostrar libros")
                print("B. Agregar libro")
                print("C. Buscar libro")
                print("D. Eliminar libro")
                print("E. Regresar al menú principal")

                opcion_biblio = input("Seleccione una opción: ").upper()

                if opcion_biblio == "A":
                    biblioteca.mostrar_libros()
                elif opcion_biblio == "B":
                    biblioteca.agregar_libros()
                elif opcion_biblio == "C":
                    biblioteca.buscar_libro()
                elif opcion_biblio == "D":
                    biblioteca.eliminar_libros()
                elif opcion_biblio == "E":
                    break
                else:
                    print("Opción no válida, por favor intente nuevamente.")

        elif opcion == "2":
            calcular_imc()

        elif opcion == "3":
            calcular_interes_compuesto()

        elif opcion == "4":
            valores, etiquetas = obtener_entradas()
            dibujar_diagrama_pastel(valores, etiquetas)

        elif opcion == "5":
            dibujar_formas()

        elif opcion == "6":
            print("¡Gracias por usar el Asistente de Gestión Personal!")
            break

        else:
            print("Opción no válida, por favor intente nuevamente.")


if __name__ == "__main__":
    menu_principal()
