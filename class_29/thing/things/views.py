from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Thing


class ThingsListView(ListView):
    template_name = "things/things-list.html"
    model = Thing


class ThingsDetailView(DetailView):
    template_name = "things/things-detail.html"
    model = Thing


class ThingsCreateView(CreateView):
    template_name = "things/things-create.html"
    model = Thing
    fields = ['name', 'description', 'purchaser']


class ThingsUpdateView(UpdateView):
    template_name = "things/things-update.html"
    model = Thing
    fields = ['name', 'description', 'purchaser']


class ThingsDeleteView(DeleteView):
    template_name = "things/things-delete.html"
    model = Thing
    success_url = reverse_lazy("things_list")