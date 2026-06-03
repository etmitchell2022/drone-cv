import pytest
from src.crsf_service.crsf_protocol import CRSFProtocol
from src.crsf_service.exceptions import InvalidChannelCountError, InvalidChannelValueError

class TestCRSFProtocol:
    def setup_method(self):
        self.protocol = CRSFProtocol()

    def test_center_channels_produce_correct_frame(self):
        frame = self.protocol.build_rc_channels_frame([992] * 16)
        expected = bytes.fromhex("c8 18 16 e0 03 1f f8 c0 07 3e f0 81 0f 7c e0 03 1f f8 c0 07 3e f0 81 0f 7c ad")
        assert frame == expected

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