from django.shortcuts import render
from email_app.forms import EntryForm
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
# from bulkemail.settings import EMAIL_HOST_USER
import openpyxl
import pandas as pd
import mimetypes
from django.core.mail import get_connection
from django.core.mail import EmailMultiAlternatives
import yaml
import base64
# Create your views here.
def home(request):
    form=EntryForm()
    if request.method == "POST":

        form=EntryForm(request.POST, request.FILES)
        if form.is_valid():
            emailList=request.FILES["Excel_Email_List"]

            attachment=request.FILES.get('Attachment',False)



            sub=request.POST['subject']
            bdy=request.POST['body']

            image=request.POST.get('Enter_Image_Url',False)
            user_id=request.POST['Senders_Email_ID']

            pasword=request.POST['Senders_Password']

            toList=pd.read_excel(emailList)
            names = toList['NAME']
            emails = toList['EMAIL']

            for i in range(len(emails)):
                _name = str(names[i]).title()
                receiver = str(emails[i])

                mesg="""<html>
                <head></head>
                <body>
                <h2>Dear %s</h2>
                <br>
                <p>%s</p>
                <img src=%s alt="No Inline Image">
                </body>
                </html>""" %(_name,bdy,image)


                connection = get_connection(
                        host='smtp.gmail.com',
                        port='587',
                        username=user_id,
                        password=pasword
                        )
                ml=EmailMessage(sub, mesg, to=[receiver],connection=connection)

                if request.POST.get('attachment',False)!=False:
                    ml.attach(attachment.name, attachment.file.getvalue(), mimetypes.guess_type(attachment.name)[0])
                ml.content_subtype = "html"
                ml.send()
                
            return HttpResponse('Mails sent successfully. Press back button and on the browser and refresh the page to send again')
    else:
        form = EntryForm()
    return render(request, 'email_app/home.html', {'form':form})
