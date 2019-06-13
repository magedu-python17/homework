from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from util.token import no_logged_redirect_to_login
from util.menu_manager import permission


@no_logged_redirect_to_login
def logout(request):
    if request.method == 'GET':
        request.session.clear()
        rep = HttpResponseRedirect('/')
        rep.delete_cookie('jwt_token')
        return rep
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


@permission
def index(request):
    if request.method == 'GET':
        return redirect(reverse("app-backend:backend-article"))
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")


@permission
def develop(request):
    if request.method == 'GET':
        return render(request, 'backend_develop.html')
    return HttpResponseNotFound("说出来你可能不信，该页面被外星人劫持了^_^")

