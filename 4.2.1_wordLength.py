def word_Length(word_list):
    Length_list = [len(i) for i in word_list]
    return Length_list


if __name__ == '__main__':
    print("Enter the words one by one and '#end_list' to the end")
    words_list = []
    while True:
        inp = input().strip()
        if inp != '#end_list':
            words_list.append(inp)
        else:
            break
    words_length = word_Length(words_list)
    print(words_length)
