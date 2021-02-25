import os


def open_file():
    base_path = os.path.dirname(os.getcwd())
    in_path = os.path.join(base_path, 'in', 'a_example')

    with open(in_path) as in_file:
        content = in_file.read()
        print(content)

def main():
    open_file()

if __name__ == '__main__':
    main()

#lennox was here 