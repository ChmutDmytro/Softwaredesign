# Клас FileWriter з методами Write() та WriteLine() для запису в файл
class FileWriter:

    def __init__(self, filename):
        self.filename = filename

    def Write(self, text):
        with open(self.filename, 'w') as file:
            file.write(text)

    def WriteLine(self, line):
        with open(self.filename, 'a') as file:
            file.write(line + '\n')



class Logger:
    # Метод для виведення звичайного повідомлення
    def Log(self, message):
        print(f"LOG: {message}")

    # Метод для виведення повідомлення про помилку
    def Error(self, message):
        print(f"ERROR: {message}")

    # Метод для виведення попередження
    def Warn(self, message):
        print(f"WARN: {message}")


class FileWriterAdapter(Logger):
    def __init__(self, filename):
        self.file_writer = FileWriter(filename)

    # Метод Log() адаптера
    def Log(self, message):
        self.file_writer.WriteLine(f"LOG: {message}")

    # Метод Error() адаптера
    def Error(self, message):
        self.file_writer.WriteLine(f"ERROR: {message}")

    # Метод Warn() адаптера
    def Warn(self, message):
        self.file_writer.WriteLine(f"WARN: {message}")


# Головний метод програми
def main():
    # Створюємо екземпляр класу FileWriterAdapter для запису повідомлень у файл log.txt
    adapter = FileWriterAdapter("log.txt")
    # Використовуємо адаптер для запису повідомлень
    adapter.Log("Це звичайне повідомлення")
    adapter.Error("Це повідомлення про помилку")
    adapter.Warn("Це попередження")


if __name__ == "__main__":
    main()