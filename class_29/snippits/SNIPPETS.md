# Django Snippets

## Python snippets

```json
    "django_app_urls": {
      "prefix": "djau",
      "body": [
        "from django.urls import path",
        "from .views import $1",
        "",
        "urlpatterns = [",
        "    path('$2', $1.as_view(), name='$3')",
        "]",
        ""
      ],
      "description": "django_app_urls"
    },

    "Django Url Patterns - CRUD": {
      "prefix": "djuc",
      "body": [
        "from django.urls import path",
        "from .views import $1ListView, $1DetailView, $1CreateView, $1UpdateView, $1DeleteView",
        "",
        "urlpatterns = [",
        "    path('', $1ListView.as_view(), name='$2_list'),",
        "    path('<int:pk>/', $1DetailView.as_view(), name='$2_detail'),",
        "    path('create/', $1CreateView.as_view(), name='$2_create'),",
        "    path('<int:pk>/update/', $1UpdateView.as_view(), name='$2_update'),",
        "    path('<int:pk>/delete/', $1DeleteView.as_view(), name='$2_delete'),",
        "]"
      ],
      "description": "Django Url Patterns - CRUD"
    },

    "Django Views - CRUD": {
      "prefix": "djvc",
      "body": [
        "from django.views.generic import (",
        "    ListView,",
        "    DetailView,",
        "    CreateView,",
        "    UpdateView,",
        "    DeleteView,",
        ")",
        "from django.urls import reverse_lazy",
        "from .models import $1",
        "",
        "",
        "class $1ListView(ListView):",
        "    template_name = \"$2/$3-list.html\"",
        "    model = $1",
        "",
        "",
        "class $1DetailView(DetailView):",
        "    template_name = \"$2/$3-detail.html\"",
        "    model = $1",
        "",
        "",
        "class $1CreateView(CreateView):",
        "    template_name = \"$2/$3-create.html\"",
        "    model = $1",
        "    fields = []",
        "",
        "",
        "class $1UpdateView(UpdateView):",
        "    template_name = \"$2/$3-update.html\"",
        "    model = $1",
        "    fields = []",
        "",
        "",
        "class $1DeleteView(DeleteView):",
        "    template_name = \"$2/$3-delete.html\"",
        "    model = $1",
        "    success_url = reverse_lazy(\"$3_list\")"
      ],
      "description": "Django Views - CRUD"
    },
```

## HTML Snippets

```json
{% raw  %}
"Django Template Block": {
  "prefix": "dtb",
  "body": [
    "{% block $1 %}",
    "",
    "{% endblock $1 %}"
  ],
  "description": "Django Template Block"
  },
"Django Template Extends": {
  "prefix": "dte",
  "body": [
    "{% extends '$1.html' %}"
  ],
  "description": "Django Template Extends"
  },
  "Django Template Tag": {
    "prefix": "dtt",
    "body": [
      "{% $1 %}"
    ],
    "description": "Django Template Extends"
    },

    "django template child": {
      "prefix": "dtc",
      "body": [
        "{% extends '$1.html' %}",
        "",
        "{% block content %}",
        "  <h2>$2 coming soon</h2>",
        "{% endblock content %}"
      ],
      "description": "django template child"
    },

    "Django Template Form": {
      "prefix": "dtf",
      "body": [
        "<form action=\"\" method=\"POST\">",
        "  {% csrf_token %}",
        "  {{ form.as_p }}",
        "  <input type=\"submit\" value=\"$1\">",
        "</form>"
      ],
      "description": "Django Template Form"
    }
}
{% endraw  %}
```
