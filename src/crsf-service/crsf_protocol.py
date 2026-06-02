"""
CRSF Protocol Frame Builder
"""


class CRSFProtocol:
    def __init__(self):
        pass

    def build_rc_channels_frame(self, channels: list[int]) -> bytes:
        channels = [992] * 16
        for i, channel in enumerate(channels):
            print(f"Channel {i+1}: {channel}")
            
            

    def _pack_channels(self, channels: list[int]) -> bytes:
        # 16 channel values (11-bit each) -> 22 packed bytes
        pass

    def _crc8(self, data: bytes) -> int:
        # some bytes in -> one CRC byte (0–255) out
        pass


if __name__ == "__main__":
    crsf = CRSFProtocol()
    crsf.build_rc_channels_frame([1000, 1500, 2000] + [0] * 13)
