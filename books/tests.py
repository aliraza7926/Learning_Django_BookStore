from django.test import TestCase
from django.urls import reverse
from .models import Book, Review
from django.contrib.auth import get_user_model

class BookTests(TestCase):
    
    def setUp(self):
        self.book = Book.objects.create(
            title='alex rider',
            author='horis',
            price='17.98',
        )

        self.user=get_user_model().objects.create(
            username='reviewuser',
            email='reviewuser@eamil.com',
            password='testpass123'
        )

        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review='oh this is bad',
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'alex rider')
        self.assertEqual(f'{self.book.author}', 'horis')
        self.assertEqual(f'{self.book.price}','17.98')
    
    def test_book_list_view(self):
        response=self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'alex rider')
        self.assertTemplateUsed(response,'books/book_list.html')
    
    def test_book_detail_view(self):
        response=self.client.get(self.book.get_absolute_url())
        no_response=self.client.get('books/12345')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'alex rider')
        self.assertContains(response,'oh this is bad')
        self.assertTemplateUsed(response,'books/book_detail.html')