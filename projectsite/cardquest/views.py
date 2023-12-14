from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from cardquest.models import PokemonCard, Trainer, Collection
from cardquest.forms import TrainerForm
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainer.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(TrainerList, self).get_queryset(*args, **kwargs)
        return qs
    
class PokemonCard(ListView):
    model = PokemonCard
    context_object_name = 'pokemon card'
    template_name = 'pokemon-card.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(PokemonCard, self).get_queryset(*args, **kwargs)
        return qs
    
class Collection(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collection.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(Collection, self).get_queryset(*args, **kwargs)
        return qs
    
class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')
    
class TrainerCreateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')