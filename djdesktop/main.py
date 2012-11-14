import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djdesktop.settings")


from django.contrib.auth.models import User
from django.template import Context, loader


if __name__=='__main__':
    user =  User.objects.all()[0]
    t = loader.get_template('main.html')
    c = Context({'user': user})
    print t.render(c)
    
