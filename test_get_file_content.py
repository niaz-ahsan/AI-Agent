from functions.get_file_content import get_file_content

def test1():
    content = get_file_content("calculator", "lorem.txt")
    print(len(content))
    print(content[-51:])

def test2():
    content = get_file_content("calculator", "main.py")
    print(content)    

def test3():
    content = get_file_content("calculator", "pkg/calculator.py")
    print(content)   

def test4():
    content = get_file_content("calculator", "/bin/cat")
    print(content) 

def test5():
    content = get_file_content("calculator", "pkg/does_not_exist.py")
    print(content) 

def main():
    test1()
    print()
    test2()
    print()
    test3()
    print()
    test4()
    print()
    test5()
    print()

if __name__ == "__main__":
    main()