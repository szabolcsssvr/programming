Primary_Colors = ["Red", "Yellow", "Blue"]

class Color_Mixing:
    Num_of_Possible_Mixes = 0

    def __init__(self, Colors_Array):
        self.Colors_Array = Colors_Array
        self.Array_Size = len(Colors_Array)

        if (len(Colors_Array) > 0):
            self.Num_of_Possible_Mixes = 1

            for i in range(1, len(Colors_Array) + 1):
                self.Num_of_Possible_Mixes *= i