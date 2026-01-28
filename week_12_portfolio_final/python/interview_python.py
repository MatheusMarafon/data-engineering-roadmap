import re
from collections import Counter


# 1. Inverter Strings
def reverse_string(s):
    return s[::-1]


# 2. Palíndromo
def is_palindrome(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


# 3. FizzBuzz
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.appen("Buzz")
        else:
            result.append(str(i))
    return result


# 4. Frequência de Palavras
def word_frequency(text):
    words = text.lower().split()
    return dict(Counter(words))


# 5. Achatamento de Lista
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


# 6. Remover Duplicatas
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
        return result


# 7. encontrar o Número Faltante
def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# 8. Extrair Emails
def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)


# 9. Merge de Dicionários
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged


# 10. Gerador de Números Pares
def even_number_generator(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i
