import datetime

import mock
from django.core.exceptions import ValidationError
from django.test import TestCase

from home.models import Nominee, NOMINATION_CHOICES


class TestSmoke(TestCase):

    def test(self):
        """
        Тестируем что сайт может просто открыться
        """

        urls = (
            '/',
        )
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, url)

    def test_is_stop_date(self):
        with self.settings(
                APPLY_STOP_DT=datetime.datetime.now()
                              + datetime.timedelta(days=7)):
            response = self.client.get('/')
            self.assertFalse(response.context['is_stop_date'])

        with self.settings(
                APPLY_STOP_DT=datetime.datetime.now()
                              - datetime.timedelta(days=7)):
            response = self.client.get('/')
            self.assertTrue(response.context['is_stop_date'])


class TestNominee(TestCase):
    def test_is_winner(self):
        n = Nominee.objects.create(
            nomination=NOMINATION_CHOICES[0][0],
            project_name='project_name1',
            founder='founder1',
            description='description1',
            is_winner=True,
            order=0,
        )
        n.clean()
        Nominee.objects.create(
            nomination=NOMINATION_CHOICES[0][0],
            project_name='project_name3',
            founder='founder3',
            description='description3',
            is_winner=True,
            order=1,
        )
        with self.assertRaises(ValidationError):
            n.clean()
        n.is_winner = False
        n.clean()
        n.save()

        n.is_winner = True
        with self.assertRaises(ValidationError):
            n.clean()
