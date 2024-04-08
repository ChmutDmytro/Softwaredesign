import re

class SmartTextReader:
    def __init__(self, filename):
        self.filename = filename

    def read_text(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                return [list(line.strip()) for line in lines]
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return None

class SmartTextChecker:
    def __init__(self, text_reader):
        self.text_reader = text_reader

    def read_text(self):
        print("Opening file...")
        text = self.text_reader.read_text()
        if text:
            num_lines = len(text)
            num_chars = sum(len(line) for line in text)
            print("File successfully read.")
            print(f"Number of lines: {num_lines}")
            print(f"Number of characters: {num_chars}")
            return text
        else:
            print("Failed to read file.")
            return None

class SmartTextReaderLocker:
    def __init__(self, text_reader, regex_pattern):
        self.text_reader = text_reader
        self.regex_pattern = regex_pattern

    def read_text(self):
        if re.match(self.regex_pattern, self.text_reader.filename):
            print("Access denied!")
            return None
        else:
            return self.text_reader.read_text()

if __name__ == "__main__":
    # Створення екземпляру SmartTextReader для тестування
    text_reader = SmartTextReader("test.txt")

    # Створення екземпляру SmartTextChecker для логування
    checker = SmartTextChecker(text_reader)
    print("Checking text:")
    checker.read_text()
    print()

    # Створення екземпляру SmartTextReaderLocker з обмеженим доступом до файлів, що починаються на 'restricted'
    locker = SmartTextReaderLocker(text_reader, r"restricted.*")
    print("Trying to read 'test.txt':")
    locker.read_text()
    print()

    # Створення екземпляру SmartTextReaderLocker з обмеженим доступом до файлів, що починаються на 'allowed'
    locker_allowed = SmartTextReaderLocker(text_reader, r"allowed.*")
    print("Trying to read 'allowed_file.txt':")
    locker_allowed.read_text()
    print("Trying to read 'allowed_file2.txt':")
    text_reader2 = SmartTextReader("allowed_file2.txt")
    checker2 = SmartTextChecker(text_reader2)
    checker2.read_text()