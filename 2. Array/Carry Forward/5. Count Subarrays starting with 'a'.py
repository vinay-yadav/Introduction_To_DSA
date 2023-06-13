string = "australia"

character_count = 0
answer = 0

for i in range(len(string) - 1, -1, -1):
    if string[i] == "a":
        character_count += 1
        answer += character_count

    else:
        character_count += 1

print("answer: ", answer)
