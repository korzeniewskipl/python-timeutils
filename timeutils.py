"""Timeutils."""

import calendar
import datetime
import pytz

unix_epoch = pytz.utc.localize(datetime.datetime(1970, 1, 1))


def unix_timestamp(value):
    """Return Unix timestamp for the given ``datetime.datetime``.

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

    :return: Unix timestamp.
    :rtype: int

    :raises ValueError: If passed date is earlier than 1970-01-01.

    """
    timestamp = calendar.timegm(value.utctimetuple())
    if timestamp < 0:
        raise ValueError("Date can't be earlier than 1970-01-01 ({0})".format(value))
    return timestamp
