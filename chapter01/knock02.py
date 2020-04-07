def main():
    s1 = 'パトカー'
    s2 = 'タクシー'
    for i, j in zip(s1, s2):
        print(i+j, end='')
    print('')


if __name__ == '__main__':
    main()
