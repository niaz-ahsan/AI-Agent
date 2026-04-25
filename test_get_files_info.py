from functions.get_files_info import get_files_info

def test1():
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

def test2():
    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

def test3():
    print("Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))

def test4():
    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))

def main():
    test1()
    print()
    test2()
    print()
    test3()
    print()
    test4()

# Checking if this file is executed directly
if __name__ == "__main__":
    main()