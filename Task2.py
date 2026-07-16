def generate_pyramid():
    try:
        rows = int(input("Enter the number of rows for the pyramid: "))

        for i in range(1, rows + 1):

            for j in range(rows - i):
                print(" ", end="")

            for k in range(1, i + 1):
                print(k, end="")

            for l in range(i - 1, 0, -1):
                print(l, end="")

            print()
            
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    generate_pyramid()