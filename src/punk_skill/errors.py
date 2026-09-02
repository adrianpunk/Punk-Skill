class PunkError(Exception):
    """Base error shown by the Punk command-line interface."""


class PunkValidationError(PunkError):
    """Raised when repository data or a generation job is invalid."""

