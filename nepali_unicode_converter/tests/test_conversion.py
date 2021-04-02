from nepali_unicode_converter.convert import Converter


test_cases = [
    ('gaahro', 'गाह्रो'),
    ('aaNNkhaa', 'आँखा'),
    ('samRIddha', 'समृद्ध'),
    ('samaRIddha', 'समृद्ध'),
    ('garyo', 'गर्यो'),
    ('hudai', 'हुँदै'),
    ('mero instagram', 'मेरो इन्स्टाग्राम'),
    ('aum nama: shiwaaya', 'ॐ नम: शिवाय'),
    ('kaam chhaina timro, haNN?', 'काम् छैन तिम्रो, हँ?'),
    ('messengermaa message aayo', 'मेसेन्जरमा मेसेज आयो'),
    ('aNDaa', 'अण्डा'),
    ('kaMsha', 'कंश'),
    ('aNNgaara', 'अँगार'),
    ('yuNNs', 'युँस्'),
    ('agyaanee', 'अज्ञानी'),
    ('gYaarej', 'ग्यारेज्'),
    ('ma RiShi ho.', 'म ॠ षि हो।'),
    ('ma {in} gYaarej', 'म in ग्यारेज्'),
    ('ma {{in} gYaarej', 'म {इन्} ग्यारेज्'),
    ('ma {{{in}} gYaarej', 'म {in} ग्यारेज्'),
    # TODO: figure out what to do with the next case
    # ('ma {inside {of} the } gYaarej', 'म inside {of}  ग्यारेज्'),
]

def test_conversion():
    converter = Converter()
    for roman, expected in test_cases:
        assert converter.convert(roman) == expected
