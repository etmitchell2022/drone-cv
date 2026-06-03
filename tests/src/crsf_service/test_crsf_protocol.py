import pytest
from src.crsf_service.crsf_protocol import CRSFProtocol
from src.crsf_service.exceptions import InvalidChannelCountError, InvalidChannelValueError

class TestCRSFProtocol:
    def setup_method(self):
        self.protocol = CRSFProtocol()

    def test_valid_channels(self):
        channels = [992] * 16  # All channels at center value
        frame = self.protocol.build_rc_channels_frame(channels)
        assert isinstance(frame, bytes)
        assert len(frame) == 26  # 3 bytes for header, 22 for payload, 1 for CRC

    def test_too_few_channels(self):
        with pytest.raises(InvalidChannelCountError):
            self.protocol.build_rc_channels_frame([992] * 15)
    
    def test_too_many_channels(self):
        with pytest.raises(InvalidChannelCountError):
            self.protocol.build_rc_channels_frame([992] * 17)

    def test_channel_value_too_high(self):
        with pytest.raises(InvalidChannelValueError):
            self.protocol.build_rc_channels_frame([992] * 15 + [1812])
    
    def test_channel_value_too_low(self):
        with pytest.raises(InvalidChannelValueError):
            self.protocol.build_rc_channels_frame([992] * 15 + [171])