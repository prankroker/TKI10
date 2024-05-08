def metaphone(word):
    word = word.upper()

    result = []
    i = 0
    length = len(word)

    def next_char(offset=1):
        if i + offset < length:
            return word[i + offset]
        return None

    while i < length:
        char = word[i]

        if char == 'A':
            if next_char() == 'E':
                i += 1
            else:
                result.append('A')
        elif char == 'B':
            if i == length - 1 and next_char() == 'M':
                result.append('M')
            else:
                result.append('B')
        elif char == 'C':
            if next_char() in ('E', 'I', 'Y'):
                result.append('S')
            else:
                result.append('K')
        elif char == 'D':
            if next_char() == 'G' or next_char() == 'J':
                result.append('J')
                i += 1
            else:
                result.append('D')
        elif char == 'G':
            if next_char() == 'H' and i < length - 2:
                result.append('J')
                i += 1
            else:
                result.append('G')
        elif char == 'H':
            if i > 0 and (i == length - 1 or word[i + 1] not in 'AEIOUY'):
                pass 
            else:
                result.append('H')
        elif char == 'F':
            if next_char() == 'F':
                i += 1
            else:
                result.append('F')
        elif char == 'K':
            if next_char() in ('N', 'G'):
                pass 
            else:
                result.append('K')
        elif char == 'P':
            if next_char() == 'H':
                result.append('F')
                i += 1
            else:
                result.append('P')
        elif char == 'Q':
            result.append('K')
        elif char == 'S':
            if next_char() == 'H':
                result.append('X')
                i += 1
            else:
                result.append('S')
        elif char == 'T':
            if next_char() == 'H':
                result.append('0')
                i += 1
            elif next_char() == 'I' and next_char(2) == 'O' and next_char(3) == 'N':
                result.append('X') 
                i += 3
            else:
                result.append('T')
        elif char == 'V':
            result.append('F')
        elif char == 'W':
            if next_char() not in 'AEIOUY':
                pass 
            else:
                result.append('W')
        elif char == 'X':
            if i > 0 and word[i - 1] in 'EIY':
                result.append('S')
            else:
                result.append('X')
        elif char == 'Y':
            if next_char() not in 'AEIOU':
                pass 
            else:
                result.append('Y')
        elif char == 'Z':
            result.append('S')
        else:
            pass

        i += 1

    return ''.join(result)

names = ["Melnyk","Shevchenko","Kovalenko","Bondarenko","Boyko","Tkachenko","Kravchenko","Kovalchuk","Koval","Oliynyk","Shevchuk","Polishchuk","Tkachuk","Savchenko",
"Bondar","Marchenko","Rudenko","Moroz","Lysenko","Petrenko","Klymenko","Pavlenko","Kravchuk","Kuzmenko","Ponomarenko","Savchuk","Vasylenko","Levchenko","Kharchenko",
"Sydorenko","Karpenko","Havryliuk","Shvets"]

for name in names:
    metaphone_code = metaphone(name)
    print(f"{name}: {metaphone_code}")
