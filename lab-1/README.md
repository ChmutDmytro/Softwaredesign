# Лабораторна робота 1, Чмут Дмитро

## Принципи програмування в коді

### 1. DRY (Don't Repeat Yourself):
**Опис:**
Цей принцип закликає уникати дублювання коду, використовуючи функції, методи та класи для уникнення повторень.

**Демонстрація в коді:**
відображено у коді через використання замовчуваних методів у класах ([MonthlyStatistics](https://gitlab.com/2022-2026/ipz-22-4/chmut-dmitro/softwaredesign/-/blob/main/lab-1/zoo_classes.py#L44)), та ([Inventory](https://gitlab.com/2022-2026/ipz-22-4/chmut-dmitro/softwaredesign/-/blob/main/lab-1/zoo_classes.py#L101)). Метод _display_count забезпечує вивід кількості подій чи працівників, уникуючи повторення коду та забезпечуючи зручний механізм виведення інформації.

### 2. KISS (Keep It Simple, Stupid):

**Опис:**
KISS стверджує, що простий код – це кращий код. Складність повинна бути уникнена.

**Демонстрація в коді:**
Принцип KISS демонструється у класі ([Animal](https://gitlab.com/2022-2026/ipz-22-4/chmut-dmitro/softwaredesign/-/blob/main/lab-1/zoo_classes.py#L61)), де метод feed виконує лише одну просту задачу - виведення повідомлення про те, що тварина їсть.

### 3. SOLID (Single Responsibility Principle):

**Опис:**
SOLID - це аббревіатура п'яти принципів: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion. Кожен з цих принципів спрямований на створення гнучких, розширюваних та підтримуваних систем.

**Демонстрація в коді:**
Один з SOLID принципів, наприклад,Клас ([ZooManager](https://gitlab.com/2022-2026/ipz-22-4/chmut-dmitro/softwaredesign/-/blob/main/lab-1/zoo_classes.py#L29))відповідає за управління зоопарком, забезпечуючи метод display_monthly_statistics, який може бути розширений для виведення статистики за місяць

### 4. Composition Over Inheritance:

**Опис:**
Composition Over Inheritance вказує на те, що краще використовувати композицію об'єктів, ніж успадкування класів, для досягнення більшої гнучкості та обмеження залежностей.

### 5. Composition Over Inheritance:

**Опис:**
Використовує композицію замість спадкування для побудови відносин між класами.

**Демонстрація в коді:**
Клас ([ZooManager](https://gitlab.com/2022-2026/ipz-22-4/chmut-dmitro/softwaredesign/-/blob/main/lab-1/zoo_classes.py#L1)) містить екземпляри класів Enclosure, Animal, і т.д., замість того, щоб успадковувати їх.

### 6. Fail Fast:

**Опис:**
Fail Fast вказує на те, що програма має негайно виявляти помилки та завершувати виконання.

