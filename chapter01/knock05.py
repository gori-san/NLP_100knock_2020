def get_ngram(target_list, n):
    ngram_list = []
    for i in range(len(target_list)-n+1):
        ngram_list.append(target_list[i:i+n])
    return ngram_list


def main():
    sentence = 'I am an NLPer'
    word_list = sentence.rstrip('\n').split()
    char_list = list(sentence.replace(' ', ''))
    n = 2
    print(get_ngram(word_list, n))
    print(get_ngram(char_list, n))


if __name__ == '__main__':
    main()

# [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
# [['I', 'a'], ['a', 'm'], ['m', 'a'], ['a', 'n'], ['n', 'N'], ['N', 'L'], ['L', 'P'], ['P', 'e'], ['e', 'r']]
