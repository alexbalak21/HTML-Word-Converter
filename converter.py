import docwow

html = open("page.html").read()

docwow.to_docx(
    html,
    "output.docx",
    is_foreign_html=True   # important for arbitrary HTML
)
