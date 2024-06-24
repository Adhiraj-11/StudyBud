from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' #taking all fields from the room model
        exclude = ['host','participants']
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
#basic struction for a model form