from functions.run_python_file import run_python_file

def test1():
    print("="*20)
    print('run_python_file("calculator", "main.py")')
    print(run_python_file("calculator", "main.py"))

def test2():
    print("="*20)
    print('run_python_file("calculator", "main.py", ["3 + 5"])')
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

def test3():
    print("="*20)
    print('run_python_file("calculator", "tests.py")')
    print(run_python_file("calculator", "tests.py"))

def test4():
    print("="*20)
    print('run_python_file("calculator", "../main.py")')
    print(run_python_file("calculator", "../main.py"))

def test5():
    print("="*20)
    print('run_python_file("calculator", "nonexistent.py")')
    print(run_python_file("calculator", "nonexistent.py"))

def test6():
    print("="*20)
    print('run_python_file("calculator", "lorem.txt")')
    print(run_python_file("calculator", "lorem.txt"))


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()

if __name__ == "__main__":
    main()