from locators.quote_locators import QuoteLocators


class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Content: {self.content} by {self.author}.'

    @property
    def content(self):
        content = QuoteLocators.CONTENT
        return self.parent.find_element_by_css_selector(content).text

    @property
    def author(self):
        author = QuoteLocators.AUTHOR
        return self.parent.find_element_by_css_selector(author).text

    @property
    def tags(self):
        tags = QuoteLocators.TAGS
        return self.parent.find_elements_by_css_selector(tags)