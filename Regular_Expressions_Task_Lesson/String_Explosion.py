some_text = input()
final_string = ""
explosion_strength = 0

for index in range(len(some_text)):
    if explosion_strength > 0 and some_text[index] != '>':
        explosion_strength -= 1
    elif some_text[index] == ">":
        final_string += '>'
        explosion_strength += int(some_text[index + 1])
    else:
        final_string += some_text[index]
print(final_string)
