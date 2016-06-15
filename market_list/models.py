from django.db import models


# Create your models here.
class InsuranceQuote(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return " ".join([str(self.name), str(self.price)])


class CompetitionRequest(models.Model):
    FALLBACK_RULES = (
        ('SH', 'Shift'),
        ('WD', 'Withdraw')
    )
    name = models.CharField(max_length=200)
    working_price = models.IntegerField()
    target_position = models.IntegerField()
    fallback_rule = models.CharField(max_length=2, choices=FALLBACK_RULES)
    max_working_price_reduction = models.FloatField()
    working_price_reduction_interval = models.FloatField()

    def __str__(self):
        return "{0}, {1} EUR, Pos {2}".format(self.name, self.working_price,
                                              self.target_position)


def fill_default_market_list():
    InsuranceQuote.objects.all().delete()

    a = InsuranceQuote(name="Aachener", price=44.)
    a.save()

    b = InsuranceQuote(name="Berliner", price=45.)
    b.save()

    c = InsuranceQuote(name="Chemnitzer", price=46)
    c.save()

    d = InsuranceQuote(name="Dortmunder", price=47.)
    d.save()


def process_competition_request(comp_req):
    """ Sort request into market list

    :param request CompetitionReqeuest:
    :return:
    """
    market_data = InsuranceQuote.objects.order_by('price')

    if not market_data:
        # empty list?
        new_entry = InsuranceQuote(comp_req.name, comp_req.working_price)
        new_entry.save()

    for position, entry in enumerate(market_data):
        if position == comp_req.target_position:
            if comp_req.working_price - comp_req.max_working_price_reduction < entry.price:
                # it is possible to reduce
                new_price = comp_req.working_price
                while new_price >= entry.price:
                    new_price = new_price - comp_req.working_price_reduction_interval
                new_entry = InsuranceQuote(name=comp_req.name, price=new_price)
                new_entry.save()
                break  # all done
            else:
                # fail. fallback?
                if comp_req.fallback_rule == 'SH':
                    comp_req.target_position += 1
                    if comp_req.target_position == len(market_data):
                        # no one to compare to, end of the list
                        new_entry = InsuranceQuote(name=comp_req.name, price=comp_req.working_price)
                        new_entry.save()
                        break
                    else:
                        process_competition_request(comp_req)
                        break
                else:
                    break
