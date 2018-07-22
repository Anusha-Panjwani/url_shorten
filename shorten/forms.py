from django import forms
from shorten.models import bitly


class shorten_form(forms.ModelForm):
	class Meta:
		model = bitly
		fields = ["long_url"]