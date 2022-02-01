from typing import List
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from locators.quote_page_locators import QuotePageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [QuoteParser(e) for e in self.browser.find_elements_by_css_selector(QuotePageLocators.QUOTE)]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(QuotePageLocators.AUTHOR_DROPDOWN)
        return Select(element)

    @property
    def tags_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(QuotePageLocators.TAG_DROPDOWN)
        return Select(element)

    @property
    def search_btn(self):
        return self.browser.find_element_by_css_selector(QuotePageLocators.SEARCH_BUTTON)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]

    def select_tag(self, tag: str):
        self.tags_dropdown.select_by_visible_text(tag)

    def search_for_quotes(self, author_name: str, tag: str) -> List[QuoteParser]:
        self.select_author(author_name)
        try:
            self.select_tag()
        except NoSuchElementException:
            raise InvalidTagForAuthorError(f'Author {author_name} has nothing under {tag}')
        self.search_btn.click()
        return self.quotes


class InvalidTagForAuthorError(ValueError):
    pass
