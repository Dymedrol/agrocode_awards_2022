from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from home.models import NOMINATION_CHOICES

MONTH_CHOICES = (
    ('1', 'Январь',),
    ('2', 'Февраль',),
    ('3', 'Март',),
    ('4', 'Апрель',),
    ('5', 'Май',),
    ('6', 'Июнь',),
    ('7', 'Июль',),
    ('8', 'Август',),
    ('9', 'Сентябрь',),
    ('10', 'Октябрь',),
    ('11', 'Ноябрь',),
    ('12', 'Декабрь',),
)

STAGE_CHOICES = (
    ('1', 'MVP (работающий прототип без продаж)',),
    ('2', 'Работающая технология с подтвержденным спросом (есть пилоты или первые клиенты)',),
    ('3', 'Работающий бизнес (есть клиенты, операционная безубыточность)',),
    ('4', 'Зрелая компания с прибылью',),
)

YEAR_CHOICES = (
    ('before_2018', 'ранее 2018', ),
    ('2019', '2019', ),
    ('2020', '2020', ),
    ('2021', '2021', ),
    ('2022', '2022', ),
)


def required_boolean_validate(value):
    if value is not True:
        raise ValidationError("Обязательное поле")


class CallMe(models.Model):
    telegram = models.CharField('Ник в телеграмм', max_length=255)
    email = models.EmailField('Email')
    agree_processing = models.BooleanField(
        'Согласие с обработкой персональных данных',
        default=False,
        validators=[required_boolean_validate, ],
    )
    dt = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = '0 - Заявки из попапа'

    def __str__(self):
        date_time = timezone.localtime(self.dt)
        date_time = date_time.strftime("%d.%m.%Y, %H:%M:%S")
        return f'Заявка #{self.id} от {date_time}'


class ApplayBase(models.Model):
    name = models.CharField('Имя', max_length=255)
    surname = models.CharField('Фамилия', max_length=255)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=255)
    agree_processing = models.BooleanField(
        'Согласие с обработкой персональных данных',
        default=False,
        validators=[required_boolean_validate, ],
    )
    agree_rules = models.BooleanField(
        'согласие с правилами проведения',
        default=False,
        validators=[required_boolean_validate, ],
    )
    dt = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        abstract = True

    def __str__(self):
        date_time = timezone.localtime(self.dt)
        date_time = date_time.strftime("%d.%m.%Y, %H:%M:%S")
        return f'Заявка #{self.id} от {date_time}'


class ApplyExtraBase(ApplayBase):
    CURRENT_NOMINATION = None

    nomination = models.CharField('Номинация', max_length=14,
                                  choices=NOMINATION_CHOICES)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.CURRENT_NOMINATION:
            raise Exception('Need set CURRENT_NOMINATION')
        self.nomination = self.CURRENT_NOMINATION
        res = super(ApplayBase, self).save(*args, **kwargs)
        FirstStep.objects.filter(email=self.email).delete()
        CallMe.objects.filter(email=self.email).delete()
        return res


class FirstStep(ApplayBase):
    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = '1 - Заявки с первого шага'


# Deprecated!
class AgroMachinery(ApplyExtraBase):
    CURRENT_NOMINATION = 'agro_machinery'

    case_name = models.CharField('Название кейса', max_length=255)
    company = models.CharField('Компания, которая реализовала кейс', max_length=255)
    company_about = models.TextField('Описание компании')
    company_url = models.CharField('Сайт компании', max_length=255)
    release_year = models.CharField('Год реализации кейса', max_length=11,
                                    choices=YEAR_CHOICES, db_index=True)
    initial_description = models.TextField('Исходные данные')
    about_case = models.TextField('Описание кейса')
    about_result = models.TextField('Результат внедрения')
    about_technology = models.TextField('Использование технологий')
    about_uniq = models.TextField('Уникальность')
    about_partners = models.TextField('Партнер по реализации кейса', default='', blank=True)
    extra_materials = models.TextField('Дополнительные материалы', default='', blank=True)

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'Agro Machinery'


class AgroDigital(ApplyExtraBase):
    CURRENT_NOMINATION = 'agro_digital'

    case_name = models.CharField('Название кейса', max_length=255)
    company = models.CharField('Компания, которая реализовала кейс', max_length=255)
    company_about = models.TextField('Описание компании')
    company_url = models.CharField('Сайт компании', max_length=255)
    release_year = models.CharField('Год реализации кейса', max_length=11,
                                    choices=YEAR_CHOICES, db_index=True)
    initial_description = models.TextField('Исходные данные')
    about_case = models.TextField('Описание кейса')
    about_result = models.TextField('Результат внедрения')
    about_technology = models.TextField('Использование технологий')
    about_uniq = models.TextField('Уникальность')
    about_partners = models.TextField('Партнер по реализации кейса', default='', blank=True)
    extra_materials = models.TextField('Дополнительные материалы', default='', blank=True)

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'Цифровизация года'


