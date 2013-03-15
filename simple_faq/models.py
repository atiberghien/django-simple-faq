from django.db import models
from tinymce import models as tinymce_models

photos_path = "/simple-faq/"


class Topic(models.Model):
    text = models.CharField(max_length=200)
    number = models.IntegerField()

    class Meta:
        order_with_respect_to = 'number'


class Question(models.Model):
    text = models.CharField(max_length=200)
    answer_text = tinymce_models.HTMLField()
    topic = models.ForeignKey(Topic, related_name="questions")
    header_picture = models.ImageField(upload_to=photos_path, blank=True)
    number = models.IntegerField()
    related_questions = models.ManyToManyField("self", related_name="related_questions")

    class Meta:
        order_with_respect_to = 'number'