from django.shortcuts import render
from django.http import HttpResponse

def error(request):
    return 'Ошибка'

def index(request, login='Login_not_found', folder='Folder_not_found', folder_num=0):
    host = request.META['HTTP_HOST']
    info_user = request.META['HTTP_USER_AGENT']
    ip_user = request.META['REMOTE_ADDR']

    return HttpResponse(f"<h4>server host: {host} <br></h4>"
                        f"<h4>info browser: {info_user} <br></h4>"
                        f"<h4>user_ip: {ip_user} <br></h4>"
                        f'<h4>Login: {login}, folder: {folder}, folder num: {folder_num}</h4>')
