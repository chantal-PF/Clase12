nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))
examen = int(input("Examen: "))
suma = nota1 + nota2 + nota3 + examen
promedio = suma / 4

if promedio > 89 and promedio < 101:
    print("A")
elif promedio > 79 and promedio < 90:
    print("B")
elif promedio > 69 and promedio < 80:
    print("C")
elif promedio > 59 and promedio < 70:
    print("D")
else:
    print("E")
      
