from pathlib import Path


# find the most common word in a file
def most_common_word(file: Path) -> str:
    '''
    Open a file and read texts from the file. If the file is not
    a text file, the error will be raised. Otherwise, seperate each
    line of text by spaces. If we encounter characters other than
    letters, we will return the only_char if only_char is not empty
    if the character is uppercase or lowercase letter, append to a
    variable only_char to words_list, which contains all of the words
    in this file.
    '''
    try:
        the_file = file.open('r')
        texts = the_file.readlines()
        count = {}
        words_list = []
        if len(texts) != 0:
            for text in texts:
                words = text.split()
                for word in words:
                    only_char = ''
                    for char in word:
                        if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                            only_char += char
                        else:
                            if len(only_char) > 0:
                                words_list.append(only_char)
                    if len(only_char) > 0:     
                        words_list.append(only_char)
        else:
            return ''

        # if word is in the dictionary count, the count of that word will
        # add one to it. Otherwise, append the word to count dictionary and
        # set the count to 1. Both circumstance will remove the word from
        # the words_list
        keys = count.keys()
        values = count.values()
        while len(words_list) > 0:
            word = words_list[0]
            if word in keys:
                for key in keys:
                    if key == word:
                        count[key] += 1
                        words_list.remove(word)
            
            else:
                count[word] = 1
                words_list.remove(word)

        # find the max value in the count dictionary.
        max_count = max(values)
        for key in count.keys():
            if count[key] == max_count:
                return key
    finally:
        if the_file != None:
            the_file.close()
