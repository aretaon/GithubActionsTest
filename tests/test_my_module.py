import unittest
from unittest.mock import patch, Mock
from mypackage.my_testfile import a_function_with_R


class TestMyPackage(unittest.TestCase):
    @patch('subprocess.run')
    def test_a_function_with_R_happy_path(self, mock_run):
        mock_process = Mock()
        mock_process.stdout.strip.return_value = 'Hello World'
        mock_run.return_value = mock_process

        result = a_function_with_R('Hello World')

        self.assertEqual(result, '[1] "Hello World"')

    @patch('subprocess.run')
    def test_a_function_with_R_empty_string(self, mock_run):
        mock_process = Mock()
        mock_process.stdout.strip.return_value = ''
        mock_run.return_value = mock_process

        result = a_function_with_R('')

        self.assertEqual(result, '[1] ""')


if __name__ == '__main__':
    unittest.main()
