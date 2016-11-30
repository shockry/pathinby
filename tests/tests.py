import os
import sys
import unittest
import tempfile
import shutil
import collections
sys.path.insert(0, os.path.abspath('..'))
import pypath


class TestLineFormatting(unittest.TestCase):
    def test_format_line(self):
        self.assertEqual(pypath.format_line('|', '|-', 'foo', 0), '|-foo')
        self.assertEqual(pypath.format_line('|', '|-', 'foo', 1), '| |-foo')
        self.assertEqual(pypath.format_line('|', '|-', '', 0), '|-')
        self.assertEqual(pypath.format_line('', '=>', 'bar', 2), '  =>bar')


class PathArrayTestCase(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()

    def test_create_path_empty_directory(self):
        actual = pypath.create_path(self.d, None, '|', '|-')
        expected = []

        self.assertEqual(actual, expected)

    def test_create_path_one_file(self):
        file = tempfile.NamedTemporaryFile(dir=self.d, delete=False)

        actual = pypath.create_path(self.d, None, '|', '|-')
        expected = ['|-'+os.path.basename(file.name)]

        self.assertEqual(actual, expected)

    def test_create_path_multiple_files(self):
        file1 = tempfile.NamedTemporaryFile(dir=self.d, delete=False)
        file2 = tempfile.NamedTemporaryFile(dir=self.d, delete=False)

        actual = collections.Counter(pypath.create_path(self.d, None, '|', '|-'))
        expected = collections.Counter(
                       ['|-'+os.path.basename(file1.name),
                        '|-'+os.path.basename(file2.name)
                        ]
                   )

        self.assertEqual(actual, expected)

    def test_create_path_multiple_directories(self):
        file1 = tempfile.NamedTemporaryFile(dir=self.d, delete=False)
        d2 = tempfile.mkdtemp(dir=self.d)
        file2 = tempfile.NamedTemporaryFile(dir=d2, delete=False)

        actual = collections.Counter(pypath.create_path(self.d, None, '|', '|-'))
        expected = collections.Counter(
                       ['|-'+os.path.basename(file1.name),
                        '|-'+os.path.basename(d2),
                        '| |-'+os.path.basename(file2.name)
                        ]
                   )

        self.assertEqual(actual, expected)

    def test_output_file(self):
        file1 = tempfile.NamedTemporaryFile(dir=self.d, delete=False)
        file2 = tempfile.NamedTemporaryFile(dir=self.d, delete=False)
        outputFile = tempfile.NamedTemporaryFile(dir=self.d, delete=False)

        fileObject = open(outputFile.name, 'r+w')
        pypath.create_path(self.d, fileObject, '|', '|-')

        with open(outputFile.name, 'r') as file:
            actual = collections.Counter(file.read())

        expected = collections.Counter(
                    '\n'.join(
                        ['|-'+os.path.basename(file1.name),
                         '|-'+os.path.basename(file2.name),
                         '|-'+os.path.basename(outputFile.name)
                         ]
                    )
                   )

        self.assertEqual(actual, expected)

    def tearDown(self):
        shutil.rmtree(self.d)

if __name__ == '__main__':
    unittest.main()
