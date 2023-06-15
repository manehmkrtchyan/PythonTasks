import PyPDF2

def remove_symbols(word):
    special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<',
                            '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '...']
    for i in special_characters:
        word = word.replace(i, '')
    return word

with open('sample.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)

    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

set_of_text = set()

splitted = text.split()
for item in splitted:
    if item.isalpha():
        set_of_text.add(remove_symbols(item).lower())

with open('reuslt.txt', 'w+') as result:
    for word in set_of_text:
        result.write(word + '\n')

print(set_of_text)
