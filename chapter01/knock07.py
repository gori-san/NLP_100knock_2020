def template_func(x, y, z):
    return f'{x}時の{y}は{z}'


def main():
    x = 12
    y = '気温'
    z = 22.4
    print(template_func(x, y, z))


if __name__ == '__main__':
    main()
