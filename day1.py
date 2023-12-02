calibration_document = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

calibration_sum = 0

#controlla ogni riga
for line in calibration_document.split('\n'):
    #rimuovi le lettere
    digits_only = ''.join(filter(str.isdigit, line))
    first_digit = digits_only[0]
    last_digit = digits_only[-1]
    calibration_sum += int(first_digit + last_digit)

print(calibration_sum)
