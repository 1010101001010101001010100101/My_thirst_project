from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from  .models import Bb, Categories

#MAIN-HOME 
def index(request):
   bbs = Bb.objects.all()
   rubrics = Categories.objects.all()
   context = {'bbs' : bbs, 'rubrics' : rubrics}
   return render(request, 'bboard/index.html', context)

#CATEGORIES 
def by_rubric(request, rubric_id):
   bbs = Bb.objects.filter(rubric=rubric_id)
   rubrics = Categories.objects.all()
   current_rubric = Categories.objects.get(pk=rubric_id)
   context = {'bbs' : bbs, 'rubrics' : rubrics, 'current_rubric' : current_rubric}
   return render(request, 'bboard/by_categories.html', context)

