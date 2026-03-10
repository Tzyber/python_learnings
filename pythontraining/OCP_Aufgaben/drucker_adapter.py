class Alter_Drucker:
    def print_text(self, text_string):
        print(f"Drucker druckt: {text_string}")


class PrintAdapter:
    def __init__(self, alter_drucker):
        self.alter_drucker = alter_drucker

    def print_document(self, doc_object):
        text = f"{doc_object['title']} - {doc_object['content']}"
        self.alter_drucker.print_text(text)


def main():
    adapter = PrintAdapter(Alter_Drucker())
    mein_dokument = {"title": "Rechnung", "content": "Bitte zahlen Sie 50 Euro."}
    adapter.print_document(mein_dokument)


if __name__ == "__main__":
    main()