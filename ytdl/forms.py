from django import forms


class DownloadForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Entrez le lien de votrez vidéo' }), label=False)
