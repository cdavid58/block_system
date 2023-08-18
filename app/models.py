from django.db import models

class System_Block(models.Model):
	active = models.BooleanField(default = True)