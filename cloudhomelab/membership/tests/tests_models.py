from django.test import TestCase

from membership.models import *

class TextilesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Textiles.objects.create(first_name='Big', last_name='Bob')

    def test_brand(self):
        Textiles = Textiles.objects.get(id=1)
        field_label = Textiles._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_product_model(self):
        Textiles = Textiles.objects.get(id=1)
        field_label = Textiles._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'died')

    def test_material_type(self):
        Textiles = Textiles.objects.get(id=1)
        max_length = Textiles._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_price(self):
        Textiles = Textiles.objects.get(id=1)
        expected_object_name = f'{Textiles.last_name}, {Textiles.first_name}'
        self.assertEqual(str(Textiles), expected_object_name)

    def test_pic(self):
        Textiles = Textiles.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(Textiles.get_absolute_url(), '/catalog/Textiles/1')
