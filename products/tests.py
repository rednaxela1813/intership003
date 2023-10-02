from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Product, Lesson, LessonStatus

from .serializers import ProductSerializer, LessonSerializer, LessonStatusSerializer


class ProductModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', owner=self.user)

    def test_product_name(self):
        self.assertEqual(str(self.product.name), 'Test Product')

    def test_product_owner(self):
        self.assertEqual(self.product.owner, self.user)


class LessonModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', owner=self.user)
        self.lesson = Lesson.objects.create(name='Test Lesson', link='http://example.com',\
                                            duration=60, product=self.product)


    def test_lesson_name(self):
        self.assertEqual(str(self.lesson.name), 'Test Lesson')

    def test_lesson_link(self):
        self.assertEqual(self.lesson.link, 'http://example.com')

    def test_lesson_duration(self):
        self.assertEqual(self.lesson.duration, 60)

    def test_lesson_product(self):
        self.assertEqual(self.lesson.product, self.product)

    def test_lesson_product_name(self):
        self.assertEqual(self.lesson.product.name, 'Test Product')


class LessonStatusModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', email="test@email.com", password='testpassword')
        self.product = Product.objects.create(name='Test Product', owner=self.user)
        self.lesson = Lesson.objects.create(name='Test Lesson', link='http://example.com',\
                      duration=60, product=self.product)

        self.lesson_status = LessonStatus.objects.create(lesson=self.lesson, user=self.user, time_watched=10)

    def test_lesson_status_time(self):
        self.assertEqual(self.lesson_status.time_watched, 10)

    def test_lesson_status_status(self):
        self.assertFalse(self.lesson_status.status)

    def test_lesson_status_lesson(self):
        self.assertEqual(self.lesson_status.lesson, self.lesson)

    def test_lesson_status_user(self):
        self.assertEqual(self.lesson_status.user, self.user)

    def test_lesson_status_user_name(self):
        self.assertEqual(self.lesson_status.user.username, 'testuser')

    def test_lesson_status_lesson_name(self):
        self.assertEqual(self.lesson_status.lesson.name, 'Test Lesson')

    def test_lesson_status_lesson_product_name(self):
        self.assertEqual(self.lesson_status.lesson.product.name, 'Test Product')

    def test_lesson_status_lesson_product_owner_name(self):
        self.assertEqual(self.lesson_status.lesson.product.owner.username, 'testuser')

    def test_lesson_status_lesson_product_owner_email(self):
        self.assertEqual(self.lesson_status.lesson.product.owner.email, 'test@email.com')



class ProductSerializerTest(TestCase):
    def test_product_serialization(self):
        CustomUser = get_user_model()
        self.user = CustomUser.objects.create(username='testuser')
        self.product = Product.objects.create(name='Test Product', owner=self.user)
        serializer = ProductSerializer(self.product)
        expected_data = {'name': 'Test Product', 'owner': self.user.id, 'access': [], 'lessons': []}
        self.assertEqual(serializer.data, expected_data)


class LessonSerializerTest(TestCase):
    def test_lesson_serialization(self):
        CustomUser = get_user_model()
        self.user = CustomUser.objects.create(username='testuser')
        self.product = Product.objects.create(name='Test Product', owner=self.user)
        self.lesson = Lesson.objects.create(name='Test Lesson', link='http://example.com',\
                                            duration=60, product=self.product)
        serializer = LessonSerializer(self.lesson)
        expected_data = {'name': 'Test Lesson', 'link': 'http://example.com',\
                         'duration': 60, 'product': self.product.id}
        self.assertEqual(serializer.data, expected_data)


class LessonStatusSerializerTest(TestCase):
    def test_lesson_status_serialization(self):
        CustomUser = get_user_model()
        self.user = CustomUser.objects.create(username='testuser')
        self.product = Product.objects.create(name='Test Product', owner=self.user)
        self.lesson = Lesson.objects.create(name='Test Lesson', link='http://example.com',\
                                            duration=60, product=self.product)
        self.lesson_status = LessonStatus.objects.create(lesson=self.lesson, user=self.user, time_watched=10)
        serializer = LessonStatusSerializer(self.lesson_status)
        expected_data = {'lesson': self.lesson.id, 'user': self.user.id, 'status': False, 'time_watched': 10}
        self.assertEqual(serializer.data, expected_data)



