from unittest import TestCase

from src.CsrankingSpider.processor import extract_page_text


class TestProcessor(TestCase):
    def test_extract_text(self):
        test_string = '''
        <html>
            <body>
                <p>233</p>
                <p>444</p>
                <br></br>
            </body>
        </html>
        '''
        print(extract_page_text(test_string))
