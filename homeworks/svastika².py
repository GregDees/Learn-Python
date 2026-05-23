
def make_swastika_pattern(size: int):
    """
    Создаёт булеву матрицу для свастики размером size x size.
    Возвращает список списков bool: True - в этом месте часть свастики, False - пусто.
    size должен быть нечётным >= 3.
    """
    if size % 2 == 0 or size < 3:
        raise ValueError("Size must be odd and >= 3")
    half = size // 2
    pattern = []
    for i in range(size):
        row = []
        for j in range(size):
            # Правила классической свастики
            if i == half or j == half:
                row.append(True)           # центральные линии
            elif i < half and j < half and j == 0:
                row.append(True)           # левый верхний угол
            elif i < half and j > half and i == 0:
                row.append(True)           # правый верхний угол
            elif i > half and j < half and i == size-1:
                row.append(True)           # левый нижний угол
            elif i > half and j > half and j == size-1:
                row.append(True)           # правый нижний угол
            else:
                row.append(False)          # пусто
        pattern.append(row)
    return pattern

def make_small_swastika(block_size: int, fill_char: str = '#', empty_char: str = '.'):
    """
    Создаёт маленькую свастику размером block_size x block_size.
    Возвращает список строк (каждая строка — символы блока).
    """
    if block_size % 2 == 0 or block_size < 3:
        raise ValueError("Block size must be odd and >= 3")
    half = block_size // 2
    result = []
    for i in range(block_size):
        line = []
        for j in range(block_size):
            if i == half or j == half:
                line.append(fill_char)
            elif i < half and j < half and j == 0:
                line.append(fill_char)
            elif i < half and j > half and i == 0:
                line.append(fill_char)
            elif i > half and j < half and i == block_size-1:
                line.append(fill_char)
            elif i > half and j > half and j == block_size-1:
                line.append(fill_char)
            else:
                line.append(empty_char)
        result.append(''.join(line))
    return result

def make_empty_block(block_size: int, empty_char: str = '.'):
    """Создаёт пустой блок (все клетки заполнены empty_char)."""
    line = empty_char * block_size
    return [line] * block_size

def draw_swastika_of_swastikas(big_size: int, block_size: int,
                               fill_char: str = '#', empty_char: str = '.'):
    """
    Рисует большую свастику размером big_size x big_size блоков,
    где каждый блок — маленькая свастика (если блок принадлежит узору)
    или пустой блок (если не принадлежит).
    """
    # Шаг 1: определяем, какие блоки входят в большую свастику
    big_pattern = make_swastika_pattern(big_size)
    
    # Шаг 2: создаём маленькую свастику и пустой блок
    small_swastika = make_small_swastika(block_size, fill_char, empty_char)
    empty_block = make_empty_block(block_size, empty_char)
    
    # Шаг 3: собираем общую картинку
    for big_row in range(big_size):
        # Каждый блок имеет высоту block_size, поэтому выводим block_size строк
        for line_idx in range(block_size):
            big_line = []
            for big_col in range(big_size):
                if big_pattern[big_row][big_col]:
                    # Блок должен быть маленькой свастикой
                    big_line.append(small_swastika[line_idx])
                else:
                    # Пустой блок
                    big_line.append(empty_block[line_idx])
                if big_col < big_size - 1:
                    big_line.append(' ')   # разделитель между блоками
            print(''.join(big_line))
        if big_row < big_size - 1:
            print()   # разделитель между строками блоков

# Пример: большая свастика 5x5 из блоков размером 5x5 каждый
# Общий размер = 5 * 5 + (5-1) пробелов = 25 + 4 = 29 символов по ширине
draw_swastika_of_swastikas(big_size=5, block_size=5, fill_char='█', empty_char=' ')



