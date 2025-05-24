from .models import Book,Category
from django.forms import ModelForm



class AddBook(ModelForm):
    class Meta:
        model=Book
        fields="__all__"

class AddCat(ModelForm):
    class Meta:
        model=Category
        fields="__all__"
