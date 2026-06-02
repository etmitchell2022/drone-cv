

class CRSFError(Exception):
    """Base class for all CRSF exceptions."""
    pass

class InvalidChannelCountError(CRSFError):
    """Raised when the number of channels is not 16."""
    pass