# Populi

This module interacts with the populi api, handling pagination, and rate limiting using pycurl.
Most every command found [here](https://support.populiweb.com/hc/en-us/articles/223798747#getAcademicTerms), can be accessed via pythonic methods. I have attempted to keep the two in sync

## Example
```python
import populi

populi.initialize(
    endpoint='https://example_campus.populi.web.com/api/index.php',
    access_key='example access key',
    asXML=True
)

# returns transactions as xml
results = populi.get_transactions(start_date='2012-10-01', end_date='2012,10-02')
```
