from django.db.models import Count
from django.db.models.functions import TruncDay

from core.models import PostsFeedBack


def get_like_analytics(date_from, date_to):
    """
    Implements statistics of likes in day.
    :return: list which contains dicts with statistics values.
    """
    queryset = PostsFeedBack.objects.filter(created__range=[date_from, date_to])
    likes = queryset.filter(like=True)
    likes_in_day = likes.annotate(day=TruncDay('created')).values('day') \
        .annotate(count=Count('id')).values('day', 'count')
    return likes_in_day
