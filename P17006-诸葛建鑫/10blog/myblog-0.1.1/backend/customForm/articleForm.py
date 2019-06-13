from django.forms import Form, fields, widgets
from django.core.exceptions import ValidationError
from web import models as web_models


class ArticleForm(Form):
    title = fields.CharField(
        max_length=128, required=True, label='标题(必填，128个字符以内)',
        widget=widgets.TextInput(attrs={"class": "form-control"}),
        error_messages={'invalid': '标题长度过长', 'required': '标题不能为空'}
    )
    summary = fields.CharField(
        max_length=255, required=True, label="摘要(必填，文章摘要，255个字符以内)",
        widget=widgets.Textarea(attrs={"class": "form-control", "rows": 3}),
        error_messages={'invalid': '摘要长度过长', 'required': '摘要不能为空'}
    )
    content = fields.CharField(
        required=False, label="正文",
        widget=widgets.Textarea(attrs={"class": "form-control kind-editor", "rows": 40})
    )
    category_id = fields.ChoiceField(
        choices=[], required=False, label="文章分类",
        widget=widgets.RadioSelect(),
        error_messages={"invalid": "该分类不存在"}
    )
    tag_id = fields.MultipleChoiceField(
        choices=[], required=False, label="文章标签",
        widget=widgets.CheckboxSelectMultiple(),
        error_messages={"invalid": "该标签不存在"}
    )
    new_tag = fields.CharField(
        required=False, label="使用新的标签(多个关键字之间用英文“,”分隔，最多不超过10个)",
        widget=widgets.TextInput(attrs={"class": "form-control"}),
    )
    webplate_id = fields.ChoiceField(
        choices=[], required=False, label="网站分类",
        widget=widgets.RadioSelect(),
        error_messages={"invalid": "该网站分类不存在"},
    )

    def __init__(self, request, *args, **kwargs):
        """
        :param bid:     bid为blog账户的id
        :param aid:     aid为该blog下某篇文章的id，如果是添加文章aid=None, 如果是修改文章，aid不为None
        :param args:    其基类Form的位置参数
        :param kwargs:  其基类Form的关键字参数
        """
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.bid = request.logged_blog.nid
        self.fields['webplate_id'].choices = web_models.WebPlate.objects.values_list('nid', 'title')
        self.fields['category_id'].choices = web_models.Category.objects.filter(
            blog_id=self.bid).values_list('nid', 'title')
        self.fields['tag_id'].choices = web_models.Tag.objects.filter(blog_id=self.bid).values_list('nid', 'title')

    def clean_new_tag(self):
        """
            new_tag是用户新增的tag，要求以逗号分隔，不能为空，检查是否和用户已有的标签tag_dic存在重复：
                如果重复则不创建Tag类实例，但是将它添加到返回列表中
                如果不重复，且不为空，创建Tag类实例，同时将它添加到返回列表中
        :return: 返回列表，列表中的元素是需要和Article类实例创建对对多关系的。
        """
        data = self.cleaned_data.get("new_tag", "")
        new_tag_lst = data.strip().split(',')
        length = len(new_tag_lst)
        if not length:
            return []
        elif length > 10:
            raise ValidationError('新增便签长度超过10个')
        try:
            new_tag_set = set([nt.strip() for nt in new_tag_lst])
            tags = web_models.Tag.objects.filter(blog_id=self.bid).only("title", 'nid')
            tag_dic = {tag.title: tag.nid for tag in tags}
            ret = []
            for nt in new_tag_set:
                if nt in tag_dic:
                    ret.append(tag_dic[nt])
                elif nt and nt not in tag_dic:      # 当标签不为空字符串，且数据库中没有该tag时，添加该tag
                    t = web_models.Tag.objects.create(title=nt, blog_id=self.bid)
                    ret.append(t.nid)
            return ret
        except:
            raise ValidationError("添加的新标签有误，请修改后重试")
