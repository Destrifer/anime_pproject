from django.contrib import admin
from .models import Anime, Comments, User

class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'password', 'email')

class AnimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'anime', 'comment_text')


admin.site.register(User, UserAdmin)
admin.site.register(Anime, AnimeAdmin)
admin.site.register(Comments, CommentsAdmin)