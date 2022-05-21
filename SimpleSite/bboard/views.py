from django.views.generic.edit import CreateView
from tempfile import template
from django.shortcuts import render
from django.http import HttpResponse


from  .models import Bb, Categories
from .forms import BbForm

#MAIN-HOME ---- index.html
def index(request):
   bbs = Bb.objects.all()
   rubrics = Categories.objects.all()
   context = {'bbs' : bbs, 'rubrics' : rubrics,}
   return render(request, 'bboard/index.html', context)

#CATEGORIES ------ by_categories.html
def by_rubric(request, rubric_id):
   bbs = Bb.objects.filter(rubric=rubric_id)
   rubrics = Categories.objects.all()
   current_rubric = Categories.objects.get(pk=rubric_id)
   context = {'bbs' : bbs, 'rubrics' : rubrics, 'current_rubric' : current_rubric}
   return render(request, 'bboard/by_categories.html', context)

#ADD POSTS ------- 
class AddBb(CreateView):
   template_name = 'bboard/add_bb.html'
   form_class = BbForm
   success_url = '/bboard/'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['rubrics'] = Categories.objects.all()
      return context

   


