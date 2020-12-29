"""Начало программы."""
import unittest



class Test(object):
    """
    >>> a=Test(5)
    >>> a.multiply_by_2()
    10
    """

    def __init__(self, cabinet):
        """метод для кабинета чтобы потом умножить на 2."""
        self._cabinet = cabinet

    def multiply_by_2(self):
        """умножение на 2."""
        return self._cabinet * 2

if __name__ == "__main__":
    import doctest
    doctest.testmod()


class TestUM(unittest.TestCase):
    """Создание класса для тестирования unittest."""

    def test_upper(self):
        """Проверка на то что текст выводится большими буквами."""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_split(self):
        """Проверка что разделитель - запятая."""
        sss = 'hello world'
        self.assertEqual(sss.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            sss.split(2)

    def test_numbers_3_4(self):
        """Умножение цифр."""
        self.assertEqual(3 * 4, 12)

    def test_strings_a_3(self):
        """Вывод N букв."""
        self.assertEqual('a' * 3, 'aaa')


if __name__ == '__main__':
    unittest.main()


class Pacient:
    """Система регистратуры больницы."""

    def __init__(self, doctor, cabinet):
        """Врач и его кабинет."""
        self.doctor = doctor
        self.cabinet = cabinet
        self.dates = {}

    def reserv(self, date, cabinet):
        """Резервация даты по расписанию."""
        reserved = self.dates[date]
        if cabinet + reserved > self.cabinet:
            raise Exception
        else:
            self.dates[date] = reserved + cabinet


class Recording:
    """Запись ко врачу."""

    NEW = "New"
    RESERVED = "Reserved"
    PERFORMED = "Performed"
    CANCELED = "Canceled"

    def __init__(self, diagnosis, date, cabinet, pacient):
        """Итоговая информация о приёме."""
        self.diagnosis = diagnosis
        self.date = date
        self.cabinet = cabinet
        self.pacient = pacient
        self.state = Recording.NEW

    def reserv(self):
        """Запись."""
        if self.state == Recording.NEW:
            try:
                self.pacient.reserv()
                self.state = Recording.RESERVED
            except:
                raise Exception
        else:
            raise Exception


class System:
    """Какому пациенту в какой кабинет."""

    u1 = "Pacient №52352"
    u2 = "Pacient №99491"
    u3 = "Pacient №1951"

    rc1 = Pacient(u1, 23)
    rc2 = Pacient(u2, 260)
    rc3 = Pacient(u3, 424)

    recordings = []

    def recording(self, pacient, diagnosis, date, cabinet):
        """."""
        new_recording = Recording(diagnosis, pacient, date, cabinet)
        self.recordings.append(new_recording)

    def reserv(self, recording):
        """."""
        recording.reserv()
