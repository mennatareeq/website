from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Image
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views import generic






@require_POST
def upload_detail(request,userid):
    form = ImageForm(request.POST, request.FILES)
    p = Image(userid = userid, product = request.FILES['product'])
    if form.is_valid():
        p.save()
        return render(request, 'detail.html', {'upload': upload})



