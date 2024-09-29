

from django import forms
from tasks.models import Category


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Search",
                "class":"form-control",

            }
        )
    )
    category = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple

    )

    orderings = (
        ("created_at", "По дате создания"),
        ("-created_at", "По дате создания(по убыванию)"),
        ("title", "По  названию"),
        ("-title", "По  названию(по убыванию)"),
        ("rate", "По рейтингу"),
        ("-rate", "По рейтингу(по убыванию)"),
    )
    ordering = forms.ChoiceField(required=False, choices=orderings)