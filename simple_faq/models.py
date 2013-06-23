from django.conf import settings
from django.db import models

if 'cked' in settings.INSTALLED_APPS:
    from cked.fields import RichTextField
elif 'tinymce' in settings.INSTALLED_APPS:
    from tinymce.models import HTMLField as RichTextField

photos_path = "simple-faq/"


class Topic(models.Model):
    text = models.CharField(max_length=200)
    number = models.IntegerField()

    class Meta:
        ordering = ['number']

    def __unicode__(self):
        return u'(%s) %s' % (self.number, self.text, )


class Question(models.Model):
    text = models.CharField(max_length=200)
    answer_text = RichTextField()
    topic = models.ForeignKey(Topic, related_name="questions")
    header_picture = models.ImageField(upload_to=photos_path, blank=True)
    number = models.IntegerField()
    related_questions = models.ManyToManyField("self", related_name="related_questions", blank=True, null=True)

    class Meta:
        ordering = ['number']

    def __unicode__(self):
        return u'(%s) %s' % (self.number, self.text, )
