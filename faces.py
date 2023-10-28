def main():
    s = input()
    ns = convert(s)
    print(ns)

def convert(s):
    s2 = s.replace(':)', '\U0001f642')
    s2 = s2.replace(':(', '\U0001f641')
    return s2


main()
