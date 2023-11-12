from abc import ABC, abstractmethod
import string
import random
from typing import List

import nltk

class PasswordGenerator(ABC) :
    def __init__(self) :
        pass
    
    @abstractmethod
    def generate_password(self) :
        pass

class PinPassword(PasswordGenerator) :
    def __init__(self, length:int = 8) :
        self.length = length
        self.numbers = string.digits
        
    def generate_password(self) :
        chosen_chars = [random.choice(self.numbers) for _ in range(self.length)]
        random.shuffle(chosen_chars)
        return "".join(chosen_chars)
    
class RandomPasswordGenerator(PasswordGenerator): 
    def __init__(
        self,
        length:int = 8,
        include_number:bool = True,
        include_symbol:bool = True,
    ):
        self.length = length
        # the chars we are allowed to use during creation of a new password
        self.characters = string.ascii_letters\
            + (string.digits if include_number else '')\
            + (string.punctuation if include_symbol else '')
    
    def generate_password(self):
        chosen_chars = [random.choice(self.characters) for _ in range(self.length)]
        random.shuffle(chosen_chars)
        return ''.join(chosen_chars)
    

class RememberablePasswordGenerator(PasswordGenerator) :
    def __init__(self,
        length:int = 8,
        *,
        word_list: List[str] = None,
        separator:str = '-'
    ):
        self.length = length
        self.separator = separator
        self.word_list = nltk.corpus.words.words() if not word_list else word_list

    @staticmethod
    def word_list_validator(word_list) :
        for word in word_list :
            if ' ' in word :
                raise ValueError(f"The words should not contain space between them: {word}")
        return True

    def generate_password(self):
        chosen_words = [random.choice(self.word_list) for _ in range(self.length)]
        self.word_list_validator(chosen_words)
        random.shuffle(chosen_words)
        return self.separator.join(chosen_words)
