from django.shortcuts import render
from django.db.models import Max

from .models import Card, CardRanking, CardType, CardColor, CardSet, CardRanking, CardComparison, CardComparisonResult

def index(request):
    '''
    View function for the home page
    '''

    num_cards = Card.objects.all().count()
    num_card_comparison_results = CardComparisonResult.objects.all().count()

    highest_rated_card_elo = CardRanking.objects.all().aggregate(Max('elo'))
    highest_rated_card_ranking = CardRanking.objects.all().filter(elo=highest_rated_card_elo['elo__max'])[0]

    if (num_cards <= 1):
        random_index = randint(0, num_cards-1)
        random_index2 = randint(0, num_cards-1)
        while (random_index == random_index2): 
            random_index2 = randint(0, num_cards-1)

        left_card = Card.objects.all()[random_index]
        left_card = Card.objects.all()[random_index2]
    else:
        left_card = None
        right_card = None


    return render(
        request,
        'index.html',
        context={'num_cards': num_cards, 
                 'num_card_comparison_results': num_card_comparison_results,
                 'highest_rated_card_ranking': highest_rated_card_ranking,
                 'left_card': left_card,
                 'right_card': right_card,
                 },
    )