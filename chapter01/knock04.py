def main():
    sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    word_list = sentence.rstrip('\n').split()
    char_dict = {}
    for i, w in enumerate(word_list):
        if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            char_dict[w[0]] = i+1
        else:
            char_dict[w[:2]] = i+1
    print(char_dict)


if __name__ == '__main__':
    main()

# {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
