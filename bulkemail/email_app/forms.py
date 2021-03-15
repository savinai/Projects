from django import forms
# from email_app.models import BulkEmail

class EntryForm(forms.Form):

    Senders_Email_ID = forms.EmailField()
    Senders_Password = forms.CharField(widget=forms.PasswordInput())
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea(attrs={'cols':80, 'rows':20}))
    # Upload_Image = forms.ImageField()
    Enter_Image_Url = forms.CharField(required=False, label="Image URL (optional)")
