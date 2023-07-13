from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='Ice Cream', price=12, inventory=10)
        self.assertEqual(item, 'Ice Cream : 12')