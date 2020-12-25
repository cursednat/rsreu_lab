import unittest
class Test(object):
    """
    >>> a=Test(5)
    >>> a.multiply_by_2()
    10
    """

    def __init__(self, cabinet):
        self._cabinet = cabinet

    def multiply_by_2(self):
        return self._cabinet * 2

if __name__ == "__main__":
    import doctest
    doctest.testmod()

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def test_numbers_3_4(self):
        self.assertEqual(3 * 4, 12)

    def test_strings_a_3(self):
        self.assertEqual('a' * 3, 'aaa')


if __name__ == '__main__':
    unittest.main()
class Pacient:
    '''Система регистратуры больницы'''
    def __init__(self, doctor, cabinet):
        self.doctor = doctor
        self.cabinet = cabinet
        self.dates = {}

    def reserv(self, date, cabinet):
        reserved = self.dates[date]
        if cabinet + reserved > self.cabinet:
            raise Exception
        else:
            self.dates[date] = reserved + cabinet

class Recording:
    NEW = "New"
    RESERVED = "Reserved"
    PERFORMED = "Performed"
    CANCELED = "Canceled"

    def __init__(self, diagnosis, date, cabinet, pacient):
        self.diagnosis = diagnosis #town
        self.date = date
        self.cabinet = cabinet
        self.pacient = pacient
        self.state = Recording.NEW

    def reserv(self):
        if self.state == Recording.NEW:
            try:
                self.pacient.reserv()
                self.state = Recording.RESERVED
            except:
                raise Exception
        else:
            raise Exception

class System:
    u1 = "Pacient №52352"
    u2 = "Pacient №99491"
    u3 = "Pacient №1951"

    rc1 = Pacient(u1, 23)
    rc2 = Pacient(u2, 260)
    rc3 = Pacient(u3, 424)

    recordings = []

    def recording(self, pacient, diagnosis, date, cabinet):
        new_recording = Recording(diagnosis, pacient, date, cabinet)
        self.recordings.append(new_recording)

    def reserv(self, recording):
        recording.reserv()

python3 - m
pycodestyle
var = __init__.py
