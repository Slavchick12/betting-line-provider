"""Enum models."""

from enum import Enum


class EventStatusEnum(str, Enum):
    """Event statuses enum."""

    scheduled = 'Scheduled'
    in_progress = 'In progress'
    half_time = 'Half time'
    FIRST_WIN = 'First win'
    SECON_WIN = 'Second win'
    DRAW = 'Draw'
    canceled = 'Canceled'
