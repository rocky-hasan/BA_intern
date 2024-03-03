from django.shortcuts import render
from .forms import Imageform
from .models import Image
from django.views.generic import DeleteView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Imageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = Imageform()
    img = Image.objects.all()
    return render(request, 'home.html', {'form': form, 'img': img})

class ImageDeleteView(DeleteView):
    form_class=Imageform
    success_url = reverse_lazy('home')  # Redirect to this URL after successful deletion
    template_name = 'confirm_delete.html'