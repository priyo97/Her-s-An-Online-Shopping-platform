from django import forms

class Login(forms.Form):
	username = forms.CharField(required=True,widget=forms.TextInput(attrs={"id":"username","name":"username","placeholder":"Enter username"}))
	password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={"id":"password","name":"password","placeholder":"Enter password"}))

class Register(forms.Form):
	
	first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={"id":"first_name","name":"first_name","placeholder":"Enter first name"}))
	last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={"id":"last_name","name":"last_Name","placeholder":"Enter last name"}))

	username = forms.CharField(required=True,widget=forms.TextInput(attrs={"id":"username","name":"username","placeholder":"Enter username"}))
	password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={"id":"password","name":"password","placeholder":"Enter password"}))
	email = forms.CharField(required=True,widget=forms.EmailInput(attrs={"id":"email","name":"email","placeholder":"Enter email"}))

	phone_number = forms.CharField(required=True,widget=forms.TextInput(attrs={"id":"phone_number","name":"phone_number","placeholder":"Enter phone number"}))

	address = forms.CharField(required=True,widget=forms.TextInput(attrs={"id":"address","name":"address","placeholder":"Enter address"}))
	
class Problem(forms.Form):

	username = forms.CharField(required=True,widget=forms.TextInput(attrs={"id":"username","name":"username","placeholder":"Enter username"}))
	query = forms.CharField(required=True,widget=forms.Textarea(attrs={"id":"query","name":"query","placeholder":"Enter query","cols":"53"}))