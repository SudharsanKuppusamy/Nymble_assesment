#include <stddef.h>
#include <stdint.h>

#ifndef CRC8_H_
#define CRC8_H_

#define CHECKSUM 8

typedef uint8_t crc;

#define WIDTH  (8 * sizeof(crc))
#define TOPBIT (1 << (WIDTH - 1))
#define POLYNOMIAL 0xD8
crc CRC8(uint8_t const message[], int nBytes);

#endif
