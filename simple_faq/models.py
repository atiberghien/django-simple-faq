from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

if 'cked' in settings.INSTALLED_APPS:
    from cked.fields import RichTextField
elif 'tinymce' in settings.INSTALLED_APPS:
    from tinymce.models import HTMLField as RichTextField

photos_path = "simple-faq/"


class Topic(models.Model):
    text = models.CharField(max_length=200, verbose_name=_('text'))
    number = models.IntegerField(verbose_name=_('number'))

    class Meta:
        ordering = ['number']
        verbose_name = _('topic')

    def __unicode__(self):
        return u'(%s) %s' % (self.number, self.text, )


class Question(models.Model):
    text = models.CharField(max_length=200, verbose_name=_('question'))
    answer_text = RichTextField(verbose_name=_('answer'))
    topic = models.ForeignKey(Topic, related_name="questions", verbose_name=_('topic'))
    header_picture = models.ImageField(upload_to=photos_path, blank=True, verbose_name=_('picture'))
    number = models.IntegerField(verbose_name=_('number'))
    related_questions = models.ManyToManyField("self", related_name="related_questions", blank=True, null=True, verbose_name=_('related questions'))

    class Meta:
        ordering = ['number']
        verbose_name = _('question')

    def __unicode__(self):
        return u'(%s) %s' % (self.number, self.text, )
