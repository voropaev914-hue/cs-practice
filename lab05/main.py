import sys
from tablestats import read_rows, count_types, total_minutes, to_csv

def main():
    # Читаем имя таблицы из первой строки ввода
    filename = input().strip()
    
    # Открываем файл и обрабатываем данные
    with open(filename, encoding="utf-8") as table:
        rows = read_rows(table)
        
    # Считаем метрики
    counts = count_types(rows)
    err_minutes = total_minutes(rows, "ошибка")
    
    # Выводим три числа по условию задачи
    print(len(rows))
    print(len(counts))
    print(err_minutes)
    
    # Записываем итоговую сводку в summary.csv
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))

if __name__ == "__main__":
    main()
