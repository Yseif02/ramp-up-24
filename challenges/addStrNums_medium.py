def add(num1, num2):
    if num1 is None or num2 is None or num1 == "" or num2 == "":
        return "Invalid Operation"
    else:
        try:
            sum = int(num1) + int(num2)
            return str(sum)
        except ValueError:
            return "Invalid Operation"

# print(add("111", "222")) # 333