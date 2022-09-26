def fact(angka):
    return 1 if angka == 1 else angka * fact(angka-1)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))