import docwow

with open("report_template.html", "r", encoding="utf-8") as f:
    html = f.read()

docwow.to_docx(
    html,
    "output.docx",
    is_foreign_html=True
)
