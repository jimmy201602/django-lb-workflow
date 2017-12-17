from django import forms
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Layout

from lbutils import BootstrapFormHelperMixin
from lbworkflow.forms import WorkflowFormMixin
from lbworkflow.forms import BSQuickSearchForm

from .models import Issue



class SearchForm(BSQuickSearchForm):
    def layout(self):
        self.helper.layout = Layout(
            'q_quick_search_kw',
            StrictButton('Search', type="submit", css_class='btn-sm btn-default'),
            StrictButton('Export', type="submit", name="export", css_class='btn-sm btn-default'),
        )


class IssueForm(BootstrapFormHelperMixin, WorkflowFormMixin, forms.ModelForm):

    def __init__(self, *args, **kw):
        super(IssueForm, self).__init__(*args, **kw)
        self.init_crispy_helper()
        self.layout_fields([
            
            ['title', 'summary'],
            
            ['content', ''],
            
        ])

    class Meta:
        model = Issue
        fields = [
            'title', 'summary', 'content'
        ]
