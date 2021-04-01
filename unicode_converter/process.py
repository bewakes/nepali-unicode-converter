from typing import List, TypeVar, Tuple

from mappings import get_mappings, consonant_kaars, get_word_maps, Mappings


State = Tuple[str, List[str]]


class Converter:
    def __init__(self, mappings, word_maps):
        self.mappings = mappings
        self.word_maps = word_maps

    def consume(self, state: State) -> State:
        current, processed = state

        for k, v in self.mappings.items():
            if current.startswith(k):
                return (current[len(k):], processed+v)
        else:
            return current[1:], processed+current[0]


    def process_word(self, word: str) -> str:
        word = word.replace(' ', '')
        # Check if word is in direct word mappings
        for k, v in self.word_maps.items():
            if word.startswith(k):
                return self.word_maps[k] + self.process_word(word[len(k):])

        state: State = (word, '')
        current, processed = state
        while current:
            current, processed = self.consume((current, processed))
        return processed


    def convert(self, text: str) -> List[str]:
        words = text.strip().split()
        return [self.process_word(word) for word in words]



if __name__ == '__main__':
    texts = [
        'hajurabuwaale',
        'bhannubhayo',
        'besmaree',
        'panDit',
        'gahro',
        'hudai',
        'chha',
        'instagram',
        'mero naam bibek aum',
        'kaam chhaina timro haN?',
        'googlele',
        'messengermaa message aayo',
        'gurungsenee',
        'e',
        'timee kina hola yastee bhaakee?'
    ]
    converter = Converter(get_mappings(), get_word_maps())
    for text in texts[:]:
        print(converter.convert(text))
