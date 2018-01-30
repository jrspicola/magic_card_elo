from django.contrib import admin
from .models import CardSet, CardColor, CardType, Card, CardComparison, CardComparisonResult, CardRanking

admin.site.register(CardSet)
admin.site.register(CardColor)
admin.site.register(CardType)
admin.site.register(CardRanking)

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
	list_display = ('name', 'card_color_display', 'card_type_display', 'cmc')
	list_filter = ('cardColor', 'cardType', 'cardSet')

@admin.register(CardComparison)
class CardComparisonAdmin(admin.ModelAdmin):
	list_display = ('id', 'leftCard', 'rightCard')

@admin.register(CardComparisonResult)
class CardComparisonResultAdmin(admin.ModelAdmin):
	list_display = ('id', 'winner', 'loser')