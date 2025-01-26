# bits to bytes chart

| bits | bytes |
|---|---|
|8 bits | 1 byte |
|16 bits | 2 byte |
|32 bits | 4 byte |
|64 bits | 8 byte |
|128 bits | 16 byte |
|256 bits | 32 byte |

# Uint Calculation
- uint calculate right to left 
- and conversion is also done right to left in bits
- uint16 to uint8 conversion
- 1110111011100011 -> uint16 = 61155
- xxxxxxxx11100011 -> uint8 = 227

# Bytes Calculation
- Bytes strip from beginning of the byte stream
- bytes2 to bytes1 conversion
- 1110111011100011 -> bytes2 -> 0xeee3 -> 61155
- 11101110xxxxxxxx -> bytes1 -> 0xee -> 238

# BitWise Operators
## and &
```
x     = 1110 = 8 + 4 + 2 + 0 = 14
y     = 1011 = 8 + 0 + 2 + 1 = 11
x & y = 1010 = 8 + 0 + 2 + 0 = 10
```

## or | 
```
x     = 1100 = 8 + 4 + 0 + 0 = 12
y     = 1001 = 8 + 0 + 0 + 1 = 9
x | y = 1101 = 8 + 4 + 0 + 1 = 13
```

## xor ^
```
x     = 1100 = 8 + 4 + 0 + 0 = 12
y     = 0101 = 0 + 4 + 0 + 1 = 5
x ^ y = 1001 = 8 + 0 + 0 + 1 = 9
```

## ShiftLeft >>
- shift to the left of position of bits by the no. inserted
- for eg:- 12 (01100) >> 1 = 6 (00110)

## ShiftRight <<
- shift to the right of position of bits by the no. inserted
- for eg:- 12 (1100) << 1 = 24 (11000)

## Python uint and bytes to binary representation
```
#!/usr/bin/env python3
import sys

val=0x4e6368fbc9266e0258e199ad57c906425f73e6c274d558000000000000000000
print(bin(val)[2:])
```
- https://uint256.net/docs/converter/