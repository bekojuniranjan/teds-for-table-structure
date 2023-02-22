from metric import TEDS
import re 
from bs4 import BeautifulSoup
from examples import y_pred_html, y_true_html
def replace_html_attr(text_):
    gt_html = text_

    gt_html = gt_html.replace("<thead>","")
    gt_html = gt_html.replace("</thead>","")
    gt_html = gt_html.replace("<tbody>","")
    gt_html = gt_html.replace("</tbody>","")
    gt_html = gt_html.replace("<sup>","")
    gt_html = gt_html.replace("</sup>","")
    gt_html = gt_html.replace("<sub>","")
    gt_html = gt_html.replace("</sub>","")
    gt_html = gt_html.replace("\xa0","")
    gt_html = gt_html.replace("<p>","")
    gt_html = gt_html.replace("</p>","")
    gt_html = gt_html.replace("<th","<td")
    gt_html = gt_html.replace("</th>","</td>")
    gt_html = gt_html.replace('colspan="1"',"")
    gt_html = gt_html.replace('colspan="4"',"")
    gt_html = gt_html.replace('rowspan="1"',"")
    gt_html = gt_html.replace('colspan="0"',"")
    gt_html = gt_html.replace('rowspan="0"',"")
    return gt_html


y_true_html = ' '.join(y_true_html.split())
y_pred_html = ' '.join(y_pred_html.split())

y_true_html = replace_html_attr(y_true_html)
y_pred_html = replace_html_attr(y_pred_html)


def get_table_structure(html_):
    bs_data = BeautifulSoup(html_, 'html.parser')
    for i in bs_data.find_all('td'):
        i.string = 'a'
    return str(bs_data)
    
y_true_html_structure = get_table_structure(y_true_html)
y_pred_html_structure = get_table_structure(y_pred_html)
teds = TEDS()
print(f"The ted score of html structure : {teds.evaluate(y_true_html_structure,y_pred_html_structure)}")
print(f"The ted score of html table     : {teds.evaluate(y_true_html,y_pred_html)}")
