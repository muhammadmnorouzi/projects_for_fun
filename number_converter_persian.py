#!/usr/bin/python3

def convert_numeric_money_to_string(indata : str) -> str:
    if indata.isnumeric() == False:
        return "Input should be numeric ... "
    
    if len(indata) == 1 and indata == '0':
        return 'بی پولی و بدبختی'

    if int(indata) >= 10**61:
        return "Input should be < 10^61"

    indata = list(indata)
    result = []
    
    zero2nine = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
    ten2nineteen = ["ده", "یازده", "دوازده", "سیزده", "چهارده", "پانزده", "شانزده", "هفده", "هجده", "نوزده"]
    zero2nineteen = zero2nine + ten2nineteen
    ten_twenty_and_more = ["", "ده", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
    oneh_twoh_and_more = ["", "صد", "دویست", "سیصد", "چهارصد", "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"]
    coef = {3: "هزار", 
            6: "میلیون", 
            9: "میلیارد", 
            12: "تریلیون",
            15: "کوآدریلیون", 
            18: "کوینتیلیون", 
            21: "سکستیلیون", 
            24: "سپتیلیون",
            27: "اکتیلیون", 
            30: "نانیلیون", 
            33: "دسیلیون", 
            36: "آندسیلیون",
            39: "دیودسیلیون", 
            42: "تریدسیلیون", 
            45: "کواتیوردسیلیون", 
            48: "کویندسیلیون",
            51: "سکسدسیلیون", 
            54: "سپتدسیلیون", 
            57: "اکتودسیلیون", 
            60: "نومدسیلیون"}
    
    indata.reverse()
    data_len = len(indata)
    
    while data_len > 0:
        current = int(indata[data_len - 1])
        remainder = data_len % 3
 
        if any(result) and remainder == 0 and data_len > 0 and result[-1] not in coef.values():
            result.append(coef[data_len])

        if current == 0:
            data_len -= 1
            continue

        if any(result):
            result.append("و")

        # sadgan
        if remainder == 0:
            result.append(oneh_twoh_and_more[current])
        # yekan
        elif remainder == 1:
            result.append(zero2nine[current])
        # dahgan
        elif remainder == 2:
            if current == 1:
                current_yekan = int(indata[data_len - 2])
                result.append(zero2nineteen[current * 10 + current_yekan])
                data_len -= 1
            else:
                result.append(ten_twenty_and_more[current])
        
        data_len -= 1

    result.append('تومان')
    return str.join(' ' , result)

print("Github : muhammadmnorouzi")

while True:
    user_input = input("Enter a numeric money amount or 'q' to break: ")

    if 'q' in user_input:
        break

    result = convert_numeric_money_to_string(user_input)
    print(result)