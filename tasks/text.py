import re
from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    text = text.strip()
    gr = re.split(r"\s+", text)
    gr = sorted(gr, key = len)
    print(len(gr))
    print(gr)
    if len(gr) == 0 or len(gr) == 1: 
        return (None, None)
    else: 
        return (gr[0], gr[-1])

