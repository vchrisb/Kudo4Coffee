
from django import forms
from .models import BeverageHistory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class BeverageForm(forms.ModelForm):

    class Meta:
        model = BeverageHistory
        fields = ['bean_amount', 'temperature', 'beverage']

    def __init__(self, *args, **kwargs):
        super(BeverageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Get Beverage'))
        self.helper.form_method = 'post'
        self.helper.form_action = 'beverage'