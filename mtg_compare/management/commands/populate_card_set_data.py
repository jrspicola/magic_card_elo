import json

from django.core.management.base import BaseCommand
from mtg_compare.models import Card, CardRanking, CardType, CardColor, CardSet

def create_card_set(set_info):
    print('STARTING SET:')
    print(set_info['name'])
    try:
        s = CardSet.objects.get(cardSet=set_info['name'])
    except CardSet.DoesNotExist:
        s = CardSet(cardSet=set_info['name'], code=set_info['code'])
        s.save()
    return s

def create_card(card_info, s):
    print(card_info['name'])
    
    if card_info.get('layout') == 'token':
        print('This card is a token and was not added.')
        return None

    try:
        c = Card.objects.get(name=card_info['name'])
    except Card.DoesNotExist:
        c = None

    if c:
        c.cardSet.add(s)
    else:
        #create card
        c = Card(name=card_info['name'], cmc=card_info['cmc'])
        c.save()

        CardRanking(card=c).save()

        #add type
        for t in card_info.get('types'):
            try:
                c.cardType.add(CardType.objects.get(cardType=t))
            except CardType.DoesNotExist:
                print('Card type: \'' + t + '\' does not exist in DB.')

        #add color
        if card_info.get('colors',None):
            for color in card_info['colors']:
                try:
                    c.cardColor.add(CardColor.objects.get(cardColor=color))
                except CardColor.DoesNotExist:
                    print('Card color: \'' + t + '\' does not exist in DB.')
        else:
            c.cardColor.add(CardColor.objects.get(cardColor='Colorless'))


        c.cardSet.add(s)



class Command(BaseCommand):
    help = 'Load the dynamic data for Cards, Sets and Rankings - These are constant and should not change.'

    def add_arguments(self, parser):
        parser.add_argument(
                '--file',
                type=str,
                action='store',
                dest='filePath',
                help='Name of the file containing the card info to upload'
            )

    def _create_card_sets(self, path):
        print('LOADING JSON')
        data = json.load(open(path, encoding='utf8'))
        print('JSON LOADED')
        
        #for each set
        for key in data.keys():
            #create the set
            s = create_card_set(data[key])

            #For each card
            for card in data[key]['cards']:
                create_card(card, s)


            #print(len(data[key]['cards']))

    def handle(self, *args, **options):
        self._create_card_sets(options['filePath'])