from src.crsf_service.exceptions import InvalidChannelCountError, InvalidChannelValueError

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
        self._validate_channels(channels)

        payload = self._pack_channels(channels)
        crc = self._crc8(bytes([0x16]) + payload)
        frame = self._assemble_complete_frame(payload, crc)

        return frame

    def _validate_channels(self, channels: list[int]):
        if len(channels) != 16:
            raise InvalidChannelCountError("Exactly 16 channels are required")

        for ch in channels:
            if not (172 <= ch <= 1811):
                raise InvalidChannelValueError(f"Channel value {ch} is out of range (172-1811)")

    def _pack_channels(self, channels: list[int]) -> bytes:
        # 16 channel values (11-bit each) -> 22 packed bytes
        converted = 0
        for i, channel in enumerate(channels):
            converted |= channel << (i * 11)
        return converted.to_bytes(22, "little")

    def _crc8(self, data: bytes) -> int:
        # some bytes in -> one CRC byte (0–255) out
        # Error detection byte: Did this frame arrive intact?
        crc = 0  # running remainder; starts empty, ends as the checksum

        for byte in data:  # walk the data one byte at a time
            crc ^= byte  # fold this byte into the remainder (XOR = mix it in)

            for _ in range(8):  # then grind through that byte one bit at a time
                if crc & 0x80:  # top bit set? -> the divisor "goes in" here
                    crc = (crc << 1) ^ 0xD5  # shift left, then subtract divisor (XOR 0xD5)
                else:
                    crc <<= 1  # divisor didn't go in -> just shift left

                crc &= 0xFF  # keep crc to a single byte (drop anything past bit 7)

        return crc  # final remainder = the checksum (0–255)

    def _assemble_complete_frame(self, payload: bytes, crc: int) -> bytes:
        # Frame Structure: [0xC8, 0x18, 0x16, payload, crc]
        return bytes([0xC8, 0x18, 0x16]) + payload + bytes([crc])


if __name__ == "__main__":
    crsf = CRSFProtocol()
    crsf.build_rc_channels_frame([992] * 16)
