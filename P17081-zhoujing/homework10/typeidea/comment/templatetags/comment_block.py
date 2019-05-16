from django import template

from comment.form import CommentForm
from comment.models import Comment

register = template.Library()

@register.inclusion_tag('comment/block.html')
def comment_block(target):
    print(target,'~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return {
        'target':target,
        'comment_form':CommentForm(),
        'comment_list':Comment.get_by_target(target)
    }
