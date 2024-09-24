from django import forms

class InvoiceForm(forms.Form):
    pdf = forms.FileField(label="Select PDF")
    question = forms.CharField(label="Enter your question", widget=forms.TextInput())
