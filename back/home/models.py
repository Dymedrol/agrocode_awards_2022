from django.core.exceptions import ValidationError
from django.db import models
from easy_thumbnails.fields import ThumbnailerField
from tinymce.models import HTMLField

NOMINATION_CHOICES = (  # max 14 characters
    ('agro_digital', 'Цифровизация года'),
    ('future_food', 'Еда будущего'),
    ('made_in_russia', 'Своя технология'),
    ('agro_hero', 'Лидер года'),
    ('agro_launch', 'Запуск года'),
    ('agro_idea', 'Идея года'),
)
STAGE_CHOICES = (
    ('1', 'Прием заявок на премию',),
    ('2', 'Отбор номинантов в Short List',),
    ('3', 'Публикация Short List',),
    ('4', 'Питчи шорт-листа и проведение церемонии награждения',),

)


class Cover(models.Model):
    stage = models.CharField('Текущий этап', choices=STAGE_CHOICES,
                             max_length=1)
    place = models.TextField('Место проведения', default='', blank=True)
    time = models.TextField('Время проведения', default='', blank=True)

    class Meta:
        verbose_name = 'Обложку'
        verbose_name_plural = 'Обложка'

    def __str__(self):
        return f'Cover #{self.id}'


class Nominee(models.Model):
    nomination = models.CharField('Номинация', max_length=14,
                                  choices=NOMINATION_CHOICES)
    project_name = models.CharField('Название проекта', max_length=255)
    founder = models.CharField('Создатель проекта', max_length=255)
    description = models.TextField('Описание')
    photo = ThumbnailerField('Фото', upload_to='founder',
                             null=True, blank=True)
    is_winner = models.BooleanField('Победитель', default=False, blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Номинант'
        verbose_name_plural = 'Номинанты'
        ordering = ('order',)

    def __str__(self):
        return f'{self.founder} - {self.project_name}'

    def clean(self):
        if self.is_winner:
            qs = Nominee.objects.filter(nomination=self.nomination, is_winner=True)
            if self.id:
                qs = qs.exclude(id=self.id)
            if qs.exists():
                raise ValidationError('В данной номинации уже есть победитель. Победитель может быть только один.')


class Stage(models.Model):
    is_active = False

    stage = models.CharField('Текущий этап', choices=STAGE_CHOICES,
                             max_length=1, unique=True)
    start_date = models.DateField('Дата начала', null=True, blank=True)
    stop_date = models.DateField('Дата окончания')

    class Meta:
        verbose_name = 'Этап'
        verbose_name_plural = 'Этапы проведения'

    def __str__(self):
        out = f'{self.get_stage_display()}: '
        if self.start_date:
            out += f'{self.start_date} - {self.stop_date}'
        else:
            out += f'{self.stop_date}'
        return out


class Jury(models.Model):
    name = models.CharField('Имя', max_length=255)
    surname = models.CharField('Фамилия', max_length=255)
    company = models.CharField('Компания', max_length=255,
                               default='', blank=True)
    role = models.CharField('Должность', max_length=255,
                            default='', blank=True)
    photo = ThumbnailerField('Фото', upload_to='jury')
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Жюри'
        verbose_name_plural = 'Жюри'
        ordering = ('order',)

    def __str__(self):
        return f'{self.name} {self.surname}'


class AwardCeremony(models.Model):
    place = models.TextField('Место')
    address = models.TextField('Адресс', default='', blank=True)
    date = models.DateField('Дата')
    about_date = models.TextField('Описание даты', default='', blank=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Церемония вручения'

    def __str__(self):
        return f'Церемония вручения #{self.id}'


class Partner(models.Model):
    name = models.CharField('Название', max_length=255)
    logo = ThumbnailerField('Логотип', upload_to='partner')
    url = models.URLField('url', default='', blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'
        ordering = ('order',)

    def __str__(self):
        return self.name


class Document(models.Model):
    NAME_CHOICES = (
        ('regulation_on_participation', 'Положение об участии',),
        ('privacy_policy', 'Политика конфиденциальности',),

    )
    name = models.CharField('Название файла', max_length=27, unique=True,
                            choices=NAME_CHOICES)
    file = models.FileField('Файл', upload_to='document')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Дополнительные файлы'

    def __str__(self):
        return self.get_name_display()


class FAQ(models.Model):
    question = models.CharField('Вопрос', max_length=255)
    answer = HTMLField('Ответ')
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'FAQ'
        ordering = ('order',)

    def __str__(self):
        return self.question
