
# Dies ist ein einzeiliger Kommentar
#print("Hallo, Welt!") # Ein Kommentar kann auch am Ende einer Codezeile stehen

"""
Dies ist ein mehrzeiliger Kommentar.
Er erstreckt sich über mehrere Zeilen.
"""


'''
Ein weiterer mehrzeiliger Kommentar
mit dreifachen Hochkommas.
'''

# Die Dateiendung für Python-Skripte ist üblicherweise .py

"""
VARIABLEN
Variablen ermöglichen uns Werte zu speichern und sie abzurufen
"""

def reverse_digits(n):
    # Convert the number to a string and reverse it
    reversed_str = str(n)[::-1]
    
    # Convert each character back to an integer and store it in a list
    reversed_digits = [int(char) for char in reversed_str]
    
    return reversed_digits

# Example usage:
number = 12345
result = reverse_digits(number)
print(result)  # Output: [5, 4, 3, 2, 1]

