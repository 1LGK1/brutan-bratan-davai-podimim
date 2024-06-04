from django.db import models

from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField( max_length = 100, unique_for_date =
    "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField( verbose_name = "Полное содержание")
    posted = models.DateTimeField(db_index = True, verbose_name = "Опубликована")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    image = models.ImageField(upload_to='images/', verbose_name="Картинка")
    def __str__(self):
        return str(self.title)

class Comment (models.Model):
    text = models.TextField(verbose_name = 'Текст комментария')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    date = models.DateTimeField(db_index = True, verbose_name = "Опубликован")
    post = models.ForeignKey(Blog , on_delete = models.CASCADE , verbose_name = "Статья комментария")
    
    def __str__(self):
        return f"{self.post} - {self.author}"
    
class Videos(models.Model):
    video_file = models.FileField(upload_to='videos/')
    name = models.TextField(verbose_name = "Название видео")

    def __str__(self):
        return str(self.name)


class Feedback(models.Model):
    username = models.CharField(max_length = 50 , verbose_name = "Имя")
    city = models.CharField(max_length = 50 , verbose_name = "Город")
    content = models.TextField(verbose_name = "Коментарий:")
    feedback = models.BooleanField(default = False)