import blog.models as m_blog


def get_main_category():
    """
    获取主分类
    :return:
    """
    category_data = dict()
    categories = list(m_blog.Category.objects.filter(parent_id=0).values('id', 'name', 'style'))
    category_data[1] = filter(lambda sa: sa['style'] == 1, categories)
    category_data[2] = filter(lambda sa: sa['style'] == 2, categories)
    category_data[3] = filter(lambda sa: sa['style'] == 3, categories)

    return category_data


def get_sub_category(pid):
    """
    获取子分类
    :param pid:主分类ID
    :return:
    """

    return m_blog.Category.objects.filter(parent_id=0).values('id', 'name', 'style')


def get_tags():
    """
    标签列表
    :return:
    """
    return m_blog.Tag.objects.all()


def get_articles_by_category(category_id):
    """
    根据类别ID 获取文章
    :param category_id:
    :return:
    """
    return m_blog.Category.objects.get(id=category_id).article_set.all()
