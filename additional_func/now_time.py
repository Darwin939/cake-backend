#!/bin/env python3

from datetime import datetime,timezone

def time():
    dt = datetime.utcnow()
    now_time = dt.replace(tzinfo=timezone.utc).timestamp()
    return now_time