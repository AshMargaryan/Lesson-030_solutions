sentence = input()

def reverse_sentece(sentence):
    splited = sentence.split(" ")
    reversed_list = splited[::-1]

    reversed_sentence = ""

    for k in reversed_list:
        reversed_sentence += k + " "

    return reversed_sentence[:-1]

print(reverse_sentece(sentence))