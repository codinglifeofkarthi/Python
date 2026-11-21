class mulfunction():

    def BMI():
        BMI = int(input("Enter the BMI Index: "))

        if BMI < 18.5:
            print("Under Weight")
            msg = "Under Weight"

        elif BMI < 24.9:
            print("Normal Weight")
            msg = "Normal Weight"

        elif BMI <= 29.9:
            print("Over Weight")
            msg = "Over Weight"

        elif BMI <= 34.9:
            print("Obese class1 with over weight")
            msg = "Obese class1 with over weight"

        elif BMI <= 39.9:
            print("Obese class2 with over weight")
            msg = "Obese class2 with over weight"

        else:
            print("Obese class3 with over weight")
            msg = "Obese class3 with over weight"

        return msg

    def findoddoreven():
        num = int(input("Enter the number: "))

        if num % 2 == 0:
            print(num, "is an even number")
        else:
            print(num, "is an odd number")