my_sentence ="Python is fun and powerful"
print(len(my_sentence))
print(my_sentence[0])
print(my_sentence[8:22])
print(my_sentence.lower())
print(my_sentence.count("O"))
print(my_sentence.find("fun"))
new_sentence = my_sentence.replace("Powerful", "Amazing")
print(new_sentence)
new_message = "Learning Python is exciting"
sentence =my_sentence + ', ' + new_message
print(sentence)
sentence = '{}, {}'.format(my_sentence, new_sentence)
print(sentence)
sentence = f'{my_sentence}, {new_sentence}'
print(sentence)
print(dir(my_sentence))
print(help(str.replace))




