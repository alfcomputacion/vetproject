from django.forms import ModelForm, Textarea
from .models import Product


class ProductForm(ModelForm):
    class Meta:

        model = Product
        fields = ['prod_name', 'description', 'category',
                  'stock', 'buy_price', 'sell_price']
        widgets = {
            'prod_name': Textarea(
                attrs={'cols': 80, 'rows': 1, 'autofocus': True}
            ),
            'description': Textarea(
                attrs={'cols': 80, 'rows': 1}
            ),
            'stock': Textarea(
                attrs={'cols': 20, 'rows': 1,
                       'display': 'inline-block'}
            ),
            'buy_price': Textarea(
                attrs={'cols': 20, 'rows': 1,
                       'display': 'inline-block'}
            ),
            'sell_price': Textarea(
                attrs={'cols': 20, 'rows': 1,
                       'display': 'inline-block'}
            ),
        }
