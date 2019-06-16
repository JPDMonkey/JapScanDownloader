import sys, os

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../japscandownloader/')
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import unittest

from helpers import helper_format

import numpy
from PIL import Image

class TestFormat(unittest.TestCase):
    chapter = os.path.join('.', 'tests', 'test_chapter')
    image_number = 10

    def setUp(self):
        self.image_files = []

        if not os.path.exists(self.chapter):
            os.makedirs(self.chapter)

        for image_index in range(0, self.image_number):
            image_array = numpy.random.rand(500, 500, 3) * 255
            image = Image.fromarray(image_array.astype('uint8')).convert('RGBA')
            image_full_path = os.path.join('.', 'tests', 'test_chapter', ('temp_%s.png' % (image_index)))
            self.image_files.append(image_full_path)
            image.save(image_full_path)

    def test_format_pdf(self):
        self.file_name = os.path.join('.', 'tests', 'test_chapter', 'test_chapter.pdf')

        helper_format.create_pdf(self.chapter, self.file_name, self.image_files)

        self.assertGreater(os.path.getsize(self.file_name), 0)

    def test_format_cbz(self):
        self.file_name = os.path.join('.', 'tests', 'test_chapter', 'test_chapter.cbz')

        helper_format.create_cbz(self.chapter, self.file_name, self.image_files)

        self.assertGreater(os.path.getsize(self.file_name), 0)

    def tearDown(self):
        for image_file in self.image_files:
            os.remove(image_file)

        os.remove(self.file_name)
