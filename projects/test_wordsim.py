from wordsim import *
import sys
import pytest

word_input = [
    'dog', 'cow', 'united', 'chinese', 'approach', 'alien'
]
word_output = [
    ['dogs', 'puppy', 'pet', 'cat', 'pup'],
    ['pig', 'sheep', 'goat', 'cattle', 'bull'],
    ['kingdom', 'america', 'country', 'britain', 'us'],
    ['korean', 'china', 'vietnamese', 'japanese', 'thai'],
    ['rather', 'perspective', 'methodology', 'understanding', 'however'],
    ['extraterrestrial', 'spaceship', 'ghost', 'creature', 'strange'],
]

analogy_input = [
    ['king', 'queen', 'man'],
    ['apple', 'tree', 'seed'],
    ['hammer', 'nail', 'comb'],
    ['dog', 'puppy', 'cat'],
    ['like', 'love', 'dislike']
]
analogy_output = [
    ['woman', 'girl', 'lady', 'wonder', 'guy'],
    ['tree', 'leaf', 'planting', 'plant', 'seedling'],
    ['nail', 'manicure', 'hair', 'cuticle', 'brush'],
    ['kitten', 'puppy', 'pup', 'kitty', 'pug'],
    ['love', 'adore', 'hate', 'liking', 'loathe']
]


@pytest.fixture(params=list(range(len(word_input))))
def word_idx(request):
    return request.param

def test_similar_words(word_idx):
    closest = closest_words(gloves, word_input[word_idx].lower(), 5)
    # assert sorted(closest) == sorted(word_output[word_idx])
    assert closest == word_output[word_idx]


@pytest.fixture(params=list(range(len(analogy_input))))
def analogy_idx(request):
    return request.param


def test_analogies(analogy_idx):
    analogs = analogies(gloves, analogy_input[analogy_idx][0].lower(),
                        analogy_input[analogy_idx][1].lower(),
                        analogy_input[analogy_idx][2].lower(), 5)
    # assert sorted(analogs) == sorted(analogy_output[analogy_idx])
    assert analogs == analogy_output[analogy_idx]


# Must be run like `python -m pytest -v test_wordsim.py ~/data`
glove_dirname = sys.argv[3]  # must pass in dir with .npy and .vocab.txt files
gloves = load_glove(glove_dirname)