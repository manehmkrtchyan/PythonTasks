text = str(input("Enter the text here: "))


def number_of_words(text):                  
    skips = [".", ",", ":", ";", "'", '"', '?', '!'] 
    for char in text:
        if char in skips: 
            text = text.replace(char, "") 
    number_of_words_dict = {} 
    for word in text.split(" "): 
        if word != "":
            if word in number_of_words_dict: 
                number_of_words_dict[word]+= 1 
            else: 
                number_of_words_dict[word]= 1 
    count = sum([int(i) for i in number_of_words_dict.values()])
    max_frequency_of_words = max([int(i) for i in number_of_words_dict.values()])
    return(f"The number of words is {count}: {number_of_words_dict} and maximum frequency is {max_frequency_of_words} \n")  

def number_of_letters(text):
    skips = [".", ",", ":", ";", "'", '"'] 
    for char in text:
        if char in skips: 
            text = text.replace(char, "") 
    number_of_letters = {}
    letters = [*text]
    for letter in letters:
        if letter != " ":
            if letter in number_of_letters:
                number_of_letters[letter] += 1
            else:
                number_of_letters[letter] = 1
    count = sum([int(i) for i in number_of_letters.values()])
    max_frequency_of_letters = max([int(i) for i in number_of_letters.values()])
    return(f'The number of letters is {count}: {number_of_letters} and maximum frequency of letters is {max_frequency_of_letters} \n'  )
    
def number_of_sentences(text):
    number_of_sentences = text.count(".") + text.count("?") + text.count("!")
    return f"The number of sentences is {number_of_sentences}"


letters = number_of_letters(text)
words = number_of_words(text)
sentences = number_of_sentences(text)

with open('result.txt', 'w') as f:
    f.write(str(letters))
    f.write(str(words))
    f.write(str(sentences))
