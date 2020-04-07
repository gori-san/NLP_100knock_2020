def main():
    sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    word_list = sentence.rstrip('\n').split()
    char_num_list = []
    for w in word_list:
        char_num_list.append(len(w.strip('.'',')))
    print(char_num_list)


if __name__ == '__main__':
    main()

# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
