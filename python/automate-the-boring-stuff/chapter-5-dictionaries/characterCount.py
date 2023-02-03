message = 'a quick brown fox jumped over the lazy dog'
count={}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)