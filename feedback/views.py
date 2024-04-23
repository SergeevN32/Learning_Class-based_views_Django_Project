from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView


# Create your views here.


# class FeedBackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#         else:
#             return render(request, 'feedback/feedback.html', context={'form': form})


class FeedBackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    # --- ИЛИ ---
    # fields = '__all__'
    template_name = 'feedback/feedback.html'
    success_url = '/done'

    # def form_valid(self, form):
    #     form.save()
    #     return super(FeedBackView, self).form_valid(form)


class FeedBackUpdateView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    # fields = ['name']
    template_name = 'feedback/feedback.html'
    success_url = '/done'




# class FeedBackUpdateView(View):
#     def get(self, request, id_feedback: int):
#         feed = Feedback.objects.get(id=id_feedback)
#         form = FeedbackForm(instance=feed)
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request, id_feedback: int):
#         feed = Feedback.objects.get(id=id_feedback)
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect(f'/{id_feedback}')
#         else:
#             return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['name'] = 'Ivanov I.I.'
        # context['date'] = '10.04.2024'
        return context


# class ListFeedBack(TemplateView):
#     template_name = 'feedback/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         feedbacks = Feedback.objects.all()
#         context['feedbacks'] = feedbacks
#         return context


class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedbacks'

    def get_queryset(self):
        queryset = super().get_queryset()
        # filter_qs = queryset.filter(rating__gt=3)
        return queryset


# class DetailFeedBack(TemplateView):
#     template_name = 'feedback/detail_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         feedback = Feedback.objects.get(id=kwargs['id_feedback'])
#         context['feedback'] = feedback
#         return context


class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
