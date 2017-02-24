from HW4 import clean_sentence
from HW4 import get_rand_word
from HW4 import get_words_min_max_length


def test_clean_sentence_nochange():
    assert clean_sentence('abcdef') == 'abcdef'


def test_clean_sentence_change():
    assert clean_sentence("A/B/c@deF") == 'abcdef'


def test_get_rand_word():
    assert get_rand_word(['apple', 'banana', 'crocodile', 'baseball', 'foot'])


def test_get_words_easy():
    assert get_words_min_max_length(['pear', "racecar", "tarantula"], 4, 6) == ['pear']


def test_get_words_medium():
    assert get_words_min_max_length(['pear', 'racecar', 'tarantula'], 6, 8) == ['racecar']


def test_get_words_hard():
    assert get_words_min_max_length(['pear', 'racecar', 'tarantula'], 8, 99) == ['tarantula']


test_clean_sentence_change()
test_clean_sentence_nochange()
test_get_rand_word()
test_get_words_easy()
test_get_words_medium()
test_get_words_hard()
print('All of the tests ran successfully')
