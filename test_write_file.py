# test_write_file.py

from tools.write_file import write_file

if __name__ == "__main__":
    # 1. Overwrite lorem.txt
    print('Test 1:')
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print()

    # 2. Create new file in pkg/
    print('Test 2:')
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print()

    # 3. Attempt to write outside calculator (should fail)
    print('Test 3:')
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print()
