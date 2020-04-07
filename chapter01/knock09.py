import random


def main():
    sentence = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
    word_list = sentence.rstrip().split(' ')
    result = []
    for w in word_list:
        if len(w) <= 4:
            result.append(w)
            continue
        char_list = list(w[1:-1])
        random.shuffle(char_list)
        result.append(w[0] + ''.join(char_list) + w[-1])
    print(' '.join(result))


if __name__ == '__main__':
    main()
