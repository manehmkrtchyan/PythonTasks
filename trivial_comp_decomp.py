choose  = str(input('''Enter 'compress' if you want to compress your program or 'decompress' if the text is already compressed. '''))
file = str(input('''Enter the name of the file you want to compress or decompress: '''))

def trivial_compression(file, choose):
    
        text_file  = open(file, 'r')
        text = text_file.read()

        if choose == 'compress':
            if text.isalnum :       
                groups= []
                last_char = None
                for char in text:
                    if char == last_char:
                        groups[-1].append(char)
                    else:
                        groups.append([char])
                    last_char = char
                lst = [f'{group[0]}{len(group)}' for group in groups]    
                return ''.join(lst)


        elif choose == 'decompress':                  
            stack = ""
            for i in range(len(text)):
                if text[i].isalpha():
                    if i + 1 < len(text) and text[i + 1].isdigit():
                        digit = text[i + 1]
                        char = text[i]
                        i += 2

                        while i < len(text) and text[i].isdigit():
                            digit += text[i]
                            i += 1
                        stack += char * int(digit)

                    else:
                        stack+= text[i]
                else:
                    ""
            return "".join(stack) 
        
        else:
            return 0

go_to_result = trivial_compression(file, choose)


with open('result.txt', 'w') as f:
    f.write(go_to_result)