def ajouter(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def multiplier(a, b):
    return a * b

def diviser(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro"
    
def calculatrice():
    while True:
        print("Options:")
        print("Entrez 'add' pour additionner deux nombres")
        print("Entrez 'subtract' pour soustraire deux nombres")
        print("Entrez 'multiply' pour multiplier deux nombres")
        print("Entrez 'divide' pour diviser deux nombres")
        print("Entrez 'test' pour tester les fonctions")
        print("Entrez 'quit' pour finir l'opération")

        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ("add", "subtract", "multiply", "divide"):
            num1 = float(input("Entrez le premier nombre: "))
            num2 = float(input("Entrez le deuxième nombre: "))

            if user_input == "add":
                print("Résultat:", ajouter(num1, num2))
            elif user_input == "subtract":
                print("Résultat:", soustraire(num1, num2))
            elif user_input == "multiply":
                print("Résultat:", multiplier(num1, num2))
            elif user_input == "divide":
                print("Résultat:", diviser(num1, num2))
            elif user_input == "test":
                print("Résultat test ajouter:", test_ajouter())
                print("Résultat test soustraire:", test_soustraire())
                print("Résultat test multiplier:", test_multiplier())
                print("Résultat test diviser:", test_diviser())

        else:
            print("Option invalide")

def main():
    calculatrice()

def test_ajouter():
    assert ajouter(2, 3) == 5
    assert ajouter(-1, 1) == 0
    assert ajouter(0, 0) == 0

def test_soustraire():
    assert soustraire(5, 3) == 2
    assert soustraire(10, 7) == 3
    assert soustraire(0, 0) == 0
    assert soustraire(5, 10) == -5

def test_multiplier():
    assert multiplier(2, 3) == 6
    assert multiplier(-1, 5) == -5
    assert multiplier(0, 10) == 0
    assert multiplier(5, 0) == 0

def test_diviser():
    assert diviser(10, 2) == 5
    assert diviser(15, 3) == 5
    assert diviser(0, 5) == 0
    assert diviser(5, 0) == "Erreur : Division par zéro"

if __name__ == "__main__":
    main()
