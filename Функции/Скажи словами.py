def number_in_english(num):
    nums = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
            12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
            16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
            6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
    in_english = ''
    if len(str(num)) == 3:
        if num // 100 > 0:
            in_english += f'{dict(list(nums.items())[:10])[num // 100]} hundred'
    units_and_tens = num % 100
    if units_and_tens > 0:
        if units_and_tens in nums.keys():
            if len(in_english) > 0:
                in_english += ' and '
            in_english += nums[units_and_tens]
        else:
            if len(in_english) > 0:
                in_english += ' and '
            if units_and_tens // 10 > 0:
                in_english += tens[units_and_tens // 10]
            if int(str(units_and_tens)[-1]) > 0:
                if units_and_tens // 10 > 0:
                    in_english += '-'
                in_english += nums[int(str(units_and_tens)[-1])]
    if num == 0:
        in_english = 'zero'
    return in_english;


print(number_in_english(0).lower())
print(number_in_english(1).lower())
