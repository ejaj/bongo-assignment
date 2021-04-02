import sys
import os
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from task.task_2 import print_depth, Person


class TestTask2:
    """
    A class to represent a TestTask2.
    """

    @pytest.fixture
    def person_a(self):
        """
        :return person_a Object:
        """
        return Person("Kazi", "Sadikul", None)

    @pytest.fixture
    def person_b(self, person_a):
        """
        :param person_a:
        :return person_b Object:
        """
        return Person("Alif", "Ahmed", person_a)

    def test_empty(self, capsys):
        """
        Test empty dictionary and capturing of writes to sys.stdout and sys.stderr.
        :param capsys:
        :return:
        """
        data = {}
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == ""
        assert err == ""

    def test_one_depth(self, capsys):
        """
        Test one key depth dictionary and capturing of writes to sys.stdout and sys.stderr.
        :param capsys:
        :return:
        """
        a = {
            "key1": 1
        }
        print_depth(a)
        out, err = capsys.readouterr()
        assert out == "key1 1\n"
        assert err == ""

    def test_two_depth(self, capsys):
        """
        Test two key depth dictionary and capturing of writes to sys.stdout and sys.stderr.
        :param capsys:
        :return:
        """
        a = {
            "key1": {
                "key2": 1
            }
        }
        print_depth(a)
        out, err = capsys.readouterr()
        assert out == (
            "key1 1\n"
            "key2 2\n"
        )
        assert err == ""

    def test_more_depth(self, capsys):
        """
        Test nested key depth dictionary and capturing of writes to sys.stdout and sys.stderr.
        :param capsys:
        :return:
        """
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        print_depth(a)
        out, err = capsys.readouterr()
        assert out == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
        )
        assert err == ""

    def test_single_person(self, capsys, person_a):
        """
        Test single person key depth and capturing of writes to sys.stdout and sys.stderr.
        :param capsys:
        :param person_a:
        :return:
        """
        print_depth(person_a)
        out, err = capsys.readouterr()
        assert out == (
            "Kazi 1\n"
            "Sadikul 1\n"
            "None 1\n"
        )
        assert err == ""

    def test_nested_person(self, capsys, person_b):
        """
        Test nested person key depth and capturing of writes to sys.stdout and sys.stderr.
        :param capsys:
        :param person_b:
        :return:
        """
        print_depth(person_b)
        out, err = capsys.readouterr()
        assert out == (
            "Alif 1\n"
            "Ahmed 1\n"
            "Kazi Sadikul 1\n"
            "Kazi 2\n"
            "Sadikul 2\n"
            "None 2\n"
        )
        assert err == ""

    def test_complex_data(self, capsys, person_b):
        """
         Test complex data key depth and capturing of writes to sys.stdout and sys.stderr.
        :param capsys:
        :param person_b:
        :return:
        """
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b,
                }
            },
        }
        print_depth(data)
        out, err = capsys.readouterr()
        assert out == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
            "user 3\n"
            "Alif 4\n"
            "Ahmed 4\n"
            "Kazi Sadikul 4\n"
            "Kazi 5\n"
            "Sadikul 5\n"
            "None 5\n"
        )
        assert err == ""
