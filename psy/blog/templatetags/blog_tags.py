# from django import template
# from blog.models import *
#
# register = template.Library()
#
# @register.simple_tag(name='gettopics')
# def get_topics(filter=None):
#     if filter == None:
#         return Topic.objects.all()
#     else:
#         return Topic.objects.filter(pk=filter)

# @register.inclusion_tag('blog/show_topics.html')
# def show_topics(sort=None, topic_selected=0):
#     if not sort:
#         topics = Topic.objects.all()
#     else:
#         topics = Topic.objects.order_by(sort)
#     return {'topics': topics, 'topic_selected': topic_selected}