from django import forms

from .models import personal_info_add

class ProductForm(forms.Form):
	name = forms.CharField()
	profession = forms.CharField()
	address = forms.CharField(widget=forms.Textarea(
													attrs={
													'rows':'4',
													'cols':'40'
													}
													)
							)
#	class Meta:
#		model = personal_info_add
#		fields = [
#			'name',
#			'profession',
#			'address'
#		]
