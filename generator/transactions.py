"""Utilities to model money transactions."""

from random import choices, randint
from string import ascii_letters, digits
from typing import NamedTuple

account_chars: str = digits + ascii_letters


def _random_account_id():
    return ''.join(choices(account_chars, k=12))


class Transaction(NamedTuple):
    """Represents a transaction."""

    source: str
    target: str
    amount: float
    currency: str

    @classmethod
    def random(cls):
        """Create a random transaction."""
        return cls(
            # Fake source and target account numbers
            source=_random_account_id(),
            target=_random_account_id(),
            # Random amount between 1.00 and 1000.00
            amount=randint(100, 100000) / 100,
            currency='EUR',
        )

    def serialize(self) -> str:
        return self._asdict()
