from django.db import models
import datetime


class BaseModel(models.Model):
    id = models.BigAutoField('主键', db_column='id', primary_key=True)
    create_time = models.DateTimeField('创建时间', db_column='create_time', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', db_column='update_time', auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    """
    文章类别
    """
    STYLE = ((0, '分隔符'), (1, '固定'), (2, '主要'), (3, '折叠'),)

    parent = models.ForeignKey('self', verbose_name='父id', db_column='pid', on_delete=models.CASCADE)
    name = models.CharField('名称', db_column='name', max_length=50)
    style = models.IntegerField('呈现样式', db_column='style', choices=STYLE)
    sort = models.IntegerField('顺序', db_column='sort', default=1)

    def save(self, *args, **kwargs):
        """
        保证类别只有两个层级
        :param args:
        :param kwargs:
        :return:
        """
        if self.parent.id and self.parent.parent.id and self.parent.parent.parent.id:
            raise Exception('文章只支持三个层级的类别')

        super(Category, self).save(*args, **kwargs)

    class Meta:
        db_table = "category"
        ordering = 'sort'


class Tag(BaseModel):
    """
    标签
    """
    name = models.CharField('名称', db_column='name', null=False, max_length=50)

    class Meta:
        db_table = 'tag'


class Article(BaseModel):
    """
    文章
    """

    STATUS = ((0, '草稿'),
              (1, '发布'),
              (2, '归档'))

    title = models.CharField('标题', db_column='title', max_length=200);
    content = models.TextField('内容', db_column='content')
    category = models.ForeignKey(Category, verbose_name='类型', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, verbose_name='标签', null=True)

    image = models.ImageField('图片', db_column='image')
    view_count = models.IntegerField('浏览次数', db_column='view_count', default=0)
    status = models.IntegerField('状态', db_column='status', choices=STATUS)

    class Meta:
        db_table = 'article'

    @property
    def update_time_str(self):
        delta = (datetime.datetime.now() - self.update_time)

        if delta.days > 30:
            return delta.days / 30 + '月前'
        elif delta.days > 0:
            return delta.days + '天前'
        elif delta.seconds > 3600:
            return delta.seconds / 3600 + '小时前'
        elif delta.seconds > 60:
            return delta.seconds / 60 + '分钟前'
        elif delta.seconds > 0:
            return delta.seconds + '秒前'
        else:
            return '刚刚'
