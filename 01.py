"""
Imprimir en una linea separados por coma todos los elementos que sean divisibles por 7 y no sean multipolos de 5 entre 20000 y 32000
(Incluyendo estos elementos).Trabajar con listas.
"""

print([number for number in range(20000, 32000) if number % 7 == 0 and not number % 5 == 0])

