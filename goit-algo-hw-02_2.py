from collections import deque

def is_palindrome(string):
    # Перетворення рядка у нижній регістр і видалення пробілів
    string = string.lower().replace(" ", "")
    
    # Створення двосторонньої черги
    char_queue = deque()
    
    # Додавання символів рядка до черги
    for char in string:
        char_queue.append(char)
    
    # Порівняння символів з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    return True