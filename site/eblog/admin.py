from django.contrib import admin
from .models import Blog , Comment , Videos , Feedback

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Videos)
admin.site.register(Feedback)