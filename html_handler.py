from bs4 import BeautifulSoup

class HtmlHandler:
    html_doc = None
    
    def __init__(self, html_response: str):
        self.html_doc = html_response
    
    def get_lyrics(self) -> str:
        soup = BeautifulSoup(self.html_doc, 'html.parser')
        for tabel in soup.find_all("div", {"class": "pg-detail-block-items"}):
            # print(tabel.prettify())
            try:
                payer = tabel.find(text='Payer').find_next(class_='pg-detail-item-value').text.strip()
                payer_account = tabel.find(text="Payer's account").find_next(class_='pg-detail-item-value').text.strip()
                target_account = tabel.find(text='Target account').find_next(class_='pg-detail-item-value').text.strip()
                value_date = tabel.find(text='Value date').find_next(class_='pg-detail-item-value').text.strip()
                amount = tabel.find(text='Amount in original currency').find_next(class_='pg-detail-item-value').text.strip()
                transaction_type = tabel.find(text='Transaction type').find_next(class_='pg-detail-item-value').text.strip()
                print("====================")
                print(payer, payer_account, target_account, value_date, amount, transaction_type)
                print("====================")
            except Exception as e:
                pass
        # print(soup.prettify())
        pass
    