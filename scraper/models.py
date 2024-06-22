from django.db import models


# Create your models here.
class Base(models.Model):
    title = models.CharField(
        max_length=100,
        null=True,
        verbose_name='title'
                            )
    description = models.TextField(
        null=True,
        verbose_name='description')

    class Meta:
        abstract = True
        ordering = ('pk',)

    def __str__(self):
        raise NotImplementedError('Implement __str__ method')


class Book(Base):
    author = models.CharField(
        max_length=50,
        verbose_name='author',
        null=True,
    )
    rate = models.CharField(
        max_length=10,
        verbose_name='rate',
        null=True
    )
    numbers_of_ratings = models.CharField(
        null=True,
        verbose_name='number of ratings',
        max_length=50,
    )
    numbers_of_reviews = models.CharField(
        null=True,
        verbose_name='number of reviews',
        max_length=50)
    genres = models.JSONField(
        default=list,
        verbose_name='genres',
        null=True
    )
    pages_format = models.CharField(
        max_length=100,
        verbose_name='pages format',
        null=True,
    )
    publication_info = models.TextField(verbose_name='publication_info',null=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Group(Base):
    tags = models.JSONField(
        default=list,
        verbose_name='tags',
        null=True,
    )
    rules = models.TextField(
        verbose_name='rules',
        null=True
    )
    categories = models.JSONField(
        default=list,
        verbose_name='categories',
        null=True,
    )
    website = models.URLField(
        verbose_name='website',
        null=True
    )
    location = models.CharField(
        max_length=150,
        verbose_name='location',
        null=True,
    )
    group_type = models.CharField(
        max_length=300,
        verbose_name='group type',
        null=True
    )

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Search(models.Model):
    OPTION_ONE = 'books'
    OPTION_TWO = 'groups'

    MY_CHOICES = [
        (OPTION_ONE, 'books'),
        (OPTION_TWO, 'groups'),
    ]
    search_bar = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=MY_CHOICES, default=OPTION_ONE)

    def __str__(self):
        return self.search_bar
