# test_run_python_file.py

from tools.run_python_file import run_python_file

if __name__ == "__main__":
    print("Test 1: main.py (no args)")
    print(run_python_file("calculator", "main.py"))
    print()

    print("Test 2: main.py with args ['3 + 5']")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print()

    print("Test 3: tests.py")
    print(run_python_file("calculator", "tests.py"))
    print()

    print('Test 4: "../main.py" (should fail)')
    print(run_python_file("calculator", "../main.py"))
    print()

    print('Test 5: nonexistent file')
    print(run_python_file("calculator", "nonexistent.py"))
    print()

    print('Test 6: not a python file')
    print(run_python_file("calculator", "lorem.txt"))
    print()
