from django.shortcuts import render, redirect
from django.contrib import messages

def landing(req):
    return render(req, 'landing.html')


def msg_render(req):
    messages.success(req, 'Successfully done')
    return render(req, 'landing.html')


def msg_redirect(req):
    messages.success(req, 'Redirect Msg successfully done')
    return redirect('landing')   
