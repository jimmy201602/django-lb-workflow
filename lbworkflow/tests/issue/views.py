from lbworkflow.views.generics import CreateView
from lbworkflow.views.generics import UpdateView
from lbworkflow.views.generics import WFListView

from .forms import IssueForm

from .models import Issue


class IssueCreateView(BSFormSetMixin, CreateView):
    form_classes = {
        'form': IssueForm,
        
    }


new = IssueCreateView.as_view()


class IssueUpdateView(BSFormSetMixin, UpdateView):
    form_classes = {
        'form': IssueForm,
        
    }


edit = IssueUpdateView.as_view()


class IssueListView(WFListView):
    wf_code = 'issue'
    model = Issue
    excel_file_name = 'issue'
    excel_titles = [
        'Created on', 'Created by',
        'Title', 'Summary', 'Content', 
        'Status',
    ]

    def get_excel_data(self, o):
        return [
            o.created_by.username, o.created_on,
            o.title, o.summary, o.content, 
            o.pinstance.cur_activity.name,
        ]


show_list = IssueListView.as_view()


def detail(request, instance, ext_ctx, *args, **kwargs):
    return {}