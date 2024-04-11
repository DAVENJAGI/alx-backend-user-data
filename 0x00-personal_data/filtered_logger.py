#!/usr/bin/env python3
"""
Handling user data
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''A function that returns log message obfuscated'''
    return re.sub('|'.join(map(re.escape, fields)), redaction, message)
