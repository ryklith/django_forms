from django.db import models


# Create your models here.
class MarketListEntry(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    position = models.IntegerField()


class CompetitionRequest(models.Model):
    FALLBACK_RULES = (
        ('SH', 'Shift'),
        ('WD', 'Withdraw')
    )
    name = models.CharField(max_length=200)
    working_price = models.IntegerField()
    target_position = models.IntegerField()
    fallback_rule = models.CharField(max_length=1, choices=FALLBACK_RULES)
    working_price_reduction_interval = models.FloatField()

    def __str__(self):
        return "{0}, {1} EUR, Pos {2}".format(self.name, self.working_price,
                                              self.target_position)


def fill_default_market_list():
    MarketListEntry.objects.all().delete()

    a = MarketListEntry(name="Aachener", price=44., position=0)
    a.save()

    b = MarketListEntry(name="Berliner", price=45., position=1)
    b.save()

    c = MarketListEntry(name="Chemnitzer", price=46., position=2)
    c.save()

    d = MarketListEntry(name="Dortmunder", price=47., position=3)
    d.save()


def add_market_entry(name="", price=0, position=100):
    a = MarketListEntry(name=name, price=price, position=position)
    a.save()