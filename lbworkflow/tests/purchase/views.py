from lbworkflow.views.generics import CreateView
from lbworkflow.views.generics import UpdateView
from lbworkflow.views.generics import WFListView
from lbworkflow.views.mixin import BSFormSetMixin

from .forms import PurchaseForm

from .forms import get_item_formset_class

from .models import Purchase


class PurchaseCreateView(BSFormSetMixin, CreateView):
    form_classes = {
        'form': PurchaseForm,
        
        'fs_item': get_item_formset_class(),
        
    }


new = PurchaseCreateView.as_view()


class PurchaseUpdateView(BSFormSetMixin, UpdateView):
    form_classes = {
        'form': PurchaseForm,
        
        'fs_item': get_item_formset_class(),
        
    }


edit = PurchaseUpdateView.as_view()


class PurchaseListView(WFListView):
    wf_code = 'purchase'
    model = Purchase
    excel_file_name = 'purchase'
    excel_titles = [
        'Created on', 'Created by',
        'Title', 'Reason', 
        'Status',
    ]

    def get_excel_data(self, o):
        return [
            o.created_by.username, o.created_on,
            o.title, o.reason, 
            o.pinstance.cur_activity.name,
        ]


show_list = PurchaseListView.as_view()


def detail(request, instance, ext_ctx, *args, **kwargs):
    return {}