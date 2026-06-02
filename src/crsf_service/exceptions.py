class CRSFError(Exception):
    """Base class for all CRSF exceptions."""

    pass


class InvalidChannelCountError(CRSFError):
    """Raised when the number of channels is not 16."""

    pass


class InvalidChannelValueError(CRSFError):
    """Raised when a channel value is out of the valid range (172-1811)."""

    pass
