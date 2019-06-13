from django.utils.safestring import mark_safe
from functools import wraps


class Pagination(object):
    def __init__(self, current_pg: str, data_count: int, per_pg_count: int=10, list_count: int=11):
        """
        :param current_pg:      当前选中页
        :param data_count:      数据总条目数
        :param per_pg_count:    每一页显示的条目数
        :param list_count:      分页组件显示多少个选择框， 如list_count=5, 表示分页组件：  上一页 1 2 3 4 5 下一页
        """
        self.data_count = data_count
        self.per_pg_count = per_pg_count
        self.current_pg = self._current(current_pg)
        self.list_count = list_count
        self.list_left_count = (list_count >> 1) + 1
        self.list_right_count = list_count-self.list_left_count

    def _current(self, cur):
        try:
            current = int(cur)
            if current < 0:
                return 1
            elif current > self.pg_total:
                return self.pg_total
            else:
                return current
        except Exception:
            return 1

    @property
    def pg_total(self):                         # 总共有多少页
        d, m = divmod(self.data_count, self.per_pg_count)
        return d if not m else d+1              # 如果数据总条目数/每页显示的条目数恰好可以整除，那么总页数不需要加1

    @property
    def start(self):                            # 当前页第一个条目对应数据的索引值（索引从0开始）
        """除非数据总条目为0，否则，当前页肯定有条目的"""
        return (self.current_pg-1)*self.per_pg_count if self.data_count != 0 else 0

    @property
    def end(self):                              # 注意是前包后不包，因此end应该是最后一个条目加1
        """假设有96条数据，每页10条数据，那么第10页本来应该是90~99，即end=99;但是没有这么多的数据量， end只能是96（前包后不包）"""
        end = self.current_pg*self.per_pg_count
        return end if end <= self.data_count else self.data_count

    def pg_range(self):
        """
            1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
            如上，假设数据可以分为17页（self.pg_total=17）,分页组件显示5个框（self.list_count=5）
            那么经计算如果当前页大于3（即self.list_left_count=3）时，起始值不为1；
            如果当前页大于17-2（即self.pg_count-self.list_right_count）时，分页终点值始终为17
        """
        if self.pg_total <= 1:                  # 如果数据只需在一页内显示，那就无须分页,或者压根就没有数据
            return False
        elif self.pg_total <= self.list_count:  # 如规定self.list_count=11,即有11个框，但实际数据总分页数为3，那么只返回1, 2, 3
            return list(range(1, self.pg_total+1))                          # 注意range是左包又不包
        else:
            if self.current_pg <= self.list_left_count:
                end = self.list_count+1
                return [
                    *range(1, end),
                    "..." if self.pg_total > end else "",                   # 当末页比列表框大于1时，需插入'...'
                    self.pg_total]
            elif self.list_left_count < self.current_pg < self.pg_total-self.list_right_count:
                start = self.current_pg-self.list_left_count+1
                end = self.current_pg+self.list_right_count+1               # 注意，前包后不包，end实际取不到
                return [
                    1,
                    "..." if start > 2 else "",                             # 当列表框第一个比1时，需插入'...'
                    *range(start, end),
                    "..." if self.pg_total > end else "",                   # 当末页比列表框大于1时，需插入'...'
                    self.pg_total
                ]
            else:
                start = self.pg_total-self.list_count+1
                return [
                    1,
                    "..." if start > 2 else "",  # 当列表框第一个比1时，需插入'...'
                    *range(start, self.pg_total+1)]

    def gen_pagination(self, base_url, prev_val="<<", next_val=">>"):
        """
        当self.current_pg = 1时， 上一页框为禁止点击，当self.current_pg=self.pg_total，表示当前在最后一页，此时下一页框为禁止点击
        如： 上一页 1 ... 13 14 15 16 17 下一页
        :param base_url:
        :param prev_val: 指定页面上上一页框显示的文本内容
        :param next_val: 指定页面上下一页框显示的文本内容
        :return:         返回一个mark_safe()字符串
        """
        lst = self.pg_range()
        ret = []
        s = '?' if base_url.rfind('?') == -1 else '&'
        if lst is not False:
            ret.append("<li {}><a {}>{}</a></li>".format(
                "class='pagi-forbid pagi-prev'" if self.current_pg == 1 else "class='pagi-prev'",
                "" if self.current_pg == 1 else "href='{}{}p={}'".format(base_url, s, self.current_pg - 1),
                prev_val))
            for item in lst:
                if item == "...":
                    ret.append("<li class='pagi-inject'><a>...</a></li>")
                elif item == "":
                    continue
                else:
                    ret.append("<li {}><a href='{}{}p={}'>{}</a></li>".format(
                        "class='pagi-active'" if self.current_pg == item else "",
                        base_url,
                        s,
                        item,
                        item
                    ))
            ret.append("<li {}><a {}>{}</a></li>".format(
                "class='pagi-forbid pagi-next'" if self.current_pg == self.pg_total else "class='pagi-next'",
                "" if self.current_pg == self.pg_total else "href='{}{}p={}'".format(base_url, s, self.current_pg + 1),
                next_val))
        return mark_safe("<ul class='pagi'>{}</ul>".format(''.join(ret)))


"""
html使用： 使用<div class="article-pagination">{{ pagination }}</div> 将它包裹住
css样式如下：
.pagi li>a {
    display: inline-block;
    width: 30px;
    height: 30px;
    line-height: 30px;
    text-align: center;
    border: 1px solid #000;
    border-radius: 4px;
    margin-right: 5px;
    float: left;
}
.pagi .pagi-forbid>a{
    border: 1px solid #e8e8e8;
    color: #e8e8e8;
}
.pagi .pagi-inject>a{
    border: none;
}
.pagi .pagi-active>a {
    background-color: #3d97cb;
    color: white;
}
.pagi a:hover{
    text-decoration: none;
}
.pagi::after{
    content: '';
    display: block;
    clear: both;
}
"""


def pagify(base_url, model, order_field, *q, **condition):
    """
    :param base_url     生成分页的url前缀
    :param model:       模型类对象
    :param order_field: 需要排序的字段
    :param q:           filter如果需要使用q对象
    :param condition:   查询条件，关键字查询
    :return:
    """
    def _pagify(fn):
        @wraps(fn)
        def _wrap(request, *args, **kwargs):
            current_pg = request.GET.get('p', 1)
            data_count = model.objects.filter(*q, **condition).count()
            if data_count:
                per_pg_count = request.GET.get('pc', 10)
                list_count = 3
                p = Pagination(current_pg, data_count, per_pg_count, list_count)
                pagination = p.gen_pagination(base_url)
                lst = model.objects.filter(*q, **condition).order_by(order_field)[p.start: p.end]
            else:
                pagination = ""
                lst = []
            request.pagination = pagination
            request.lst = lst
            return fn(request, *args, **kwargs)
        return _wrap
    return _pagify

