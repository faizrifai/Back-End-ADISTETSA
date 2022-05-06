from django.db.models import Model
from django.urls import reverse
from factory.django import DjangoModelFactory
from rest_framework import status

def testListView(self, url: str, factory_class: DjangoModelFactory, factory_length: int, check_length=True):
    for _ in range(factory_length):
        factory_class()

    response = self.client.get(reverse(url))

    self.assertEqual(response.status_code, status.HTTP_200_OK)

    if check_length:
        self.assertEqual(len(response.data['results']), factory_length)

    return response

def testListViewWithSearch(self, url: str, factory_class: DjangoModelFactory, factory_length: int, model_class: Model, model_field: str, check_length=True):
    for _ in range(factory_length):
        factory_class()

    response = self.client.get(reverse(url))

    self.assertEqual(response.status_code, status.HTTP_200_OK)

    if check_length:
        self.assertEqual(len(response.data['results']), factory_length)

    # search
    data = model_class.objects.get(pk=1)
    search_str = getattr(data, model_field)
    url_search = '{base_url}?{querystring}'.format(
        base_url=reverse(url),
        querystring=f'search={search_str}'
    )
    response_search = self.client.get(url_search)

    self.assertLessEqual(len(response_search.data['results']), 1)

    return response