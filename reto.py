#!/usr/bin/python3

# Hola {nombre} y {apellido}
def reto_1_2(first_name, last_name):
  print(f"Hello, {first_name} {last_name}")

# Mensaje multilinea
def reto_3()
  print("""
Platzi cuenta con mas de 600 cursos en categorias como:
- Desarrollo e Ingenieria
- Marketing
- Produccion Audiovisual
- Crecimiento Profecional
- Disenio y UX
- Negocios y Emprendimiento
  """)
def main():
  print("""
Enter a letter to select what you want to do
[1] - Para reto de imprimir tu nombre y apellido
[3] - Para reto de imprimir categorias de Platzi
[4] - Para reto de suma de numeros
[5] - Para reto de suma y multiplicacion
[6] - Para reto de resta de pizzas
[7] - Para reto de edad futura y pasada
[8] - Para reto de divide la cuenta
[9] - Para reto de calculando dias
[10] - Para reto de conversor de millas
[11] - Para reto de cuantas veces un numero aparece en otro
""")

if __name__ == "__main__":
  main()
  letter = input("-> ")
  if letter == "1" or letter == "2":
    scan_fname = input("What is your name?\n-> ")
    scan_lname = input("What is your last name?\n-> ")
    reto_1_2(scan_fname, scan_lname)
  else:
    print("Eu")

