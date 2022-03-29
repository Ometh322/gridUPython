"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
"""
import re


def is_http_domain(domain: str) -> bool:
    ans = re.match('\Ahttp(s{0,1})://(\w+\.)+\w+(/{0,1})', domain)
    current_url: str = ''
    if ans:
        current_url = ans.group(0)
    else:
        current_url = ''
    return current_url == domain


"""
write tests for is_http_domain function
"""
