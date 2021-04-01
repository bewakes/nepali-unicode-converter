from typing import List, TypeVar, Tuple

from mappings import get_mappings, consonant_kaars, get_word_maps, Mappings, amkaar, aNNkaar, Ri


State = Tuple[str, str, str]


class Converter:
    def __init__(self, mappings, word_maps):
        self.mappings = mappings
        self.word_maps = word_maps

    def consume(self, state: State) -> State:
        consumed, current, processed = state

        # add amkar and aaNkar
        if current.startswith('M'):
            return (consumed + current[0], current[1:], processed + amkaar)
        if current.startswith('NN'):
            return (consumed + current[:2], current[2:], processed + aNNkaar)

        # Special case for Ri and Ree
        if current.startswith('RI') and consumed[-1] != 'a':
            # remove halanta and add Ri
            return (consumed + current[:2], current[2:], processed[:-1] + Ri)
        if current.startswith('RI') and consumed[-1] == 'a':
            # normal proceeding
            return (consumed + current[:2], current[2:], processed + Ri)

        for k, v in self.mappings.items():
            if current.startswith(k):
                return (consumed + current[:len(k)], current[len(k):], processed+v)
        else:
            # TODO: what if upper case and does not match any pattern?
            # In that case try lower casing char by char
            return consumed + current[0], current[1:], processed+current[0]

    def process_word(self, word: str) -> str:
        word = word.replace(' ', '')
        if not word:
            return ''
        # Check if word is in direct word mappings
        for k, v in self.word_maps.items():
            if word.startswith(k):
                return self.word_maps[k] + self.process_word(word[len(k):])

        state: State = ('', word, '')
        while True:
            state = self.consume(state)
            consumed, current, processed = state
            if not current:
                break
        return processed

    def convert(self, text: str) -> List[str]:
        words = text.strip().split()
        return [self.process_word(word) for word in words]

# TODO: GYAAS, etc


if __name__ == '__main__':
    texts = [
        'gaahro',
        'aaNNkhaa',
        'samRIddha',
        'garyo',
        'hudai',
        'instagram',
        'aum nama: shiwaaye',
        'kaam chhaina timro, haNN?',
        'messengermaa message aayo',
        'aNDaa',
        'kaMsha',
        'aNNgaara',
        'yuNNs',
        'ma RiShi ho .',
    ]
    converter = Converter(get_mappings(), get_word_maps())
    for text in texts[:]:
        print(converter.convert(text))
