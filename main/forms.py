from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)


class ProductForm(forms.ModelForm):
    # Add some custom validation to our image field
    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image. _size > 2*1024*1024:
                raise ValidationError("Image file too large ( > 4mb )")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")