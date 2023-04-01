# Generated by Django 4.1.7 on 2023-03-30 17:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0003_alter_movie_actors_alter_movie_directors_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="director",
            name="filmography",
            field=models.ManyToManyField(
                null=True, to="movies.movie", verbose_name="Filmography"
            ),
        ),
    ]
