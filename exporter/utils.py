from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_html, context_dict={}):
    template = get_template(template_html)
    html = template.render(context_dict)
    result = BytesIO()
    pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    return result.getvalue()