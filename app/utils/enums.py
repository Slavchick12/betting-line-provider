"""Enum models."""

from enum import Enum


class EventStatusEnum(str, Enum):
    """Event statuses enum."""

    in_progress = 'In progress'
    win = 'Win'
    loss = 'Loss'
