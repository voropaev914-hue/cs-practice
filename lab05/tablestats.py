def read_rows(lines) -> list[dict]:
    """Разбирает CSV с заголовком в список словарей.
    Пустые строки и строки с неверным количеством полей пропускаются.
    Пробелы вокруг значений отбрасываются.
    """
    header = None
    rows = []
    
    for line in lines:
        # Убираем символы переноса строки и лишние пробелы по краям
        clean_line = line.strip()
        if not clean_line:
            continue
            
        # Разбиваем строку по запятым и очищаем каждое поле от пробелов
        fields = [field.strip() for field in clean_line.split(',')]
        
        # Первая непустая строка становится заголовком
        if header is None:
            header = fields
            continue
            
        # Если количество полей не совпадает с заголовком, пропускаем
        if len(fields) != len(header):
            continue
            
        # Собираем словарь {колонка: значение}
        row_dict = {}
        for i in range(len(header)):
            row_dict[header[i]] = fields[i]
        rows.append(row_dict)
        
    return rows


def count_types(rows: list[dict]) -> dict:
    """Считает, сколько записей каждого типа присутствует в данных."""
    counts = {}
    for row in rows:
        kind = row.get("тип")
        if kind:
            counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    """Считает суммарные минуты записей одного типа, округляя до десятых.
    Нечисловые значения пропускаются, запятая заменяется на точку.
    """
    total = 0.0
    has_records = False
    
    for row in rows:
        if row.get("тип") == kind:
            has_records = True
            minutes_str = row.get("минуты", "0")
            # Заменяем запятую на точку, если она есть
            minutes_str = minutes_str.replace(",", ".")
            try:
                total += float(minutes_str)
            except ValueError:
                # Пропускаем нечисловые значения
                continue
                
    if not has_records:
        return 0.0
        
    return round(total, 1)


def to_csv(counts: dict) -> str:
    """Формирует сводку текстом CSV: заголовок тип,количество.
    Строки сортируются по алфавиту названия типа. В конце — перевод строки.
    """
    result = ["тип,количество"]
    # Сортируем ключи по алфавиту
    for kind in sorted(counts.keys()):
        result.append(f"{kind},{counts[kind]}")
        
    # Объединяем строки и добавляем финальный перенос строки
    return "\n".join(result) + "\n"
