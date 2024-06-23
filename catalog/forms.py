from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'category_name', 'image', 'price',)

    def clean_title(self):
        cleaned_data = self.cleaned_data.get('title')
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in bad_words:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка! название не должно содержать запрещённых слов!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in bad_words:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка! описание не должно содержать запрещённых слов!')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ("__all__")


