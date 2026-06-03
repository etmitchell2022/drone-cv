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
        
    def test_all_min_channels(self):
        frame = self.protocol.build_rc_channels_frame([172] * 16)
        expected = bytes.fromhex("c8 18 16 ac 60 05 2b 58 c1 0a 56 b0 82 15 ac 60 05 2b 58 c1 0a 56 b0 82 15 5b")
        assert frame == expected

    def test_all_max_channels(self):
        frame = self.protocol.build_rc_channels_frame([1811] * 16)
        expected = bytes.fromhex("c8 18 16 13 9f f8 c4 27 3e f1 89 4f 7c e2 13 9f f8 c4 27 3e f1 89 4f 7c e2 b9")
        assert frame == expected
        
    def test_varied_channels(self):
        channels = [172, 300, 450, 600, 750, 900, 992, 1100, 1250, 1400, 1550, 1700, 1811, 800, 1000, 500]
        frame = self.protocol.build_rc_channels_frame(channels)
        expected = bytes.fromhex("c8 18 16 ac 60 89 70 b0 e4 2e c2 81 8f 89 e2 c4 ab 83 49 3d 71 90 a1 8f 3e 3e")
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