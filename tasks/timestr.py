__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    Flag = False
    string = ""
    days = seconds//86400
    if (days) != 0 or Flag:
        string = string + f'{days:02}' + 'd'
        seconds = seconds - (days*86400)
        Flag = True
    
    hours = seconds//3600
    if (hours) != 0 or Flag:
        string = string + f'{hours:02}' + 'h'
        seconds = seconds - (hours*3600)
        Flag = True
    
    minutes = seconds//60
    if (minutes) != 0 or Flag:
        string = string + f'{minutes:02}' + 'm'
        seconds = seconds - (minutes*60)
        Flag = True
    
    string = string + f'{seconds:02}' + 's'
    return string








