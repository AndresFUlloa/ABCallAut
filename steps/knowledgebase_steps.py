from behave import when, then

from pages.knowledegebase_articles_page import KnowledgebaseArticlesPage


@when('user search article "{search_text}"')
def search_article(context, search_text: str):
    context.knowledgebase_articles_page = KnowledgebaseArticlesPage()
    context.knowledgebase_articles_page.input_search(search_text)
    context.knowledgebase_articles_page.click_on_search()
    context.knowledgebase_articles_page.wait_spinner_fade_out()


@then('there must be articles')
def must_be_articles(context):
    context.knowledgebase_articles_page = KnowledgebaseArticlesPage()
    context.knowledgebase_articles_page.click_on_see_more(1)
    element = context.knowledgebase_articles_page.get_content(1)
    assert element.is_displayed(), "There are no articles"
    assert len(element.text) > 0, "Article has no content"
