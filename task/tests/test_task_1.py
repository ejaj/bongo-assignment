import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from task.task_1 import print_depth


class TestTask1:
    """
      A class to represent a TestTask1.
    """

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
