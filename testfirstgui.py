import unittest

from first_gui import MainWindow


class TestFirstGui(unittest.TestCase):
    window = MainWindow()

    def test_flip_the_line(self):
        line = '123457890'
        a_line = line[::-1]
        msg = f'Вместо {line}, должно быть {a_line}!'
        self.assertEqual(self.window.flip_the_line(line), a_line, msg=msg)


if __name__ == '__main__':
    unittest.main()
