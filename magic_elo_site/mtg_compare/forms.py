from django import forms
from random import randint
from .models import Card, CardComparison, CardComparisonResult

def get_new_comparison():
        num_cards = Card.objects.all().count()

        if (num_cards > 1):
            random_index = randint(0, num_cards-1)
            random_index2 = randint(0, num_cards-1)
            while (random_index == random_index2): 
                random_index2 = randint(0, num_cards-1)

            left_card = Card.objects.all()[random_index]
            right_card = Card.objects.all()[random_index2]
            left_card_choice = (left_card.name, left_card)
            right_card_choice = (right_card.name, right_card)
        else:
            left_card = None
            right_card = None
            left_card_choice = None
            right_card_choice = None

        return [left_card_choice, right_card_choice]

class CompareCardsForm(forms.Form):

    def get_fresh_comparison():
        return get_new_comparison()

    def __init__(self, *args, **kwargs):
        super(CompareCardsForm, self).__init__(*args, **kwargs)
        self.fields['cards_to_compare'] = forms.ChoiceField(choices=get_new_comparison(), widget=forms.RadioSelect())
