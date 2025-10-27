from django.test import TestCase
from reservation.models import Menu
from reservation.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="Pizza", price=150, inventory=10)
        self.item2 = Menu.objects.create(title="Pasta", price=120, inventory=15)
        self.item3 = Menu.objects.create(title="Burger", price=100, inventory=20)

    def test_getall(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        self.assertEqual(len(serialized_items.data), 3)
