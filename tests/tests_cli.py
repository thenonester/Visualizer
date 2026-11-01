"""Тесты CLI-приложения."""

import unittest

from src.cli import (parse, valid, dep)


class TestParseArguments(unittest.TestCase):
    """Тесты парсинга аргументов."""

    def test_all_args(self):
        """Проверяет все параметры вместе."""
        args = parse(["--package", "One", "--source", "Two", "--test", "--depth", "3", "--filter", "Foru"])
        self.assertEqual(args["Package"], "One")
        self.assertTrue(args["Test"])
        self.assertEqual(args["Depth"], 3)

    def test_minimal_args(self):
        """Проверяет минимальный набор параметров."""
        args = parse(["--package", "pkg", "--source", "path"])
        self.assertEqual(args["Package"], "pkg")
        self.assertFalse(args["Test"])

    def test_missing_value(self):
        """Проверяет ошибку при отсутствии значения."""
        with self.assertRaises(ValueError):
            parse(["--package"])

    def test_unknown_argument(self):
        """Проверяет ошибку для неизвестного флага."""
        with self.assertRaises(ValueError):
            parse(["--unknown", "value"])


class TestValidateArguments(unittest.TestCase):
    """Тесты валидации аргументов."""

    def test_valid_args(self):
        """Проверяет валидные аргументы."""
        args = {"Package": "pkg", "Source": "path", "Test": False, "Depth": None, "Filter": None}
        valid(args)

    def test_missing_package(self):
        """Проверяет ошибку при отсутствии package."""
        args = {"Package": None, "Source": "path", "Test": False, "Depth": None, "Filter": None}
        with self.assertRaises(ValueError):
            valid(args)


class TestParseDepth(unittest.TestCase):
    """Тесты парсинга глубины."""

    def test_valid_depth(self):
        """Проверяет корректную глубину."""
        self.assertEqual(dep("5"), 5)

    def test_invalid_depth(self):
        """Проверяет ошибку для не-числа или <= 0."""
        with self.assertRaises(ValueError):
            dep("abc")
        with self.assertRaises(ValueError):
            dep("0")


if __name__ == "__main__":
    unittest.main()
