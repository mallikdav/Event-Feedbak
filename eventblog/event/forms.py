__author__ = 'User'
from django.forms import *    # fill in custom user info then save it
from event.models import Feedback
from event.models import Suggestion
from event.models import Rating
from django.utils.translation import ugettext_lazy as _


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        # exclude = ('event_id',)
        fields = ('feedback_data', 'event')
        labels = {
            'feedback_data': _('Feedback'),
            'event': "",
        }
        widgets = {
            'feedback_data': TextInput(attrs={'class': 'form-control'}),
            'event': TextInput(attrs={'style': 'display:none;'}),
        }


class SuggestionForm(ModelForm):
    class Meta:
        model = Suggestion
        fields = ('suggestion_data',)
        labels = {
            'suggestion_data': _('Suggestion'),
        }
        widgets = {
            'suggestion_data': TextInput(attrs={'class': 'form-control'}),
        }


RATING_CHOICES = (
    (' 1 ', 'One'),
    (' 2 ', 'Two'),
    (' 3 ', 'Three'),
    (' 4 ', 'Four'),
    (' 5 ', 'Five'),

)


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ('rating_star',)
        labels = {
            'rating_star': _('Rating'),
        }
        widgets = {
            'rating_star': Select(choices=RATING_CHOICES, attrs={'class': 'form-control'}),
        }

