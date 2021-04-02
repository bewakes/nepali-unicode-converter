from dataclasses import dataclass
from typing import List, TypeVar, Tuple

from nepali_unicode_converter.mappings import (
    get_mappings,
    consonant_kaars,
    get_word_maps,
    Mappings,
    amkaar,
    aNNkaar,
    Ri,
)


@dataclass
class State:
    remaining: str = ''
    consumed: str = ''
    processed: str = ''
    as_is: bool = False

    def copy(self, **kwargs):
        return State(self.remaining, self.consumed, self.processed, **kwargs)


class Converter:
    def __init__(self):
        self.mappings = get_mappings()
        self.word_maps = get_word_maps()

    def consume(self, state: State) -> State:
        current = state.remaining
        consumed = state.consumed
        processed = state.processed

        if state.as_is and current[0] == '}':
            return State(current[1:], consumed + current[:1], processed, False)
        if state.as_is and current[0] != '}':
            return State(current[1:], consumed + current[0], processed + current[0], True)

        # check for escape sequences
        if current.startswith('{{'):
            return State(current[2:], consumed + current[:2], processed+'{')
        if current.startswith('{') and not state.as_is:
            return State(
                current[1:],
                consumed + current[:1],
                processed,
                True
            )
        # Check if word is in direct word mappings
        for k, v in self.word_maps.items():
            if current.startswith(k):
                return State(
                    current[len(k):],
                    consumed + current[:len(k)],
                    processed + v
                )

        # add amkar and aaNkar
        if current.startswith('M'):
            return State(current[1:], consumed + current[0], processed + amkaar)
        if current.startswith('NN'):
            return State(current[2:], consumed + current[:2], processed + aNNkaar)

        # Special case for Ri and Ree
        if current.startswith('RI') and consumed[-1] != 'a':
            # remove halanta and add Ri
            return State(current[2:], consumed + current[:2], processed[:-1] + Ri)
        if current.startswith('RI') and consumed[-1] == 'a':
            # normal proceeding
            return State(current[2:], consumed + current[:2], processed + Ri)

        for k, v in self.mappings.items():
            if current.startswith(k):
                return State(current[len(k):], consumed + current[:len(k)], processed+v)
        else:
            # TODO: what if upper case and does not match any pattern?
            # In that case try lower casing char by char
            return State(current[1:], consumed + current[0], processed+current[0])

    def convert(self, text: str) -> str:
        if not text:
            return text
        state = State(text)
        while state.remaining:
            state = self.consume(state)
        return state.processed
