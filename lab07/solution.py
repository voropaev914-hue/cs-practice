import numpy as np


def reshape_table(values, rows, columns):
    """Раскладывает значения в таблицу заданной формы."""
    try:
        arr = np.asarray(values, dtype="float64")
        
        if rows < 0 or columns < 0:
            return []
        
        if arr.size != rows * columns:
            return []
        
        return arr.reshape(rows, columns).tolist()
    except Exception:
        return []


def select_block(matrix, row_start, row_stop, column_start, column_stop):
    """Прямоугольный срез таблицы."""
    try:
        arr = np.asarray(matrix, dtype="float64")
        
        if arr.ndim != 2 or arr.size == 0:
            return []
        
        return arr[row_start:row_stop, column_start:column_stop].tolist()
    except Exception:
        return []


def replace_block(matrix, row_start, row_stop, column_start, column_stop, value):
    """Возвращает копию таблицы с заменённым блоком."""
    try:
        arr = np.asarray(matrix, dtype="float64")
        
        if arr.ndim != 2 or arr.size == 0:
            return []
        
        changed = arr.copy()
        changed[row_start:row_stop, column_start:column_stop] = float(value)
        
        return changed.tolist()
    except Exception:
        return []


def transpose_table(matrix):
    """Меняет строки и столбцы местами."""
    try:
        arr = np.asarray(matrix, dtype="float64")
        
        if arr.ndim != 2 or arr.size == 0:
            return []
        
        return arr.T.tolist()
    except Exception:
        return []