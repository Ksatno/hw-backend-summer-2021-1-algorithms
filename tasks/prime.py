__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number == 0 or number == 1: return False
    if number == 2: return True
    for i in range(2, number, 1):
        print(i)
        if number % i == 0: return False
    return True
