"""
CRSF Protocol Frame Builder
"""


"""
Frame structure:

- Start with 16 channels of 11 bits each (total 176 bits = 22 bytes)
- Range of 172-1811 for each channel (centered around 992)
- Shift each channel to its' own spot. Channel 0 stays at bit 0, channel 1 starts at bit 11, channel 2 at bit 22, etc.
- Merge into one number. One number is 16X11 = 176 bits, which is 22 bytes.
- Slice into 22 bytes, least significant byte first (little-endian)
"""


class CRSFProtocol:
    def __init__(self):
        pass

    def build_rc_channels_frame(self, channels: list[int]) -> bytes:
        channels = [992] * 16
        
        converted = 0
        for i, channel in enumerate(channels):
            converted |= channel << (i * 11)
        print("Converted channels:", converted.to_bytes(22, 'little').hex(" "))
            
            

    def _pack_channels(self, channels: list[int]) -> bytes:
        # 16 channel values (11-bit each) -> 22 packed bytes
        pass

    def _crc8(self, data: bytes) -> int:
        # some bytes in -> one CRC byte (0–255) out
        pass


if __name__ == "__main__":
    crsf = CRSFProtocol()
    crsf.build_rc_channels_frame([1000, 1500, 2000] + [0] * 13)
