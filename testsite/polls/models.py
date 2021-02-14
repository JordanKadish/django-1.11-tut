# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible



# Create your models here.

# wrapper to allow py2 to work with unicode
@python_2_unicode_compatible
class Question(models.Model):
    def __str__(self):
        # this is used for querying, to differentiate Question objects in the db
        return str(self.id)
    # string no more than 200 chars
    # these vars become the collumn names in the db
    question_text = models.CharField(max_length=200)
    # date time, first arg is the human readable table name
    # (used in cases like automated documentation)
    pub_date = models.DateTimeField('date published')

    # a normal method within the model
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible
class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    # foreign key to relate to the Question model
    # relation can be one-to-one, many-to-one, or one-to-many
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # string no more than 200 chars
    # some Field Classes, eg CharField, have required params (eg max_length)
    # these params can be used in validation funcs as well as for the db schema
    choice_text = models.CharField(max_length=200)
    # int vote total
    votes = models.IntegerField(default=0)
