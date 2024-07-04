from django.contrib import admin

from authentication.models import RegisterModel, MovieModel, ReviewModel

admin.site.register(RegisterModel)
admin.site.register(MovieModel)
admin.site.register(ReviewModel)
