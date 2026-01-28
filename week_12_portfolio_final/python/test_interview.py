import unittest
from interview_python import *


class TestInterviewQuestions(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("Hello"))

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test_word_frequency(self):
        text = "banco de dados dados"
        expected = {"banco": 1, "de": 1, "dados": 2}
        self.assertEqual(word_frequency(text), expected)

    def test_flatten_list(self):
        self.assertEqual(flatten_list([1, [2, [3, 4], 5]]), [1, 2, 3, 4, 5])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 1]), [1, 2, 3])

    def test_find_missing_number(self):
        self.assertEqual(find_missing_number([1, 2, 4, 5]), 3)

    def test_extract_emails(self):
        text = "Contato: matheus@email.com ou teste@dados.br"
        expected = ["matheus@email.com", "teste@dados.br"]
        self.assertEqual(extract_emails(text), expected)

    def test_merge_dicts(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        self.assertEqual(merge_dicts(d1, d2), {"a": 1, "b": 2})

    def test_generator(self):
        gen = even_number_generator(4)
        self.assertEqual(list(gen), [0, 2, 4])


if __name__ == "__main__":
    unittest.main()
