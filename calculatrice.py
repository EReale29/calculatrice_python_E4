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

        else:
            print("Option invalide")

def main():
    calculatrice()


if __name__ == "__main__":
    main()
