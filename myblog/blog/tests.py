#encoding:utf-8
from blog.models import Event,Guest
q1=Event.objects.get(name='魅族16plus发布会')
print q1
