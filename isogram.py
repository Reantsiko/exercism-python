def is_isogram(string:str) -> bool:
    has_appeared = ''
    for letter in string.lower():
        if letter is not ' ' and letter is not '-' and has_appeared.__contains__(letter):
            return False
        has_appeared = has_appeared.__add__(letter)
    return True
