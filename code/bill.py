"""Reusable calculations for the Bill Splitter interfaces."""


def tip_amount(subtotal, pct):
    """Return the tip amount, rounded to the nearest cent."""
    return round(subtotal * pct / 100, 2)


def grand_total(subtotal, pct):
    """Return the subtotal plus the tip, rounded to cents."""
    return round(subtotal + tip_amount(subtotal, pct), 2)


def split_evenly(total, people):
    """Return each person's share; reject zero or negative people."""
    if people <= 0:
        raise ValueError("people must be greater than 0")
    return round(total / people, 2)


def is_generous(pct):
    """Return True if the tip percentage is at least 20."""
    return pct >= 20
