from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='Ice Cream', price=12, inventory=10)
        self.assertEqual(item.get_item(), 'Ice Cream : 12')
        self.assertEqual(item.title, 'Ice Cream')
        self.assertEqual(item.price, 12)
        self.assertEqual(item.inventory, 10)