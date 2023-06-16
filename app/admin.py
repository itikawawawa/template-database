from django.contrib import admin
from .models import Post
from .models import User
from .models import Anime
from .models import Prace

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Anime)
admin.site.register(Prace)

# Register your models here.
