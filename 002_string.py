my_sentence: "Python is fun and powerful!"
print(len(my_sentence))
print(my_sentence[0])
print(my_sentence[9:])
lowercase_sentence = my_sentence.lower()
print(lowercase_sentence)
print(my_sentence.count(o))
print(my_sentence[9:11])
my_sentence = my_sentence.replace('powerful', 'amazing')
print(my_sentence)

new_message: "Learning python is exciting!"

new_sentence = my_sentence + ', ' + new_message
print(new_sentence)
new_sentence = '{}, {}'.format(my_sentence, new_message)
print(new_sentence)
new_sentence =f'{my_sentence}, {new_message}'
print(new_sentence)
print(dir(my_sentence))
print(help(str))

