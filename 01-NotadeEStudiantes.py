nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))
examen = int(input("Examen: "))
suma = nota1 + nota2 + nota3 + examen
promedio = suma / 4

if promedio >= 90:
    print("A")
elif promedio >= 80:
    print("B")
elif promedio >= 70:
    print("C")
elif promedio >= 60:
    print("D")
else:
    print("E")
      