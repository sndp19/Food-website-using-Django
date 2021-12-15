from django import forms
from .models import Item

#contains classes  for each form bein created

class ItemForm(forms.ModelForm):
    class Meta:
        model =Item
        fields = ['item_name','item_desc','item_price','item_image']
