import string
import random
from typing import List

import nltk

def generate_pin_password(length: int = 8) -> str:
    numbers = string.digits
    chosen_chars = [random.choice(numbers) for _ in range(length)]
    random.shuffle(chosen_chars)
    return "".join(chosen_chars)

def generate_random_password(
    length: int = 8, include_number: bool = True, include_symbol: bool = True
) -> str:
    characters = (
        string.ascii_letters
        + (string.digits if include_number else "")
        + (string.punctuation if include_symbol else "")
    )
    chosen_chars = [random.choice(characters) for _ in range(length)]
    random.shuffle(chosen_chars)
    return "".join(chosen_chars)

def generate_rememberable_password(
    length: int = 8,
    word_list: List[str] = None,
    separator: str = "-",
) -> str:
    def word_list_validator(word_list: List[str]) -> bool:
        for word in word_list:
            if " " in word:
                raise ValueError(f"The words should not contain space between them: {word}")
        return True
    word_list = nltk.corpus.words.words() if word_list is None else word_list
    chosen_words = [random.choice(word_list) for _ in range(length)]
    word_list_validator(chosen_words)
    random.shuffle(chosen_words)
    return separator.join(chosen_words)

if __name__ == "__main__" :
    pin_password = generate_pin_password()
    random_password = generate_random_password()
    rememberable_password = generate_rememberable_password()
