from django.core import mail
from django.test import TestCase

from apply.models import AgroMachinery, AgroDigital, FutureFood, MadeInRussia, \
    AgroHero, AgroLaunch, AgroIdea, FirstStep


class APISmokeTestMixing(object):
    url = None
    required_fields = None
    valid_data = None
    model = None
    check_email_notify = False

    def test_required_fields(self):
        response = self.client.post(self.url)
        response_json = response.json()
        for f in self.required_fields:
            self.assertIn(f, response_json, msg=f'Required field {f} not found in error list from response')
        self.assertEqual(response.status_code, 400)

    def test_valid_request(self):
        response = self.client.post(self.url, self.valid_data)
        if not response.status_code == 201:
            print(response.json())
        self.assertEqual(response.status_code, 201)

        if self.model and self.model.CURRENT_NOMINATION:
            response_json = response.json()
            item = self.model.objects.get(id=response_json['id'])
            self.assertEqual(item.nomination, self.model.CURRENT_NOMINATION)

    def test_create_and_remove_first_step(self):
        if not self.model:
            return False

        self.assertEqual(FirstStep.objects.count(), 0)
        self.assertEqual(self.model.objects.count(), 0)
        self.client.post('/api/first_step/', self.valid_data)
        self.assertEqual(FirstStep.objects.count(), 1)
        self.assertEqual(self.model.objects.count(), 0)
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(FirstStep.objects.count(), 0)
        self.assertEqual(self.model.objects.count(), 1)

    def test_send_email(self):
        if not self.check_email_notify:
            return False
        self.assertEqual(len(mail.outbox), 0)
        self.client.post(self.url, self.valid_data)
        self.assertEqual(len(mail.outbox), 1)


class TestFirstStep(APISmokeTestMixing, TestCase):
    url = '/api/first_step/'
    required_fields = (
        'name',
        'surname',
        'email',
        'agree_processing',
        'agree_rules',
    )
    valid_data = {
        'name': 'name',
        'surname': 'surname',
        'email': 'email@example.com',
        'phone': 'phone',
        'agree_processing': '1',
        'agree_rules': '1',
    }


class TestCallMe(APISmokeTestMixing, TestCase):
    url = '/api/call_me/'
    required_fields = (
        'email',
        'telegram',
        'agree_processing',
    )
    valid_data = {
        'email': 'email@example.com',
        'telegram': 'telegram',
        'agree_processing': '1',
    }


class TestAgroMachinery(APISmokeTestMixing, TestCase):
    url = '/api/agro_machinery/'
    model = AgroMachinery
    check_email_notify = True
    required_fields = (
        'name',
        'surname',
        'email',
        'agree_processing',
        'agree_rules',
        'case_name',
        'company',
        'company_about',
        'company_url',
        'release_year',
        'initial_description',
        'about_case',
        'about_result',
        'about_technology',
        'about_uniq',
    )
    valid_data = {
        'name': 'name',
        'surname': 'surname',
        'email': 'email@example.com',
        'phone': 'phone',
        'agree_processing': '1',
        'agree_rules': '1',
        'case_name': 'case_name',
        'company': 'company',
        'company_about': 'company_about',
        'company_url': 'some_url',
        'release_year': '2020',
        'initial_description': 'initial_description',
        'about_case': 'about_case',
        'about_result': 'about_result',
        'about_technology': 'about_technology',
        'about_uniq': 'about_uniq',
        'about_partners': 'about_partners',
        'extra_materials': 'extra_materials',
    }


class TestAgroDigital(APISmokeTestMixing, TestCase):
    url = '/api/agro_digital/'
    model = AgroDigital
    check_email_notify = True
    required_fields = (
        'name',
        'surname',
        'email',
        'agree_processing',
        'agree_rules',
        'case_name',
        'company',
        'company_about',
        'company_url',
        'release_year',
        'initial_description',
        'about_case',
        'about_result',
        'about_technology',
        'about_uniq',
    )
    valid_data = {
        'name': 'name',
        'surname': 'surname',
        'email': 'email@example.com',
        'phone': 'phone',
        'agree_processing': '1',
        'agree_rules': '1',
        'case_name': 'case_name',
        'company': 'company',
        'company_about': 'company_about',
        'company_url': 'some_url',
        'release_year': '2020',
        'initial_description': 'initial_description',
        'about_case': 'about_case',
        'about_result': 'about_result',
        'about_technology': 'about_technology',
        'about_uniq': 'about_uniq',
        'about_partners': 'about_partners',
        'extra_materials': 'extra_materials',
    }


