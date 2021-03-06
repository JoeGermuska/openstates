import datetime
from billy.utils.fulltext import pdfdata_to_text, text_after_line_numbers

metadata = {
    "capitol_timezone": 'America/Chicago',
    "terms": [
        {
            "name": "2008-2011",
            "start_year": 2008,
            "end_year": 2011,
            "sessions": [
                "2009",
                "2010",
                "2011 1st Extraordinary Session",
                "2011"
                ]
        },
        {
            "name": "2012-2015",
            "start_year": 2012,
            "end_year": 2015,
            "sessions": [
                "2012",
                "2013",
                ]
        }
    ],
    "name": "Louisiana",
    "legislature_url": "http://www.legis.la.gov/",
    "abbreviation": "la",
    "session_details": {
        "2009": {
            "type": "primary",
            "start_date": datetime.date(2010, 4, 27),
            "end_date": datetime.date(2010, 6, 24),
            'display_name': '2009 Regular Session',
            '_scraped_name': '2009 Regular Session'
        },
        "2010": {
            "type": "primary",
            "start_date": datetime.date(2010, 3, 29),
            "end_date": datetime.date(2010, 6, 21),
            'display_name': '2010 Regular Session',
            '_scraped_name': '2010 Regular Session',
        },
        "2011 1st Extraordinary Session": {
            "type": "special",
            "_id": "111es",
            'display_name': '2011, 1st Extraordinary Session',
            '_scraped_name': '2011 First Extraordinary Session',
        },
        "2011": {
            "type": "primary",
            'display_name': '2011 Regular Session',
            '_scraped_name': '2011 Regular Session',
        },
        "2012": {
            "type": "primary",
            'display_name': '2012 Regular Session',
            '_scraped_name': '2012 Regular Session',
        },
        "2013": {
            "type": "primary",
            'display_name': '2013 Regular Session',
            '_scraped_name': '2013 Regular Session',
        },
    },
    "legislature_name": "Louisiana Legislature",
    'chambers': {
        'upper': {'name': 'Senate', 'title': 'Senator'},
        'lower': {'name': 'House', 'title': 'Representative'},
    },
    'feature_flags': ['subjects', 'events', 'influenceexplorer'],
    '_ignored_scraped_sessions': [
        '2008 Regular Session',
        '2008 Organizational Session',
        '2008 Second Extraordinary Session',
        '2008 First Extraordinary Session',
        '2007 Regular Session',
        '2006 Regular Session',
        '2005 Regular Session',
        '2004 Regular Session',
        '2004 1st Extraordinary Session',
        '2003 Regular Session',
        '2002 Regular Session',
        '2001 Regular Session',
        '2000 Regular Session',
        '1999 Regular Session',
        '1998 Regular Session',
        '1997 Regular Session',
        '2006 Second Extraordinary Session',
        '2006 First Extraordinary Session',
        '2005 First Extraordinary Session',
        '2002 First Extraordinary Session',
        '2001 Second Extraordinary Session',
        '2001 First Extraordinary Session',
        '2000 Second Extraordinary Session',
        '2000 First Extraordinary Session',
        '1998 First Extraordinary Session'
    ]
}


def session_list():
    from billy.scrape.utils import url_xpath
    import re
    return url_xpath(
                'http://www.legis.la.gov/Legis/SessionInfo/SessionInfo.aspx',
                '//select//option/text()')


def extract_text(doc, data):
    return text_after_line_numbers(pdfdata_to_text(data))
