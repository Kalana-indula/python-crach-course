message = "Hello Python world"
print(message)

#To make starting letter uppercase of each word
name='ada lovelase'
print(name.title())

phrase='girraffe academy'
print(len(phrase))

print(phrase[0])
print(phrase[10])

print(phrase.index("a"))
print(phrase.index("g"))
print(phrase.index("acad"))

print(phrase.replace("girraffe","cat"))
new_phrase=phrase.replace("girraffe","cat")
print(new_phrase)

new_phrase=phrase.split(' ')
print(new_phrase)

joined_phrase='and'.join(new_phrase)
print(joined_phrase)

#remove white space
name_whitespace = " Eric "
print(name_whitespace.rstrip())
print(name_whitespace.lstrip())
print(name_whitespace.strip())

