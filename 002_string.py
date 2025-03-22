my_sentence = "python is fun and powerful"
print(len(my_sentence))
print(my_sentence[0])
print(my_sentence[8:22])
sentence = my_sentence.lower
print(my_sentence.lower())
print(my_sentence.count("o"))
print(my_sentence.find("fun"))
new_sentence = my_sentence.replace("powerful", "amazing")
print(new_sentence)
new_message = "learning python is exciting"
sentence = my_sentence + ', ' + new_message
print(sentence)
sentence = '{} {}'.format(my_sentence, new_message)
print(sentence)
sentence = f'{my_sentence}, {new_message}'
print(dir(my_sentence))
print(help(str.replace))