class FutureFood(ApplyExtraBase):
    CURRENT_NOMINATION = 'future_food'

    case_name = models.CharField('Название кейса', max_length=255)
    company = models.CharField('Компания, которая реализовала кейс', max_length=255)
    company_about = models.TextField('Описание компании')
    company_url = models.CharField('Сайт компании', max_length=255)
    release_year = models.CharField('Год реализации кейса', max_length=11,
                                    choices=YEAR_CHOICES, db_index=True)
    about_product = models.TextField('Описание продукции')
    about_process = models.TextField('Процесс производства')
    about_uniq = models.TextField('Уникальность и новизна')
    production_volumes = models.TextField('Объемы производства')
    sales_market = models.TextField('Рынок сбыта')
    extra_materials = models.TextField('Дополнительные материалы', default='', blank=True)

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'Еда будущего'


class MadeInRussia(ApplyExtraBase):
    CURRENT_NOMINATION = 'made_in_russia'

    case_name = models.CharField('Название кейса', max_length=255)
    company = models.CharField('Компания, которая реализовала кейс', max_length=255)
    company_about = models.TextField('Описание компании')
    company_url = models.CharField('Сайт компании', max_length=255)
    release_year = models.CharField('Год запуска кейса', max_length=11,
                                    choices=YEAR_CHOICES, db_index=True)
    release_month = models.CharField('Месяц запуска кейса', max_length=2,
                                     choices=MONTH_CHOICES, db_index=True)
    initial_description = models.TextField('Исходные данные')
    about_technology = models.TextField('Описание технологии')
    transition_process = models.TextField('Процесс перехода', default='', blank=True)
    about_result = models.TextField('Результат внедрения')
    about_partners = models.TextField('Партнер по реализации кейса', default='', blank=True)
    extra_materials = models.TextField('Дополнительные материалы', default='', blank=True)

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'Своя технология'


class AgroHero(ApplyExtraBase):
    CURRENT_NOMINATION = 'agro_hero'

    nominate_fio = models.CharField('Имя и фамилия номинанта', max_length=255)
    company = models.CharField('Компания (основное место работы)', max_length=255)
    company_about = models.TextField('Описание компании')
    company_url = models.CharField('Сайт компании', max_length=255)
    role = models.CharField('Должность', max_length=255)
    nomination_bio = models.TextField('Экспертиза и биография номинанта')
    achievements = models.TextField('Достижения в области AgroTech')
    other_role = models.TextField('Другие роли', default='', blank=True)
    media_urls = models.TextField('Ссылки на интервью и публикации в СМИ',
                                  default='', blank=True)

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'Лидер года'


class AgroLaunch(ApplyExtraBase):
    CURRENT_NOMINATION = 'agro_launch'

    project_name = models.CharField('Название проекта / стартапа', max_length=255)
    project_url = models.CharField('Сайт проекта', max_length=255)
    company_about = models.TextField('Описание компании')
    release_year = models.CharField('Год запуска кейса', max_length=11,
                                    choices=YEAR_CHOICES, db_index=True)
    release_month = models.CharField('Месяц запуска кейса', max_length=2,
                                     choices=MONTH_CHOICES, db_index=True)
    project_stage = models.CharField('Стадия развития', max_length=1,
                                     choices=STAGE_CHOICES, db_index=True)
    project_sphere = models.CharField('Сфера применения', max_length=255)
    project_about = models.TextField('Описание проекта')
    about_technology = models.TextField('Использование технологий')
    about_result = models.TextField('Результаты и показатели')
    about_uniq = models.TextField('Уникальность')
    founder = models.TextField('Основатель проекта')
    team = models.TextField('Команда проекта')
    extra_info = models.TextField('Дополнительная информация', default='', blank=True)
    extra_materials = models.TextField('Дополнительные материалы', default='', blank=True)

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'Запуск года'


class AgroIdea(ApplyExtraBase):
    CURRENT_NOMINATION = 'agro_idea'

    project_name = models.CharField('Название проекта', max_length=255)
    project_date = models.CharField('Примерная дата реализации или публикации', max_length=255)
    project_author = models.CharField('Автор', max_length=255)
    project_about = models.TextField('Описание проекта')
    project_sphere = models.CharField('Сфера применения', max_length=255)
    about_uniq = models.TextField('Научная новизна и уникальность')
    project_prototype = models.TextField('Наличие и описание работающего прототипа')
    about_technology = models.TextField('Использование технологий')
    media_urls = models.TextField(
        'Ссылки на публикации вашего проекта в открытом '
        'доступе (научные издания, сайты, конференции)',
        default='', blank=True
    )
    extra_info = models.TextField('Дополнительная информация', default='', blank=True)
    extra_materials = models.TextField('Дополнительные материалы', default='', blank=True)

    class Meta:
        verbose_name = 'заявку'
        verbose_name_plural = 'Идея года'
