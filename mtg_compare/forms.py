from django import forms
from random import randint
from .models import Card, CardComparison, CardComparisonResult
import ast

def get_new_comparison():
        num_cards = Card.objects.all().count()

        if (num_cards > 1):
            random_index = randint(0, num_cards-1)
            random_index2 = randint(0, num_cards-1)
            while (random_index == random_index2): 
                random_index2 = randint(0, num_cards-1)

            left_card = Card.objects.all()[random_index]
            right_card = Card.objects.all()[random_index2]
            left_card_choice = (left_card.name, left_card.name)
            right_card_choice = (right_card.name, right_card.name)
        else:
            left_card = None
            right_card = None
            left_card_choice = None
            right_card_choice = None

        return [left_card_choice, right_card_choice]

class CompareCardsForm(forms.Form):

    def get_fresh_comparison():
        return get_new_comparison()

    def get_left_card_name(self):
        return self.card_list[0][0]

    def get_right_card_name(self):
        return self.card_list[1][0]

    def get_other_card(self, name):
        if self.get_left_card_name() == name:
            return self.get_right_card_name()
        else:
            return self.get_left_card_name()

    def __init__(self, *args, **kwargs):
        post_flag = False
        if kwargs.get('post_flag'):
            post_flag = kwargs.pop('post_flag')

        super(CompareCardsForm, self).__init__(*args, **kwargs)

        if post_flag and len(args) > 0:
            self.card_list = ast.literal_eval(args[0].get('card_list')) #get the choices from the POST message
            self.fields['cards_to_compare'] = forms.ChoiceField(choices=self.card_list, widget=forms.RadioSelect())
        
        else:
            self.card_list = get_new_comparison()
            self.fields['cards_to_compare'] = forms.ChoiceField(choices=self.card_list, widget=forms.RadioSelect())
