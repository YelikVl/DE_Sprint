def arabic_to_roman(x):
    output = ""

    while x > 0:
        if x >= 1000:
            x -= 1000
            output += "M"
        elif x >= 900:
            x -= 900
            output += "CM"
        elif x >= 500:
            x -= 500
            output += "D"
        elif x >= 400:
            x -= 400
            output += "CD"
        elif x >= 100:
            x -= 100
            output += "C"
        elif x >= 90:
            x -= 90
            output += "XC"
        elif x >= 50:
            x -= 50
            output += "L"
        elif x >= 40:
            x -= 40
            output += "XL"
        elif x >= 10:
            x -= 10
            output += "X"
        elif x >= 9:
            x -= 9
            output += "IX"
        elif x >= 5:
            x -= 5
            output += "V"
        elif x >= 4:
            x -= 4
            output += "IV"
        elif x >= 1:
            x -= 1
            output += "I"
    return output
