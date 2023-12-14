from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from cardquest.models import PokemonCard, Trainer, Collection
from cardquest.forms import TrainerForm, PokemonCardForm, CollectionForm
from django.urls import reverse_lazy
import json


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
    
class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'add.html'
    success_url = reverse_lazy('trainer-list')
    
class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'edit.html'
    success_url = reverse_lazy('trainer-list')
    
class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'delete.html'
    success_url = reverse_lazy('trainer-list')
    
# #Uses html premade list not database
# class PokemonCard(ListView):
#     model = PokemonCard
#     context_object_name = 'pokemon card'
#     template_name = 'pokemon-card.html'
#     paginate_by = 5

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

#     def get_queryset(self, *args, **kwargs):
#         qs = super(PokemonCard, self).get_queryset(*args, **kwargs)
#         return qs
    
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
    
class PokemonCardListView(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncard'
    template_name = "pokemoncards.html"
    json_file_path = 'data/pokemon_data.json'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon_data = self.get_pokemon_data()
        context['pokemon_data'] = pokemon_data
        return context
    def get_pokemon_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
        return data.get('pokemons', [])
    
class PokemonCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'add.html'
    success_url = reverse_lazy('pokemoncard-list')
    
class PokemonUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'edit.html'
    success_url = reverse_lazy('pokemoncard-list')
    
class PokemonDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'delete.html'
    success_url = reverse_lazy('pokemoncard-list')