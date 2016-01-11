import requests
from lxml import html

MODELS = {
    'biutee': '-config biutee/biutee/biutee.xml',
    'edit-distance': '-config eop-resources-demo-configs-1.2.0/EditDistanceEDA_EN/EditDistanceEDA_EN.xml',
    'edit-distance-wordnet': '-config eop-resources-demo-configs-1.2.0/EditDistanceEDA_EN_WordNet/EditDistanceEDA_EN_WordNet.xml',
    'maxent-all': '-config eop-resources-demo-configs-1.2.0/MaxEntClassificationEDA_Base-WN-VO-TP-TPPos-TS_EN/MaxEntClassificationEDA_Base-WN-VO-TP-TPPos-TS_EN.xml',
    'maxent-verbocean': '-config eop-resources-demo-configs-1.2.0/MaxEntClassificationEDA_Base-VO-TP-TPPos-TS_EN/MaxEntClassificationEDA_Base-VO-TP-TPPos-TS_EN.xml',
    'maxent-wordnet': '-config eop-resources-demo-configs-1.2.0/MaxEntClassificationEDA_Base-WN-TP-TPPos-TS_EN/MaxEntClassificationEDA_Base-WN-TP-TPPos-TS_EN.xml',
    'pieda': '-config eop-resources-demo-configs-1.2.0/P1EDA_EN/P1EDA_Base_EN.xml',
}


def query(text, hypothesis, model='pieda'):
    base_url = "http://hlt-services4.fbk.eu/eop/"

    payload = {
        'languages': '',
        'configuration': MODELS[model],
        'ttext': text,
        'htext': hypothesis,
    }

    response = requests.get(base_url + 'runSystem.php', params=payload)

    elt = html.fromstring(response.text)
    report_url = elt.get_element_by_id('resu').value.strip()
    report_xml = requests.get(base_url + report_url).text

    # output of the biutee model breaks lxml's parsing
    encoding_str = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    report_xml = report_xml.replace(encoding_str, '')
    report_xml = html.fromstring(report_xml).get_element_by_id('1')

    entailment = report_xml.get('entailment')
    confidence = float(report_xml.get('confidence'))
    return confidence, entailment
