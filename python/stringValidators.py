def run():
    s = input()
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in s))

if __name__ == '__main__':
    run()
