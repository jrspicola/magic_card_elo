from django.db import models
from django.urls import reverse

ELO_DEFAULT = 1400

class CardColor(models.Model):
    cardColor = models.CharField(max_length=20, help_text="Enter a color", unique=True)

    def __str__(self):
        return self.cardColor

class CardType(models.Model):
    cardType = models.CharField(max_length=50, help_text="Enter a card type", unique=True)

    def __str__(self):
        return self.cardType

class CardSet(models.Model):
    cardSet = models.CharField(max_length=50, help_text="Enter the name of a set", unique=True)

    def __str__(self):
        return self.cardSet

class Card(models.Model):
    '''
    Model representing a single Magic Card.
    '''
    name = models.CharField(max_length=200, unique=True)
    cmc = models.IntegerField(default=0, help_text="Enter the converted mana cost of this card")

    cardType = models.ManyToManyField(CardType, help_text="Select a type for this card")
    cardColor = models.ManyToManyField(CardColor, help_text="Select a color for this card")
    cardSet = models.ManyToManyField(CardSet, help_text="Select a set this card is from")

    #TODO: Add a 'get random card' method.
    #TODO: Implement a custom manager for the random method

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''returns the url to access a particular card information'''
        return reverse('card-detail', args=[str(self.id)])

    def card_type_display(self):
        return ', '.join([ cardType.cardType for cardType in self.cardType.all()])
    card_type_display.short_description = 'Type'

    def card_color_display(self):
        return ', '.join([ cardColor.cardColor for cardColor in self.cardColor.all()])
    card_color_display.short_description = 'Color'

class CardComparison(models.Model):
    '''
    Model representing a comparison between two cards
    '''
    leftCard = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="left_card")
    rightCard = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="right_card")

    def __str__(self):
        return str(self.id) + ': ' + str(self.leftCard) + ' vs. ' + str(self.rightCard)

class CardComparisonResult(models.Model):
    '''
    Model representing a completed comparison
    '''
    comparison = models.ForeignKey(CardComparison, on_delete=models.CASCADE)
    winner = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="winning_card")
    loser = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="losing_card")

    def __str__(self):
        return str(self.id) + ': ' + str(self.winner) + ' DEFEATED ' + str(self.loser)

    def get_absolute_url(self):
        return reverse('card-comparison-result-detail', args=[str(self.id)])

class CardRanking(models.Model):
    '''
    Model representing an Elo ranking for a specific card
    '''
    card = models.OneToOneField(Card, on_delete=models.CASCADE, primary_key=True)
    elo = models.IntegerField(default=ELO_DEFAULT, help_text="Enter the starting Elo for this card")

    def __str__(self):
        return self.card.name

    def get_absolute_url(self):
        '''returns the url to access a particular card ranking information'''
        return reverse('cardranking-detail', args=[self.pk])
        #currently is the ID. Since the cardRanking's primary key is currently ID.
        #If we change it to be reversed on the self.card.name, then we need to make the cardranking have
        #   a primary key of its name, but the only object we have is the card itself.
        #TODO: Either have the url accept the card object
        #   or
        #      Have the primary key be a card name

    @staticmethod
    def get_k_value(score):
        if score > 2400:
            return 16
        elif score >= 2100:
            return 24
        else:
            return 32 

    @staticmethod
    def calculate_elo_ranking(winner_score, loser_score):
        K1 = CardRanking.get_k_value(winner_score)
        K2 = CardRanking.get_k_value(loser_score)

        R1 = 10 ** (winner_score / 400)
        R2 = 10 ** (loser_score / 400)

        E1 = R1 / (R1 + R2)
        E2 = R2 / (R1 + R2)

        return (winner_score + K1 * (1 - E1), loser_score + K2 * (0 - E2))

    @staticmethod
    def adjust_elo_from_rankings(winner, loser):
        score_tuple = CardRanking.calculate_elo_ranking(winner.elo, loser.elo)
        winner.elo = score_tuple[0]
        loser.elo = score_tuple[1]
        winner.save()
        loser.save()

    @staticmethod
    def adjust_elo_from_cards(winner, loser):
        winner_ranking = CardRanking.objects.get(card=winner)
        loser_ranking = CardRanking.objects.get(card=loser)

        score_tuple = CardRanking.calculate_elo_ranking(winner_ranking.elo, loser_ranking.elo)
        winner_ranking.elo = score_tuple[0]
        loser_ranking.elo = score_tuple[1]

        winner_ranking.save()
        loser_ranking.save()