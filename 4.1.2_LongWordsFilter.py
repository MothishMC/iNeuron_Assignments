def filter_long_words(word_list, threshold):
    return_list = [i for i in word_list if len(i) >= threshold]
    return return_list


if __name__ == '__main__':
    n = int(input("Enter the value for n : "))
    print("Enter the words one by one and '#end_list' to the end")
    words_list = []
    while True:
        inp = input().strip()
        if inp != '#end_list':
            words_list.append(inp)
        else:
            break
    words = filter_long_words(words_list, n)
    print(words)
