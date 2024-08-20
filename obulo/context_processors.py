from django.conf import settings


def googleanalytic(request):
    return {'G_ANALYTIC_CODE': settings.G_ANALYTIC_CODE}
