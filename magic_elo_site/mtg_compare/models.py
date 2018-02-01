from django.db import models

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
    card = models.OneToOneField(Card, on_delete=models.CASCADE)
    elo = models.IntegerField(default=ELO_DEFAULT, help_text="Enter the starting Elo for this card")

    def __str__(self):
        return self.card.name
