from metric import TEDS
from bs4 import BeautifulSoup
from examples import y_pred_html, y_true_html

def clean_html(html_):
    def replace_html_attr(html_):
        tag_list = ["<thead>", "</thead>", "<tbody>", "</tbody>", "<sup>", "</sup>", "<sub>", "</sub>", "\xa0", "<p>", "</p>", 'colspan="1"', 'colspan="4"', 'rowspan="1"', 'colspan="0"', 'rowspan="0"']
        for tag in tag_list:
            html_ = html_.replace(tag, "")
        html_ = html_.replace("<th","<td")
        html_ = html_.replace("</th>","</td>")
        return html_
    html_ = ' '.join(html_.split())
    return replace_html_attr(html_)

y_pred_html = clean_html(y_pred_html)
y_true_html = clean_html(y_true_html)
    
teds = TEDS()
print(f"The ted score of html structure : {teds.evaluate(y_pred_html,y_true_html, True)}")
print(f"The ted score of html table     : {teds.evaluate(y_true_html,y_pred_html)}")
