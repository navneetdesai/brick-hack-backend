from django.db import models


class Lecture(models.Model):
    Name = models.TextField()
    date = models.DateField()
    professor = models.TextField()
    transcript = models.TextField()
    thumbnail = models.TextField()
    hidden = models.BooleanField()

    def __str__(self):
        return f'Lecture:{self.Name}\nProfessor:{self.professor}\nDate:{self.date}\n'


class Feature(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE),
    summary = models.TextField()
    outline = models.TextField()
    quiz = models.TextField()
    announcements = models.TextField()

    def __str__(self):
        return f'{self.outline}'
