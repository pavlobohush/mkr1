import pytest
from word_sentence_counter import count_words_and_sentences

@pytest.fixture
def sample_text_file(tmp_path):
    file_content = "This is a sample text. It contains three sentences! Isn't that great?"
    file_path = tmp_path / "text.txt"
    with open(file_path, 'w') as f:
        f.write(file_content)
    return file_path

def test_count_words_and_sentences(sample_text_file):
    expected_word_count = 11
    expected_sentence_count = 3
    word_count, sentence_count = count_words_and_sentences(sample_text_file)
    assert word_count == expected_word_count
    assert sentence_count == expected_sentence_count

import pytest
from word_sentence_counter import count_words_and_sentences

@pytest.fixture
def sample_text(tmp_path):
    file_path = tmp_path / "test.txt"
    with open(file_path, "w") as file:
        file.write("This is a sample sentence. Another sentence follows!")

    return file_path

def test_count_words_and_sentences(sample_text):
    word_count, sentence_count = count_words_and_sentences(sample_text)
    assert word_count == 8
    assert sentence_count == 2

def test_count_words_and_sentences_empty_file(tmp_path):
    file_path = tmp_path / "empty.txt"
    with open(file_path, "w") as file:
        file.write("")

    word_count, sentence_count = count_words_and_sentences(file_path)
    assert word_count == 0
    assert sentence_count == 0

def test_count_words_and_sentences_no_sentences(tmp_path):
    file_path = tmp_path / "no_sentences.txt"
    with open(file_path, "w") as file:
        file.write("This is a sample text with no sentences")

    word_count, sentence_count = count_words_and_sentences(file_path)
    assert word_count == 7
    assert sentence_count == 0
