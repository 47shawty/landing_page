from django.views import generic
from . import models

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from task.settings import EMAIL_HOST_USER
from .forms import ContactForm


class HomeView(generic.TemplateView):
    template_name = 'pages/home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['head'] = models.Header.objects.all().first()
        context['products'] = models.ProductDetail.objects.order_by('-created')[:5]
        long, lat = models.SomeLocationModel.objects.all().first().location
        context['long'] = long
        context['lat'] = lat
        return context


class ProductDetail(generic.DetailView):
    model = models.ProductDetail
    template_name = 'pages/product/product_detail.html'
    context_object_name = 'product'
    # pk_url_kwarg = 'id'


class SomeLocationModel(generic.TemplateView):
    model = models.SomeLocationModel
    template_name = 'pages/home/home_include/map.html'
    context_object_name = 'map'


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            try:
                send_mail(name, 'salom', EMAIL_HOST_USER, [email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('main:home_url')
    return render(request, "pages/home/index.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
