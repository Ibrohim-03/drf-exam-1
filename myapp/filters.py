
from django.db.models import Q


def filter_posts(posts, params):
    search = params.get('search')
    min_views = params.get('min_views')
    max_views = params.get('max_views')
    user_id = params.get('user_id')

    if search:
        posts = posts.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search)
        )

    if min_views:
        posts = posts.filter(views__gte=min_views)

    if max_views:
        posts = posts.filter(views__lte=max_views)

    if user_id:
        posts = posts.filter(user_id=user_id)

    return posts
