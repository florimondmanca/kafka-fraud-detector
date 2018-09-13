"""Utilities to model money transactions."""

from random import choices, randint
from string import ascii_letters, digits
from typing import NamedTuple

account_chars: str = digits + ascii_letters


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
            source=choices(account_chars, k=12),
            target=choices(account_chars, k=12),
            # Random amount between 1.00 and 1000.00
            amount=randint(100, 1000000) / 100,
            currency='EUR',
        )

    def serialize(self) -> str:
        return self._asdict()
