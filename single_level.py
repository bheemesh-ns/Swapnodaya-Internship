class Book:
    def __init__(abc, title="NONE", author="NONE"):
        abc.title = title
        abc.author = author
    def display_book_details(abc):
        return f"Title: {abc.title}, Author: {abc.author}"    

class IssuedBook(Book):
    def __init__(abc, title, author, issued_to="NONE", issue_date="NONE"):
        super().__init__(title, author)
        abc.issued_to = issued_to
        abc.issue_date = issue_date

    def display_issued_book_details(abc):
        return (f"Title: {abc.title}, Author: {abc.author}, Issued To: {abc.issued_to}, issue Date: {abc.issue_date}")

obj = IssuedBook("India that is Bharat", "J Sai Deepak", "Bheemesh N S", "04-02-2026")   
print(obj.display_issued_book_details())
print(obj.display_book_details())