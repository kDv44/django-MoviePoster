from django.contrib import admin
from .models import (
    Actor,
    Category,
    Genre,
    Director,
    MovieShots,
    Movie,
    Rating,
    RatingStar,
    Reviews,
)

# Register your models here.

admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Genre)
