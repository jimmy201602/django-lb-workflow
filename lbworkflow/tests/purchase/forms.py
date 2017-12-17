from django import forms
from django.forms.models import inlineformset_factory
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Layout

from lbutils import BootstrapFormHelperMixin
from lbworkflow.forms import WorkflowFormMixin
from lbworkflow.forms import BSQuickSearchForm

from .models import Purchase

from .models import Item



class SearchForm(BSQuickSearchForm):
    def layout(self):
        self.helper.layout = Layout(
            'q_quick_search_kw',
            StrictButton('Search', type="submit", css_class='btn-sm btn-default'),
            StrictButton('Export', type="submit", name="export", css_class='btn-sm btn-default'),
        )


class PurchaseForm(BootstrapFormHelperMixin, WorkflowFormMixin, forms.ModelForm):

    def __init__(self, *args, **kw):
        super(PurchaseForm, self).__init__(*args, **kw)
        self.init_crispy_helper()
        self.layout_fields([
            
            ['title', 'reason'],
            
        ])

    class Meta:
        model = Purchase
        fields = [
            'title', 'reason'
        ]


class ItemForm(BootstrapFormHelperMixin, WorkflowFormMixin, forms.ModelForm):

    class Meta:
        model = Item
        fields = [
          'purchase', 'name', 'qty', 'note'
        ]


def get_item_formset_class(**kwargs):
    params = {'extra': 1, 'can_delete': True}
    params.update(kwargs)
    return inlineformset_factory(
            Purchase, Item,
            form=ItemForm, **params)