class TestFutureFood(APISmokeTestMixing, TestCase):
    url = '/api/future_food/'
    model = FutureFood
    check_email_notify = True
    required_fields = (
        'name',
        'surname',
        'email',
        'agree_processing',
        'agree_rules',
        'case_name',
        'company',
        'company_about',
        'company_url',
        'release_year',
        'about_product',
        'about_process',
        'about_uniq',
        'production_volumes',
        'sales_market',
    )
    valid_data = {
        'name': 'name',
        'surname': 'surname',
        'email': 'email@example.com',
        'phone': 'phone',
        'agree_processing': '1',
        'agree_rules': '1',
        'case_name': 'case_name',
        'company': 'company',
        'company_about': 'company_about',
        'company_url': 'some_url',
        'release_year': '2020',
        'about_product': 'about_product',
        'about_process': 'about_process',
        'about_uniq': 'about_uniq',
        'production_volumes': 'production_volumes',
        'sales_market': 'sales_market',
        'extra_materials': 'extra_materials',
    }


class TestMadeInRussia(APISmokeTestMixing, TestCase):
    url = '/api/made_in_russia/'
    model = MadeInRussia
    check_email_notify = True
    required_fields = (
        'name',
        'surname',
        'email',
        'agree_processing',
        'agree_rules',
        'case_name',
        'company',
        'company_about',
        'company_url',
        'release_year',
        'release_month',
        'initial_description',
        'about_technology',
        'about_result',
    )
    valid_data = {
        'name': 'name',
        'surname': 'surname',
        'email': 'email@example.com',
        'phone': 'phone',
        'agree_processing': '1',
        'agree_rules': '1',
        'case_name': 'case_name',
        'company': 'company',
        'company_about': 'company_about',
        'company_url': 'some_url',
        'release_year': '2020',
        'release_month': '2',
        'initial_description': 'initial_description',
        'about_technology': 'about_technology',
        'about_result': 'about_result',
        'transition_process': 'transition_process',
        'about_partners': 'about_partners',
        'extra_materials': 'extra_materials',
    }


class TestAgroHero(APISmokeTestMixing, TestCase):
    url = '/api/agro_hero/'
    model = AgroHero
    check_email_notify = True
    required_fields = (
        'name',
        'surname',
        'email',
        'agree_processing',
        'agree_rules',
        'nominate_fio',
        'company',
        'company_about',
        'company_url',
        'role',
        'nomination_bio',
        'achievements',
    )
    valid_data = {
        'name': 'name',
        'surname': 'surname',
        'email': 'email@example.com',
        'phone': 'phone',
        'agree_processing': '1',
        'agree_rules': '1',
        'nominate_fio': 'nominate_fio',
        'company': 'company',
        'company_about': 'company_about',
        'company_url': 'some_url',
        'role': 'role',
        'nomination_bio': 'nomination_bio',
        'achievements': 'achievements',
    }


class TestAgroLaunch(APISmokeTestMixing, TestCase):
    url = '/api/agro_launch/'
    model = AgroLaunch
    check_email_notify = True
    required_fields = (
        'name',
        'surname',
        'email',
        'agree_processing',
        'agree_rules',
        'project_name',
        'project_url',
        'company_about',
        'release_year',
        'release_month',
        'project_stage',
        'project_sphere',
        'project_about',
        'about_technology',
        'about_result',
        'about_uniq',
        'founder',
        'team',
    )
    valid_data = {
        'name': 'name',
        'surname': 'surname',
        'email': 'email@example.com',
        'phone': 'phone',
        'agree_processing': '1',
        'agree_rules': '1',
        'project_name': 'project_name',
        'project_url': 'some_url',
        'company_about': 'company_about',
        'release_year': '2020',
        'release_month': '2',
        'project_stage': '1',
        'project_sphere': 'project_sphere',
        'project_about': 'project_about',
        'about_technology': 'about_technology',
        'about_result': 'about_result',
        'about_uniq': 'about_uniq',
        'founder': 'founder',
        'team': 'team',
    }


class TestAgroIdea(APISmokeTestMixing, TestCase):
    url = '/api/agro_idea/'
    model = AgroIdea
    check_email_notify = True
    required_fields = (
        'name',
        'surname',
        'email',
        'agree_processing',
        'agree_rules',
        'project_name',
        'project_date',
        'project_author',
        'project_about',
        'project_sphere',
        'about_uniq',
        'project_prototype',
        'about_technology',
    )
    valid_data = {
        'name': 'name',
        'surname': 'surname',
        'email': 'email@example.com',
        'phone': 'phone',
        'agree_processing': '1',
        'agree_rules': '1',
        'project_name': 'project_name',
        'project_date': 'project_date',
        'project_author': 'project_author',
        'project_about': 'project_about',
        'project_sphere': 'project_sphere',
        'about_uniq': 'about_uniq',
        'project_prototype': 'project_prototype',
        'about_technology': 'about_technology',
        'media_urls': 'media_urls',
        'extra_info': 'extra_info',
        'extra_materials': 'extra_materials',
    }
