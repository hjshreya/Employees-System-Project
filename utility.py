def input_is_valid(prompt, start=0, end=None):
    while True:
        try:
            value = int(input(prompt))

            if end is not None and not (start <= value <= end):
                print(f"Please enter a number between {start} and {end}.")
            elif value < start:
                print(f"Please enter a number greater than or equal to {start}.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")

