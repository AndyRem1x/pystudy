sentence = input("Input your sentence:  ")
sentence_list = sentence.split()
dict_sentence = {key: sentence_list.count(f"{key}") for key in sentence_list}
print(dict_sentence)
