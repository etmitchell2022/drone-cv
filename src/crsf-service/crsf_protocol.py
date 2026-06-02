"""
CRSF Protocol Frame Builder
"""


class CRSFProtocol:
    def __init__(self):
        pass

    def build_rc_channels_frame(self, channels: list[int]) -> bytes:
        ch0 = 992
        ch1 = 992
        
        combined = ch0 | (ch1 << 11)
        print(f"Combined: {combined} (0x{combined:06x})")
        print(combined.to_bytes(3, 'little').hex())

    def _pack_channels(self, channels: list[int]) -> bytes:
        # 16 channel values (11-bit each) -> 22 packed bytes
        pass
    
    def _crc8(self, data: bytes) -> int:
        # some bytes in -> one CRC byte (0–255) out
        pass
    
if __name__ == "__main__":
    crsf = CRSFProtocol()
    crsf.build_rc_channels_frame([1000, 1500, 2000] + [0]*13)