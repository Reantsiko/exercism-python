def is_pangram(sentence:str) -> bool:
    remaining = 'abcdefghijklmnopqrstuvwxyz'
    for letter in sentence.lower():
        if remaining.__contains__(letter):
            remaining = remaining.replace(letter,'')
    return len(remaining) is 0

