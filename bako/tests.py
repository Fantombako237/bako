from django.contrib.auth.models import User
from django.test import TestCase
from .models import Recipe, Category

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Dinner')
        self.recipe = Recipe.objects.create(
            user=self.user,
            title='Test Recipe',
            description='Test Description',
            ingredients='Test Ingredients',
            instructions='Test Instructions',
            category=self.category
        )

    def test_recipe_creation(self):
        recipe = Recipe.objects.get(title='Test Recipe')
        self.assertEqual(recipe.description, 'Test Description')

    def test_category_assignment(self):
        recipe = Recipe.objects.get(title='Test Recipe')
        self.assertEqual(recipe.category.name, 'Dinner')
