from selenium import webdriver

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:
    author = input('Enter the author: ')
    selected_tag = input('Enter the tag: ')


    chrome = webdriver.Chrome(executable_path=r'Users\44775\Desktop\chromedriver')
    chrome.get('http://quotes.toscrape.com\search.aspx')
    page = QuotesPage(chrome)

    # page.select_author(author)

    # tags = page.get_available_tags()
    # print('Pick one tag [{}]'.format(" / ").join(tags))

    # page.select_tag(selected_tag)
    # page.search_btn.click()

    print(page.search_for_quotes(author, selected_tag))

    # print(page.quotes)
except InvalidTagForAuthorError as e:
    pass
except Exception as e:
    print(e)
    print('Unkown error')