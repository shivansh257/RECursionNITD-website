from django import forms
from .models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
import mimetypes



class Profileform(forms.ModelForm):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    college = models.TextField(max_length=100)
    dept = models.IntegerField
    image_url = models.URLField
    nickname = models.TextField(max_length=100)

    def clean_image_url(self):
        url = self.cleaned_data['image_url'].lower()
        if not valid_url_extension(url) or not valid_url_mimetype(url):
            raise forms.ValidationError(_("Not a valid Image. The URL must have an image extensions (.jpg/.jpeg/.png)"))
        return url

    class Meta:
        model = Profile
        fields = ('name', 'email', 'college', 'dept', 'image_url', 'nickname')

VALID_IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
]

def valid_url_extension(url, extension_list=VALID_IMAGE_EXTENSIONS):
    return any([url.endswith(e) for e in extension_list])


VALID_IMAGE_MIMETYPES = [
    "image"
]

def valid_url_mimetype(url, mimetype_list=VALID_IMAGE_MIMETYPES):
    mimetype, encoding = mimetypes.guess_type(url)
    if mimetype:
        return any([mimetype.startswith(m) for m in mimetype_list])
    else:
        return False