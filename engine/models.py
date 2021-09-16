from django.db import models

class Account(models.Model):

    class TempBot:
        bot = None

    class Dialog:
        START = 'start'
        DEFAULT = 'default'

    username = models.TextField(default=None, null=True, blank=True)
    user_id = models.IntegerField(default=0)
    dialog = models.TextField(default=Dialog.START)
    temp = models.TextField(default='')
    reg_date = models.DateTimeField(auto_now_add=True)
    hyperlink = models.BooleanField(default=True)