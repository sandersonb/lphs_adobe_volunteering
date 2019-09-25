import logging
import urllib.request
from urllib.error import URLError
from urllib.parse import quote

_STATS_ENDPOINT = 'https://blmlonepeak2019.sc.omtrdc.net'
_REPORT_SUITE_ID = 'blm.lonepeak2019'
_log = logging.getLogger(__name__)


def track(page_name: str, studentid: str, function_input: str, function_output: str):
    url = "%s/b/ss/%s/2/PY3/s12345?AQB=1&vid=%s&pageName=%s&c1=%s&c2=%s&c3=%s&pccr=true&AQE=1" % \
          (_STATS_ENDPOINT, quote(_REPORT_SUITE_ID), quote(studentid), quote(page_name), quote(studentid),
           quote(function_input), quote(function_output))

    request = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
    )

    try:
        with urllib.request.urlopen(request) as f:
            response = f.read().decode('utf-8')
            _log.debug("Tracked %s = %s" % (url, response))
    except URLError as ue:
        _log.error("Error sending track call: reason=%s filename=%s" % (ue.reason, ue.filename))
