def cipher(sentence):
    new_sentence = ''
    for c in sentence:
        if c.islower():
            new_sentence += chr(219-ord(c))
        else:
            new_sentence += c
    return new_sentence


def main():
    sentence = 'He is from Japan'
    print(cipher(sentence))
    print(cipher(cipher(sentence)))


if __name__ == '__main__':
    main()

# Hv rh uiln Jzkzm
# He is from Japan
