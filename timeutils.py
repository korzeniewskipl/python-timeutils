"""Timeutils."""

import calendar


def unix_timestamp(value):
    """Return UNIX timestamp for the given ``datetime.datetime``.

    Examples:
        >>> import datetime
        >>> import pytz
        >>> naive_dt = datetime.datetime(2014, 8, 3, 20, 34, 10)
        >>> naive_dt
        datetime.datetime(2014, 8, 3, 20, 34, 10)
        >>> unix_timestamp(naive_dt)
        1407098050
        >>> utc_dt = pytz.utc.localize(naive_dt)
        >>> utc_dt
        datetime.datetime(2014, 8, 3, 20, 34, 10, tzinfo=<UTC>)
        >>> unix_timestamp(utc_dt)
        1407098050
        >>> eu_dt = pytz.timezone('Europe/Warsaw').normalize(utc_dt)
        >>> eu_dt
        datetime.datetime(2014, 8, 3, 22, 34, 10, tzinfo=<DstTzInfo 'Europe/Warsaw' CEST+2:00:00 DST>)
        >>> unix_timestamp(eu_dt)
        1407098050

    :param value: ``datetime.datetime`` object.

    :return: UNIX timestamp.
    :rtype: int

    """
    return calendar.timegm(value.utctimetuple())
