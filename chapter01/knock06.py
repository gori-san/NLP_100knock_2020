from knock05 import get_ngram


def main():
    s1 = 'paraparaparadise'
    s2 = 'paragraph'
    X = set(get_ngram(s1, 2))
    Y = set(get_ngram(s2, 2))
    s_union = X | Y
    s_intersection = X & Y
    s_difference = X - Y
    print(s_union)
    print(s_intersection)
    print(s_difference)
    print('se in X') if 'se' in X else print('se not in X')
    print('se in Y') if 'se' in Y else print('se not in Y')


if __name__ == '__main__':
    main()

# {'ar', 'ra', 'di', 'ph', 'ag', 'gr', 'ad', 'is', 'pa', 'ap', 'se'}
# {'pa', 'ra', 'ap', 'ar'}
# {'se', 'is', 'di', 'ad'}
# se in X
# se not in Y
