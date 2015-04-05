from django.db import models

class Visitor(models.Model):
    def __unicode__(self):
        return self.name

    class meta(file):
        app_label = 'blog'

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    reg_date = models.DateTimeField('date registered')
    visits = models.IntegerField(default=0)