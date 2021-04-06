import os
from typing import Dict


Mappings = Dict[str, str]

numbers: Mappings = {
   '0': '०',
   '1': '१',
   '2': '२',
   '3': '३',
   '4': '४',
   '5': '५',
   '6': '६',
   '7': '७',
   '8': '८',
   '9': '९'
}

basic_vowels: Mappings = {
    'a': 'अ',
    'aa': 'आ',
    'ee': 'ई ',
    'i': 'इ',
    'u': 'उ',
    'oo': 'ऊ',
    'Ri': 'ॠ ',
    'Ree': 'ॠ',
    'e': 'ए',
    'ai': 'ऐ',
    'o': 'ओ',
}

consonant_kaars: Mappings = {
    'aa': 'ा',
    'e': 'े',
    'ee': 'ी',
    'i': 'ि',
    'u': 'ु',
    'oo': 'ू',
    'o': 'ो',
    'au': 'ौ',
    'ai': 'ै'
}

akaars: Mappings = {
    'ka': 'क',
    'kha': 'ख',
    'ga': 'ग',
    'gha': 'घ',
    'Nga': 'ङ',
    'NGa': 'ङ्ग',
    'cha': 'च',
    'chha': 'छ',
    'ja': 'ज',
    'jha': 'झ',
    'yNa': 'ञ',
    'Ta': 'ट',
    'Tha': 'ठ',
    'Da': 'ड',
    'Dha': 'ढ',
    'Na': 'ण',
    'ta': 'त',
    'tha': 'थ',
    'da': 'द',
    'dha': 'ध',
    'na': 'न',
    'nga': 'ङ',
    'pa': 'प',
    'pha': 'फ',
    'fa': 'फ',
    'ba': 'ब',
    'bha': 'भ',
    'va': 'भ',
    'ma': 'म',
    'ya': 'य',
    'ra': 'र',
    'la': 'ल',
    'wa': 'व',
    'sa': 'स',
    'sha': 'श',
    'Sha': 'ष',
    'ha': 'ह',
    'ksha': 'क्ष',
    'tra': 'त्र',
    'gya': 'ज्ञ',
    'gYa': 'ग्य',
}

halanta = '्'
amkaar = 'ं'
aNNkaar = 'ँ'
Ri = 'ृ'


def get_mappings() -> Mappings:
    all_mappings: Mappings = {
        **basic_vowels,
        **akaars,
    }
    assert len(all_mappings) == len(basic_vowels) + len(akaars)

    # create halanta maps
    halantas = {k[:-1]: v+halanta for k, v in akaars.items()}

    all_mappings.update(halantas)
    assert len(all_mappings) == len(basic_vowels) + 2 * len(akaars)

    curr_key_counts = len(all_mappings)
    for rom, sym in consonant_kaars.items():
        kaar_maps = {k+rom : akaars[k+'a'] + sym for k in halantas}
        all_mappings.update(kaar_maps)
        assert len(all_mappings) == curr_key_counts + len(halantas)
        curr_key_counts += len(halantas)

    # add purnabiram
    all_mappings['.'] = '।'
    # add numbers
    all_mappings.update(numbers)
    return dict(sorted(all_mappings.items(), key=lambda x: len(x[0]), reverse=True))


def get_word_maps() -> Mappings:
    maps: Mappings = {}
    filepath = os.path.join(
        os.path.dirname(__file__),
        'word_maps.txt'
    )
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if not line.strip():
                continue
            w, uni = line.split()
            maps[w] = uni
    return maps


# TODO: include these as well
map_str = '''
gy ग्य् ज्ञ्
gya ज्ञ ग्या
'''

if __name__ == '__main__':
    all_maps = get_mappings()
    print(all_maps)
