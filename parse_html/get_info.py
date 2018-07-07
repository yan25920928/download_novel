from get_html.get_html_text import get_html_text
from lxml import etree


# 获取书本的说明信息和各个章节的URL
def get_info_and_chapter_url(one_book_url):
    # 本书目录信息
    book_info = {}
    # 得到URL的HTML文件
    book_html_text = get_html_text(one_book_url)
    # 得到书的标题
    title_res = html_parser(book_html_text, '//*[@id="info"]/h1/text()')
    if len(title_res):
        title = title_res[0]
        book_info["name"] = title
    else:
        return
    # 得到文章章节链接和章节名
    chapter_list = []
    chapter_nodes = html_parser(book_html_text, '//*[@id="list"]/dl/dd/a')
    for one in chapter_nodes:
        tmp = {}
        # 得到章节节点的标题
        chapter_name_res = one.xpath("text()")
        if len(chapter_name_res):
            chapter_name = chapter_name_res[0]
            tmp["chapter_name"] = chapter_name
        # 得到章节的url
        chapter_href_res = one.xpath("@href")
        if len(chapter_href_res):
            chapter_href = r"http://www.biquge.com.tw" + chapter_href_res[0]
            tmp["chapter_href"] = chapter_href
        chapter_list.append(tmp)
    # 重新组合信息
    book_info['chapter'] = chapter_list
    return book_info


def html_parser(html_text, compl_str):
    # 解析HTML文件
    tree = etree.HTML(html_text)
    res = tree.xpath(compl_str)
    return res