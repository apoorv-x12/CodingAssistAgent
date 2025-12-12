# test_get_file_content.py

from tools.get_file_content import get_file_content

if __name__ == "__main__":
    # 1. Test lorem.txt truncation
    content = get_file_content("calculator", "lorem.txt")
    print("Length:", len(content))
    print("Ends with truncation message:", content.endswith('characters]'))
    print()

    # 2. Test reading main.py
    print("main.py content:")
    print(get_file_content("calculator", "main.py"))
    print()

    # 3. Test reading pkg/calculator.py
    print("pkg/calculator.py content:")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    # 4. Test outside directory
    print('Attempting to read "/bin/cat":')
    print(get_file_content("calculator", "/bin/cat"))
    print()

    # 5. Test nonexistent file
    print('Attempting to read pkg/does_not_exist.py:')
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print()
