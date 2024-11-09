#MATCH 
"""name = input("Name ?")

print(name)

match name:
    case "A" | "B" | "C":
        print("ABC")
    
    case "D" | "E":
        print("DE")

    case _:
        print("Alphabet")"""


def main():
    x = get_int("What is x? ")
    print(f"X is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            pass


main()


