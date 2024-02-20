"""" 
Desarollar una funcion que nos retorne verdadero o falso, si una palabra, texto, o enunciado es palindromo.
Palindromo: Palabra o frase, que se se lee igual tanto al derecho como al reves 
Ejemplo: ANA, Radar, kayak
"""

def palindromo(enunciado: str):
    """ Funcion que nos retorna verdadero o falso si una frase, palabra es palindroma """
    text = enunciado.replace(' ','').lower()
    return text == text[::-1]

if __name__=='__main__':
    variable_texto1 = 'radar'
    variable_texto2 = 'roma'
    variable_texto3 = 'anita lava la tina'
    print(f"{palindromo(variable_texto1)}")
    print(f"{palindromo(variable_texto2)}")
    print(f"{palindromo(variable_texto3)}")

