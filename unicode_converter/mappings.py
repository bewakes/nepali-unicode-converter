from typing import List, Dict

Mappings = Dict[str, str]

basic_vowels = {
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
    'aum': 'ॐ',
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
    'cha': 'च',
    'chha': 'छ',
    'ja': 'ज',
    'jha': 'झा',
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


    return dict(sorted(all_mappings.items(), key=lambda x: len(x[0]), reverse=True))


def get_word_maps() -> Mappings:
    maps: Mappings = {}
    with open('word_maps.txt', 'r') as f:
        for line in f.readlines():
            if not line.strip():
                continue
            w, uni = line.split()
            maps[w] = uni
    return maps

map_str = '''
ng ङ् ङ्ग
gy ग्य् ज्ञ्
gya ज्ञ ग्या
'''

if __name__ == '__main__':
    all_maps = get_mappings()
    # print(all_maps)
