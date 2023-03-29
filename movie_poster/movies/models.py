from django.db import models
from datetime import datetime as dt

# Create your models here.


class Category(models.Model):
    name = models.CharField("Category", max_length=50)
    description = models.TextField("Description", max_length=500)
    url = models.SlugField(max_length=150)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Genre(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description", max_length=500)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Actor(models.Model):
    name = models.CharField("Name", max_length=50)
    age = models.PositiveBigIntegerField("Years old", default=0)
    biography = models.TextField("Biography", max_length=500)
    image = models.ImageField("Photo", upload_to="actors/")

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"


class Director(models.Model):
    name = models.CharField("Name", max_length=50)
    age = models.PositiveBigIntegerField("Years old", default=0)
    filmography = models.ManyToManyField("Movie", "Filmography")
    biography = models.TextField("Biography", max_length=500)
    image = models.ImageField("Photo", upload_to="actors/")

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"


class Movie(models.Model):
    title = models.CharField("Title", max_length=100)
    tagline = models.CharField("Tagline", max_length=100, default="")
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.SET_NULL, null=True
    )
    description = models.TextField("Description", max_length=500)
    poster = models.ImageField("Poster", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Release date")
    country = models.CharField("Country", max_length=40)
    directors = models.ManyToManyField(Director, "Dorector")
    actors = models.ManyToManyField(Actor, "Actors")
    ganres = models.ManyToManyField(Genre, "Ganre")
    world_premiere = models.DateField("World premiere", default=dt.today)
    budget = models.PositiveIntegerField("Budget", default=0, help_text="onli dollars")
    fees_in_usa = models.PositiveIntegerField(
        "Fees in USA", default=0, help_text="only dollars"
    )
    fees_in_world = models.PositiveIntegerField(
        "Fees in World", default=0, help_text="Only dollars"
    )
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField("Draft", default=False)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class MovieShots(models.Model):
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    Image = models.ImageField("Image", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = "Movie shot"
        verbose_name_plural = "Movie shots"


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField("Value", default=0)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = "Rating star"
        verbose_name_plural = "Rating stars"


class Rating(models.Model):
    user_ip = models.CharField("IP adress", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="star")
    movie = models.ForeignKey(Movie, on_delete=models.CharField, verbose_name="Movie")

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.CharField("Message", max_length=5000)
    parent = models.ForeignKey(
        "self", verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
