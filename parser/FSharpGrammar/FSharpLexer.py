# Generated from FSharpGrammar/FSharpLexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 0, 108, 773, 6, -1, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5,
        2, 6, 7, 6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2,
        13, 7, 13, 2, 14, 7, 14, 2, 15, 7, 15, 2, 16, 7, 16, 2, 17, 7, 17, 2, 18, 7, 18, 2, 19, 7,
        19, 2, 20, 7, 20, 2, 21, 7, 21, 2, 22, 7, 22, 2, 23, 7, 23, 2, 24, 7, 24, 2, 25, 7, 25, 2,
        26, 7, 26, 2, 27, 7, 27, 2, 28, 7, 28, 2, 29, 7, 29, 2, 30, 7, 30, 2, 31, 7, 31, 2, 32, 7,
        32, 2, 33, 7, 33, 2, 34, 7, 34, 2, 35, 7, 35, 2, 36, 7, 36, 2, 37, 7, 37, 2, 38, 7, 38, 2,
        39, 7, 39, 2, 40, 7, 40, 2, 41, 7, 41, 2, 42, 7, 42, 2, 43, 7, 43, 2, 44, 7, 44, 2, 45, 7,
        45, 2, 46, 7, 46, 2, 47, 7, 47, 2, 48, 7, 48, 2, 49, 7, 49, 2, 50, 7, 50, 2, 51, 7, 51, 2,
        52, 7, 52, 2, 53, 7, 53, 2, 54, 7, 54, 2, 55, 7, 55, 2, 56, 7, 56, 2, 57, 7, 57, 2, 58, 7,
        58, 2, 59, 7, 59, 2, 60, 7, 60, 2, 61, 7, 61, 2, 62, 7, 62, 2, 63, 7, 63, 2, 64, 7, 64, 2,
        65, 7, 65, 2, 66, 7, 66, 2, 67, 7, 67, 2, 68, 7, 68, 2, 69, 7, 69, 2, 70, 7, 70, 2, 71, 7,
        71, 2, 72, 7, 72, 2, 73, 7, 73, 2, 74, 7, 74, 2, 75, 7, 75, 2, 76, 7, 76, 2, 77, 7, 77, 2,
        78, 7, 78, 2, 79, 7, 79, 2, 80, 7, 80, 2, 81, 7, 81, 2, 82, 7, 82, 2, 83, 7, 83, 2, 84, 7,
        84, 2, 85, 7, 85, 2, 86, 7, 86, 2, 87, 7, 87, 2, 88, 7, 88, 2, 89, 7, 89, 2, 90, 7, 90, 2,
        91, 7, 91, 2, 92, 7, 92, 2, 93, 7, 93, 2, 94, 7, 94, 2, 95, 7, 95, 2, 96, 7, 96, 2, 97, 7,
        97, 2, 98, 7, 98, 2, 99, 7, 99, 2, 100, 7, 100, 2, 101, 7, 101, 2, 102, 7, 102, 2, 103,
        7, 103, 2, 104, 7, 104, 2, 105, 7, 105, 2, 106, 7, 106, 2, 107, 7, 107, 1, 0, 4, 0, 219,
        8, 0, 11, 0, 12, 0, 220, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 229, 8, 1, 10, 1, 12, 1,
        232, 9, 1, 1, 1, 3, 1, 235, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 241, 8, 1, 10, 1, 12, 1, 244,
        9, 1, 1, 1, 1, 1, 3, 1, 248, 8, 1, 1, 1, 1, 1, 1, 2, 4, 2, 253, 8, 2, 11, 2, 12, 2, 254, 1,
        2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 263, 8, 2, 1, 3, 4, 3, 266, 8, 3, 11, 3, 12, 3, 267,
        1, 3, 1, 3, 4, 3, 272, 8, 3, 11, 3, 12, 3, 273, 1, 3, 3, 3, 277, 8, 3, 1, 4, 1, 4, 1, 4, 1,
        4, 1, 4, 1, 4, 1, 4, 1, 4, 3, 4, 287, 8, 4, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1,
        5, 1, 5, 1, 5, 3, 5, 300, 8, 5, 1, 5, 1, 5, 1, 6, 1, 6, 1, 6, 1, 6, 5, 6, 308, 8, 6, 10, 6, 12,
        6, 311, 9, 6, 1, 6, 1, 6, 1, 7, 1, 7, 1, 7, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1,
        8, 3, 8, 327, 8, 8, 1, 9, 1, 9, 5, 9, 331, 8, 9, 10, 9, 12, 9, 334, 9, 9, 1, 9, 1, 9, 1, 10,
        1, 10, 1, 10, 1, 10, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 12, 1, 12, 1, 12,
        1, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13,
        1, 13, 1, 14, 1, 14, 1, 14, 1, 14, 1, 14, 1, 14, 1, 14, 1, 14, 1, 15, 1, 15, 1, 15, 1, 15,
        1, 16, 1, 16, 1, 16, 1, 16, 1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1, 17, 1, 18, 1, 18, 1, 18,
        1, 19, 1, 19, 1, 19, 1, 19, 1, 20, 1, 20, 1, 20, 1, 21, 1, 21, 1, 21, 1, 21, 1, 21, 1, 21,
        1, 21, 1, 22, 1, 22, 1, 22, 1, 23, 1, 23, 1, 24, 1, 24, 1, 24, 1, 24, 1, 24, 1, 25, 1, 25,
        1, 25, 1, 25, 1, 25, 1, 25, 1, 25, 1, 26, 1, 26, 1, 26, 1, 26, 1, 26, 1, 27, 1, 27, 1, 27,
        1, 27, 1, 27, 1, 27, 1, 27, 1, 27, 1, 27, 1, 27, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28, 1, 28,
        1, 29, 1, 29, 1, 29, 1, 29, 1, 30, 1, 30, 1, 30, 1, 30, 1, 30, 1, 30, 1, 30, 1, 31, 1, 31,
        1, 31, 1, 31, 1, 32, 1, 32, 1, 32, 1, 32, 1, 32, 1, 32, 1, 32, 1, 32, 1, 32, 1, 32, 1, 33,
        1, 33, 1, 33, 1, 33, 1, 34, 1, 34, 1, 34, 1, 34, 1, 34, 1, 34, 1, 34, 1, 34, 1, 35, 1, 35,
        1, 35, 1, 35, 1, 35, 1, 35, 1, 35, 1, 35, 1, 35, 1, 36, 1, 36, 1, 36, 1, 36, 1, 36, 1, 36,
        1, 36, 1, 36, 1, 37, 1, 37, 1, 37, 1, 37, 1, 37, 1, 37, 1, 37, 1, 37, 1, 37, 1, 38, 1, 38,
        1, 38, 1, 38, 1, 38, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39, 1, 39, 1, 40, 1, 40, 1, 40, 1, 40,
        1, 40, 1, 41, 1, 41, 1, 41, 1, 41, 1, 42, 1, 42, 1, 42, 1, 42, 1, 42, 1, 43, 1, 43, 1, 43,
        1, 43, 1, 43, 1, 44, 1, 44, 1, 44, 1, 44, 1, 44, 1, 44, 1, 44, 1, 45, 1, 45, 1, 45, 1, 45,
        1, 46, 1, 46, 1, 46, 1, 46, 1, 47, 1, 47, 1, 47, 1, 47, 1, 48, 1, 48, 1, 48, 1, 48, 1, 48,
        1, 48, 1, 49, 1, 49, 1, 49, 1, 49, 1, 49, 1, 49, 1, 49, 1, 49, 1, 50, 1, 50, 1, 50, 1, 50,
        1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 51, 1, 51, 1, 51, 1, 51, 1, 51, 1, 51, 1, 51, 1, 51,
        1, 51, 1, 51, 1, 51, 1, 52, 1, 52, 1, 52, 1, 52, 1, 53, 1, 53, 1, 53, 1, 53, 1, 54, 1, 54,
        1, 54, 1, 54, 1, 54, 1, 54, 1, 54, 1, 54, 1, 55, 1, 55, 1, 55, 1, 55, 1, 55, 1, 55, 1, 56,
        1, 56, 1, 56, 1, 56, 1, 56, 1, 57, 1, 57, 1, 57, 1, 57, 1, 58, 1, 58, 1, 58, 1, 58, 1, 58,
        1, 58, 1, 59, 1, 59, 1, 59, 1, 59, 1, 59, 1, 60, 1, 60, 1, 60, 1, 60, 1, 60, 1, 60, 1, 60,
        1, 60, 1, 60, 1, 60, 1, 61, 1, 61, 1, 61, 1, 62, 1, 62, 1, 63, 1, 63, 1, 63, 1, 64, 1, 64,
        1, 65, 1, 65, 1, 66, 1, 66, 1, 67, 1, 67, 1, 68, 1, 68, 1, 68, 1, 69, 1, 69, 1, 69, 1, 70,
        1, 70, 1, 71, 1, 71, 1, 71, 1, 72, 1, 72, 1, 72, 1, 73, 1, 73, 1, 74, 1, 74, 1, 75, 1, 75,
        1, 76, 1, 76, 1, 77, 1, 77, 1, 77, 1, 78, 1, 78, 1, 79, 1, 79, 1, 80, 1, 80, 1, 80, 1, 81,
        1, 81, 1, 82, 1, 82, 1, 83, 1, 83, 1, 83, 1, 84, 1, 84, 1, 84, 1, 85, 1, 85, 1, 85, 1, 86,
        1, 86, 1, 86, 1, 87, 1, 87, 1, 87, 1, 87, 1, 88, 1, 88, 1, 88, 1, 88, 1, 89, 1, 89, 1, 89,
        1, 89, 1, 90, 1, 90, 1, 90, 1, 90, 1, 91, 1, 91, 1, 91, 1, 91, 1, 92, 1, 92, 1, 92, 1, 92,
        1, 93, 1, 93, 1, 93, 1, 93, 1, 94, 1, 94, 1, 94, 1, 95, 1, 95, 1, 96, 1, 96, 1, 97, 1, 97,
        1, 98, 1, 98, 1, 99, 1, 99, 1, 100, 1, 100, 1, 101, 1, 101, 1, 102, 1, 102, 1, 102, 1,
        103, 1, 103, 1, 103, 1, 103, 1, 103, 1, 104, 1, 104, 1, 104, 1, 104, 1, 104, 1, 105,
        1, 105, 1, 106, 1, 106, 5, 106, 767, 8, 106, 10, 106, 12, 106, 770, 9, 106, 1, 107,
        1, 107, 2, 230, 242, 0, 108, 1, 1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6, 13, 7, 15, 8, 17, 9, 19,
        10, 21, 11, 23, 12, 25, 13, 27, 14, 29, 15, 31, 16, 33, 17, 35, 18, 37, 19, 39, 20, 41,
        21, 43, 22, 45, 23, 47, 24, 49, 25, 51, 26, 53, 27, 55, 28, 57, 29, 59, 30, 61, 31, 63,
        32, 65, 33, 67, 34, 69, 35, 71, 36, 73, 37, 75, 38, 77, 39, 79, 40, 81, 41, 83, 42, 85,
        43, 87, 44, 89, 45, 91, 46, 93, 47, 95, 48, 97, 49, 99, 50, 101, 51, 103, 52, 105, 53,
        107, 54, 109, 55, 111, 56, 113, 57, 115, 58, 117, 59, 119, 60, 121, 61, 123, 62, 125,
        63, 127, 64, 129, 65, 131, 66, 133, 67, 135, 68, 137, 69, 139, 70, 141, 71, 143, 72,
        145, 73, 147, 74, 149, 75, 151, 76, 153, 77, 155, 78, 157, 79, 159, 80, 161, 81, 163,
        82, 165, 83, 167, 84, 169, 85, 171, 86, 173, 87, 175, 88, 177, 89, 179, 90, 181, 91,
        183, 92, 185, 93, 187, 94, 189, 95, 191, 96, 193, 97, 195, 98, 197, 99, 199, 100,
        201, 101, 203, 102, 205, 103, 207, 104, 209, 105, 211, 106, 213, 107, 215, 108,
        1, 0, 13, 3, 0, 9, 10, 13, 13, 32, 32, 1, 1, 10, 10, 1, 0, 48, 57, 2, 0, 115, 115, 121,
        121, 2, 0, 76, 76, 117, 117, 2, 0, 102, 102, 109, 109, 2, 0, 39, 39, 92, 92, 5, 0, 34,
        34, 39, 39, 92, 92, 110, 110, 116, 116, 3, 0, 48, 57, 65, 70, 97, 102, 2, 0, 34, 34,
        92, 92, 5, 0, 34, 34, 39, 39, 92, 92, 110, 110, 116, 117, 4, 0, 48, 57, 65, 90, 95, 95,
        97, 122, 1, 0, 46, 46, 794, 0, 1, 1, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 5, 1, 0, 0, 0, 0, 7, 1, 0,
        0, 0, 0, 9, 1, 0, 0, 0, 0, 11, 1, 0, 0, 0, 0, 13, 1, 0, 0, 0, 0, 15, 1, 0, 0, 0, 0, 17, 1, 0,
        0, 0, 0, 19, 1, 0, 0, 0, 0, 21, 1, 0, 0, 0, 0, 23, 1, 0, 0, 0, 0, 25, 1, 0, 0, 0, 0, 27, 1, 0,
        0, 0, 0, 29, 1, 0, 0, 0, 0, 31, 1, 0, 0, 0, 0, 33, 1, 0, 0, 0, 0, 35, 1, 0, 0, 0, 0, 37, 1, 0,
        0, 0, 0, 39, 1, 0, 0, 0, 0, 41, 1, 0, 0, 0, 0, 43, 1, 0, 0, 0, 0, 45, 1, 0, 0, 0, 0, 47, 1, 0,
        0, 0, 0, 49, 1, 0, 0, 0, 0, 51, 1, 0, 0, 0, 0, 53, 1, 0, 0, 0, 0, 55, 1, 0, 0, 0, 0, 57, 1, 0,
        0, 0, 0, 59, 1, 0, 0, 0, 0, 61, 1, 0, 0, 0, 0, 63, 1, 0, 0, 0, 0, 65, 1, 0, 0, 0, 0, 67, 1, 0,
        0, 0, 0, 69, 1, 0, 0, 0, 0, 71, 1, 0, 0, 0, 0, 73, 1, 0, 0, 0, 0, 75, 1, 0, 0, 0, 0, 77, 1, 0,
        0, 0, 0, 79, 1, 0, 0, 0, 0, 81, 1, 0, 0, 0, 0, 83, 1, 0, 0, 0, 0, 85, 1, 0, 0, 0, 0, 87, 1, 0,
        0, 0, 0, 89, 1, 0, 0, 0, 0, 91, 1, 0, 0, 0, 0, 93, 1, 0, 0, 0, 0, 95, 1, 0, 0, 0, 0, 97, 1, 0,
        0, 0, 0, 99, 1, 0, 0, 0, 0, 101, 1, 0, 0, 0, 0, 103, 1, 0, 0, 0, 0, 105, 1, 0, 0, 0, 0, 107,
        1, 0, 0, 0, 0, 109, 1, 0, 0, 0, 0, 111, 1, 0, 0, 0, 0, 113, 1, 0, 0, 0, 0, 115, 1, 0, 0, 0,
        0, 117, 1, 0, 0, 0, 0, 119, 1, 0, 0, 0, 0, 121, 1, 0, 0, 0, 0, 123, 1, 0, 0, 0, 0, 125, 1,
        0, 0, 0, 0, 127, 1, 0, 0, 0, 0, 129, 1, 0, 0, 0, 0, 131, 1, 0, 0, 0, 0, 133, 1, 0, 0, 0, 0,
        135, 1, 0, 0, 0, 0, 137, 1, 0, 0, 0, 0, 139, 1, 0, 0, 0, 0, 141, 1, 0, 0, 0, 0, 143, 1, 0,
        0, 0, 0, 145, 1, 0, 0, 0, 0, 147, 1, 0, 0, 0, 0, 149, 1, 0, 0, 0, 0, 151, 1, 0, 0, 0, 0, 153,
        1, 0, 0, 0, 0, 155, 1, 0, 0, 0, 0, 157, 1, 0, 0, 0, 0, 159, 1, 0, 0, 0, 0, 161, 1, 0, 0, 0,
        0, 163, 1, 0, 0, 0, 0, 165, 1, 0, 0, 0, 0, 167, 1, 0, 0, 0, 0, 169, 1, 0, 0, 0, 0, 171, 1,
        0, 0, 0, 0, 173, 1, 0, 0, 0, 0, 175, 1, 0, 0, 0, 0, 177, 1, 0, 0, 0, 0, 179, 1, 0, 0, 0, 0,
        181, 1, 0, 0, 0, 0, 183, 1, 0, 0, 0, 0, 185, 1, 0, 0, 0, 0, 187, 1, 0, 0, 0, 0, 189, 1, 0,
        0, 0, 0, 191, 1, 0, 0, 0, 0, 193, 1, 0, 0, 0, 0, 195, 1, 0, 0, 0, 0, 197, 1, 0, 0, 0, 0, 199,
        1, 0, 0, 0, 0, 201, 1, 0, 0, 0, 0, 203, 1, 0, 0, 0, 0, 205, 1, 0, 0, 0, 0, 207, 1, 0, 0, 0,
        0, 209, 1, 0, 0, 0, 0, 211, 1, 0, 0, 0, 0, 213, 1, 0, 0, 0, 0, 215, 1, 0, 0, 0, 1, 218, 1,
        0, 0, 0, 3, 247, 1, 0, 0, 0, 5, 252, 1, 0, 0, 0, 7, 265, 1, 0, 0, 0, 9, 286, 1, 0, 0, 0, 11,
        288, 1, 0, 0, 0, 13, 303, 1, 0, 0, 0, 15, 314, 1, 0, 0, 0, 17, 326, 1, 0, 0, 0, 19, 328,
        1, 0, 0, 0, 21, 337, 1, 0, 0, 0, 23, 341, 1, 0, 0, 0, 25, 348, 1, 0, 0, 0, 27, 356, 1, 0,
        0, 0, 29, 365, 1, 0, 0, 0, 31, 373, 1, 0, 0, 0, 33, 377, 1, 0, 0, 0, 35, 381, 1, 0, 0, 0,
        37, 387, 1, 0, 0, 0, 39, 390, 1, 0, 0, 0, 41, 394, 1, 0, 0, 0, 43, 397, 1, 0, 0, 0, 45, 404,
        1, 0, 0, 0, 47, 407, 1, 0, 0, 0, 49, 409, 1, 0, 0, 0, 51, 414, 1, 0, 0, 0, 53, 421, 1, 0,
        0, 0, 55, 426, 1, 0, 0, 0, 57, 436, 1, 0, 0, 0, 59, 442, 1, 0, 0, 0, 61, 446, 1, 0, 0, 0,
        63, 453, 1, 0, 0, 0, 65, 457, 1, 0, 0, 0, 67, 467, 1, 0, 0, 0, 69, 471, 1, 0, 0, 0, 71, 479,
        1, 0, 0, 0, 73, 488, 1, 0, 0, 0, 75, 496, 1, 0, 0, 0, 77, 505, 1, 0, 0, 0, 79, 510, 1, 0,
        0, 0, 81, 516, 1, 0, 0, 0, 83, 521, 1, 0, 0, 0, 85, 525, 1, 0, 0, 0, 87, 530, 1, 0, 0, 0,
        89, 535, 1, 0, 0, 0, 91, 542, 1, 0, 0, 0, 93, 546, 1, 0, 0, 0, 95, 550, 1, 0, 0, 0, 97, 554,
        1, 0, 0, 0, 99, 560, 1, 0, 0, 0, 101, 568, 1, 0, 0, 0, 103, 577, 1, 0, 0, 0, 105, 588, 1,
        0, 0, 0, 107, 592, 1, 0, 0, 0, 109, 596, 1, 0, 0, 0, 111, 604, 1, 0, 0, 0, 113, 610, 1,
        0, 0, 0, 115, 615, 1, 0, 0, 0, 117, 619, 1, 0, 0, 0, 119, 625, 1, 0, 0, 0, 121, 630, 1,
        0, 0, 0, 123, 640, 1, 0, 0, 0, 125, 643, 1, 0, 0, 0, 127, 645, 1, 0, 0, 0, 129, 648, 1,
        0, 0, 0, 131, 650, 1, 0, 0, 0, 133, 652, 1, 0, 0, 0, 135, 654, 1, 0, 0, 0, 137, 656, 1,
        0, 0, 0, 139, 659, 1, 0, 0, 0, 141, 662, 1, 0, 0, 0, 143, 664, 1, 0, 0, 0, 145, 667, 1,
        0, 0, 0, 147, 670, 1, 0, 0, 0, 149, 672, 1, 0, 0, 0, 151, 674, 1, 0, 0, 0, 153, 676, 1,
        0, 0, 0, 155, 678, 1, 0, 0, 0, 157, 681, 1, 0, 0, 0, 159, 683, 1, 0, 0, 0, 161, 685, 1,
        0, 0, 0, 163, 688, 1, 0, 0, 0, 165, 690, 1, 0, 0, 0, 167, 692, 1, 0, 0, 0, 169, 695, 1,
        0, 0, 0, 171, 698, 1, 0, 0, 0, 173, 701, 1, 0, 0, 0, 175, 704, 1, 0, 0, 0, 177, 708, 1,
        0, 0, 0, 179, 712, 1, 0, 0, 0, 181, 716, 1, 0, 0, 0, 183, 720, 1, 0, 0, 0, 185, 724, 1,
        0, 0, 0, 187, 728, 1, 0, 0, 0, 189, 732, 1, 0, 0, 0, 191, 735, 1, 0, 0, 0, 193, 737, 1,
        0, 0, 0, 195, 739, 1, 0, 0, 0, 197, 741, 1, 0, 0, 0, 199, 743, 1, 0, 0, 0, 201, 745, 1,
        0, 0, 0, 203, 747, 1, 0, 0, 0, 205, 749, 1, 0, 0, 0, 207, 752, 1, 0, 0, 0, 209, 757, 1,
        0, 0, 0, 211, 762, 1, 0, 0, 0, 213, 764, 1, 0, 0, 0, 215, 771, 1, 0, 0, 0, 217, 219, 7,
        0, 0, 0, 218, 217, 1, 0, 0, 0, 219, 220, 1, 0, 0, 0, 220, 218, 1, 0, 0, 0, 220, 221, 1,
        0, 0, 0, 221, 222, 1, 0, 0, 0, 222, 223, 6, 0, 0, 0, 223, 2, 1, 0, 0, 0, 224, 225, 5, 47,
        0, 0, 225, 226, 5, 47, 0, 0, 226, 230, 1, 0, 0, 0, 227, 229, 9, 0, 0, 0, 228, 227, 1, 0,
        0, 0, 229, 232, 1, 0, 0, 0, 230, 231, 1, 0, 0, 0, 230, 228, 1, 0, 0, 0, 231, 234, 1, 0,
        0, 0, 232, 230, 1, 0, 0, 0, 233, 235, 7, 1, 0, 0, 234, 233, 1, 0, 0, 0, 235, 248, 1, 0,
        0, 0, 236, 237, 5, 40, 0, 0, 237, 238, 5, 42, 0, 0, 238, 242, 1, 0, 0, 0, 239, 241, 9,
        0, 0, 0, 240, 239, 1, 0, 0, 0, 241, 244, 1, 0, 0, 0, 242, 243, 1, 0, 0, 0, 242, 240, 1,
        0, 0, 0, 243, 245, 1, 0, 0, 0, 244, 242, 1, 0, 0, 0, 245, 246, 5, 42, 0, 0, 246, 248, 5,
        41, 0, 0, 247, 224, 1, 0, 0, 0, 247, 236, 1, 0, 0, 0, 248, 249, 1, 0, 0, 0, 249, 250, 6,
        1, 0, 0, 250, 4, 1, 0, 0, 0, 251, 253, 7, 2, 0, 0, 252, 251, 1, 0, 0, 0, 253, 254, 1, 0,
        0, 0, 254, 252, 1, 0, 0, 0, 254, 255, 1, 0, 0, 0, 255, 262, 1, 0, 0, 0, 256, 257, 5, 117,
        0, 0, 257, 263, 5, 121, 0, 0, 258, 263, 7, 3, 0, 0, 259, 260, 5, 117, 0, 0, 260, 263,
        5, 115, 0, 0, 261, 263, 7, 4, 0, 0, 262, 256, 1, 0, 0, 0, 262, 258, 1, 0, 0, 0, 262, 259,
        1, 0, 0, 0, 262, 261, 1, 0, 0, 0, 262, 263, 1, 0, 0, 0, 263, 6, 1, 0, 0, 0, 264, 266, 7,
        2, 0, 0, 265, 264, 1, 0, 0, 0, 266, 267, 1, 0, 0, 0, 267, 265, 1, 0, 0, 0, 267, 268, 1,
        0, 0, 0, 268, 269, 1, 0, 0, 0, 269, 271, 5, 46, 0, 0, 270, 272, 7, 2, 0, 0, 271, 270, 1,
        0, 0, 0, 272, 273, 1, 0, 0, 0, 273, 271, 1, 0, 0, 0, 273, 274, 1, 0, 0, 0, 274, 276, 1,
        0, 0, 0, 275, 277, 7, 5, 0, 0, 276, 275, 1, 0, 0, 0, 276, 277, 1, 0, 0, 0, 277, 8, 1, 0,
        0, 0, 278, 279, 5, 37, 0, 0, 279, 287, 5, 115, 0, 0, 280, 281, 5, 37, 0, 0, 281, 287,
        5, 100, 0, 0, 282, 283, 5, 37, 0, 0, 283, 287, 5, 102, 0, 0, 284, 285, 5, 37, 0, 0, 285,
        287, 5, 99, 0, 0, 286, 278, 1, 0, 0, 0, 286, 280, 1, 0, 0, 0, 286, 282, 1, 0, 0, 0, 286,
        284, 1, 0, 0, 0, 287, 10, 1, 0, 0, 0, 288, 299, 5, 39, 0, 0, 289, 300, 8, 6, 0, 0, 290,
        291, 5, 92, 0, 0, 291, 300, 7, 7, 0, 0, 292, 293, 5, 92, 0, 0, 293, 294, 5, 117, 0, 0,
        294, 295, 1, 0, 0, 0, 295, 296, 7, 8, 0, 0, 296, 297, 7, 8, 0, 0, 297, 298, 7, 8, 0, 0,
        298, 300, 7, 8, 0, 0, 299, 289, 1, 0, 0, 0, 299, 290, 1, 0, 0, 0, 299, 292, 1, 0, 0, 0,
        300, 301, 1, 0, 0, 0, 301, 302, 5, 39, 0, 0, 302, 12, 1, 0, 0, 0, 303, 309, 3, 203, 101,
        0, 304, 308, 8, 9, 0, 0, 305, 306, 5, 92, 0, 0, 306, 308, 7, 10, 0, 0, 307, 304, 1, 0,
        0, 0, 307, 305, 1, 0, 0, 0, 308, 311, 1, 0, 0, 0, 309, 307, 1, 0, 0, 0, 309, 310, 1, 0,
        0, 0, 310, 312, 1, 0, 0, 0, 311, 309, 1, 0, 0, 0, 312, 313, 3, 203, 101, 0, 313, 14, 1,
        0, 0, 0, 314, 315, 3, 47, 23, 0, 315, 316, 3, 13, 6, 0, 316, 16, 1, 0, 0, 0, 317, 318,
        5, 116, 0, 0, 318, 319, 5, 114, 0, 0, 319, 320, 5, 117, 0, 0, 320, 327, 5, 101, 0, 0,
        321, 322, 5, 102, 0, 0, 322, 323, 5, 97, 0, 0, 323, 324, 5, 108, 0, 0, 324, 325, 5, 115,
        0, 0, 325, 327, 5, 101, 0, 0, 326, 317, 1, 0, 0, 0, 326, 321, 1, 0, 0, 0, 327, 18, 1, 0,
        0, 0, 328, 332, 5, 40, 0, 0, 329, 331, 5, 32, 0, 0, 330, 329, 1, 0, 0, 0, 331, 334, 1,
        0, 0, 0, 332, 330, 1, 0, 0, 0, 332, 333, 1, 0, 0, 0, 333, 335, 1, 0, 0, 0, 334, 332, 1,
        0, 0, 0, 335, 336, 5, 41, 0, 0, 336, 20, 1, 0, 0, 0, 337, 338, 5, 114, 0, 0, 338, 339,
        5, 101, 0, 0, 339, 340, 5, 99, 0, 0, 340, 22, 1, 0, 0, 0, 341, 342, 5, 112, 0, 0, 342,
        343, 5, 117, 0, 0, 343, 344, 5, 98, 0, 0, 344, 345, 5, 108, 0, 0, 345, 346, 5, 105, 0,
        0, 346, 347, 5, 99, 0, 0, 347, 24, 1, 0, 0, 0, 348, 349, 5, 112, 0, 0, 349, 350, 5, 114,
        0, 0, 350, 351, 5, 105, 0, 0, 351, 352, 5, 118, 0, 0, 352, 353, 5, 97, 0, 0, 353, 354,
        5, 116, 0, 0, 354, 355, 5, 101, 0, 0, 355, 26, 1, 0, 0, 0, 356, 357, 5, 105, 0, 0, 357,
        358, 5, 110, 0, 0, 358, 359, 5, 116, 0, 0, 359, 360, 5, 101, 0, 0, 360, 361, 5, 114,
        0, 0, 361, 362, 5, 110, 0, 0, 362, 363, 5, 97, 0, 0, 363, 364, 5, 108, 0, 0, 364, 28,
        1, 0, 0, 0, 365, 366, 5, 109, 0, 0, 366, 367, 5, 117, 0, 0, 367, 368, 5, 116, 0, 0, 368,
        369, 5, 97, 0, 0, 369, 370, 5, 98, 0, 0, 370, 371, 5, 108, 0, 0, 371, 372, 5, 101, 0,
        0, 372, 30, 1, 0, 0, 0, 373, 374, 5, 108, 0, 0, 374, 375, 5, 101, 0, 0, 375, 376, 5, 116,
        0, 0, 376, 32, 1, 0, 0, 0, 377, 378, 5, 102, 0, 0, 378, 379, 5, 117, 0, 0, 379, 380, 5,
        110, 0, 0, 380, 34, 1, 0, 0, 0, 381, 382, 5, 119, 0, 0, 382, 383, 5, 104, 0, 0, 383, 384,
        5, 105, 0, 0, 384, 385, 5, 108, 0, 0, 385, 386, 5, 101, 0, 0, 386, 36, 1, 0, 0, 0, 387,
        388, 5, 100, 0, 0, 388, 389, 5, 111, 0, 0, 389, 38, 1, 0, 0, 0, 390, 391, 5, 102, 0, 0,
        391, 392, 5, 111, 0, 0, 392, 393, 5, 114, 0, 0, 393, 40, 1, 0, 0, 0, 394, 395, 5, 116,
        0, 0, 395, 396, 5, 111, 0, 0, 396, 42, 1, 0, 0, 0, 397, 398, 5, 100, 0, 0, 398, 399, 5,
        111, 0, 0, 399, 400, 5, 119, 0, 0, 400, 401, 5, 110, 0, 0, 401, 402, 5, 116, 0, 0, 402,
        403, 5, 111, 0, 0, 403, 44, 1, 0, 0, 0, 404, 405, 5, 105, 0, 0, 405, 406, 5, 110, 0, 0,
        406, 46, 1, 0, 0, 0, 407, 408, 5, 36, 0, 0, 408, 48, 1, 0, 0, 0, 409, 410, 5, 116, 0, 0,
        410, 411, 5, 121, 0, 0, 411, 412, 5, 112, 0, 0, 412, 413, 5, 101, 0, 0, 413, 50, 1, 0,
        0, 0, 414, 415, 5, 109, 0, 0, 415, 416, 5, 111, 0, 0, 416, 417, 5, 100, 0, 0, 417, 418,
        5, 117, 0, 0, 418, 419, 5, 108, 0, 0, 419, 420, 5, 101, 0, 0, 420, 52, 1, 0, 0, 0, 421,
        422, 5, 111, 0, 0, 422, 423, 5, 112, 0, 0, 423, 424, 5, 101, 0, 0, 424, 425, 5, 110,
        0, 0, 425, 54, 1, 0, 0, 0, 426, 427, 5, 110, 0, 0, 427, 428, 5, 97, 0, 0, 428, 429, 5,
        109, 0, 0, 429, 430, 5, 101, 0, 0, 430, 431, 5, 115, 0, 0, 431, 432, 5, 112, 0, 0, 432,
        433, 5, 97, 0, 0, 433, 434, 5, 99, 0, 0, 434, 435, 5, 101, 0, 0, 435, 56, 1, 0, 0, 0, 436,
        437, 5, 99, 0, 0, 437, 438, 5, 108, 0, 0, 438, 439, 5, 97, 0, 0, 439, 440, 5, 115, 0,
        0, 440, 441, 5, 115, 0, 0, 441, 58, 1, 0, 0, 0, 442, 443, 5, 101, 0, 0, 443, 444, 5, 110,
        0, 0, 444, 445, 5, 100, 0, 0, 445, 60, 1, 0, 0, 0, 446, 447, 5, 115, 0, 0, 447, 448, 5,
        116, 0, 0, 448, 449, 5, 114, 0, 0, 449, 450, 5, 117, 0, 0, 450, 451, 5, 99, 0, 0, 451,
        452, 5, 116, 0, 0, 452, 62, 1, 0, 0, 0, 453, 454, 5, 97, 0, 0, 454, 455, 5, 110, 0, 0,
        455, 456, 5, 100, 0, 0, 456, 64, 1, 0, 0, 0, 457, 458, 5, 105, 0, 0, 458, 459, 5, 110,
        0, 0, 459, 460, 5, 116, 0, 0, 460, 461, 5, 101, 0, 0, 461, 462, 5, 114, 0, 0, 462, 463,
        5, 102, 0, 0, 463, 464, 5, 97, 0, 0, 464, 465, 5, 99, 0, 0, 465, 466, 5, 101, 0, 0, 466,
        66, 1, 0, 0, 0, 467, 468, 5, 103, 0, 0, 468, 469, 5, 101, 0, 0, 469, 470, 5, 116, 0, 0,
        470, 68, 1, 0, 0, 0, 471, 472, 5, 105, 0, 0, 472, 473, 5, 110, 0, 0, 473, 474, 5, 104,
        0, 0, 474, 475, 5, 101, 0, 0, 475, 476, 5, 114, 0, 0, 476, 477, 5, 105, 0, 0, 477, 478,
        5, 116, 0, 0, 478, 70, 1, 0, 0, 0, 479, 480, 5, 111, 0, 0, 480, 481, 5, 118, 0, 0, 481,
        482, 5, 101, 0, 0, 482, 483, 5, 114, 0, 0, 483, 484, 5, 114, 0, 0, 484, 485, 5, 105,
        0, 0, 485, 486, 5, 100, 0, 0, 486, 487, 5, 101, 0, 0, 487, 72, 1, 0, 0, 0, 488, 489, 5,
        100, 0, 0, 489, 490, 5, 101, 0, 0, 490, 491, 5, 102, 0, 0, 491, 492, 5, 97, 0, 0, 492,
        493, 5, 117, 0, 0, 493, 494, 5, 108, 0, 0, 494, 495, 5, 116, 0, 0, 495, 74, 1, 0, 0, 0,
        496, 497, 5, 97, 0, 0, 497, 498, 5, 98, 0, 0, 498, 499, 5, 115, 0, 0, 499, 500, 5, 116,
        0, 0, 500, 501, 5, 114, 0, 0, 501, 502, 5, 97, 0, 0, 502, 503, 5, 99, 0, 0, 503, 504,
        5, 116, 0, 0, 504, 76, 1, 0, 0, 0, 505, 506, 5, 98, 0, 0, 506, 507, 5, 97, 0, 0, 507, 508,
        5, 115, 0, 0, 508, 509, 5, 101, 0, 0, 509, 78, 1, 0, 0, 0, 510, 511, 5, 97, 0, 0, 511,
        512, 5, 115, 0, 0, 512, 513, 5, 121, 0, 0, 513, 514, 5, 110, 0, 0, 514, 515, 5, 99, 0,
        0, 515, 80, 1, 0, 0, 0, 516, 517, 5, 116, 0, 0, 517, 518, 5, 97, 0, 0, 518, 519, 5, 115,
        0, 0, 519, 520, 5, 107, 0, 0, 520, 82, 1, 0, 0, 0, 521, 522, 5, 110, 0, 0, 522, 523, 5,
        101, 0, 0, 523, 524, 5, 119, 0, 0, 524, 84, 1, 0, 0, 0, 525, 526, 5, 116, 0, 0, 526, 527,
        5, 104, 0, 0, 527, 528, 5, 101, 0, 0, 528, 529, 5, 110, 0, 0, 529, 86, 1, 0, 0, 0, 530,
        531, 5, 116, 0, 0, 531, 532, 5, 104, 0, 0, 532, 533, 5, 105, 0, 0, 533, 534, 5, 115,
        0, 0, 534, 88, 1, 0, 0, 0, 535, 536, 5, 109, 0, 0, 536, 537, 5, 101, 0, 0, 537, 538, 5,
        109, 0, 0, 538, 539, 5, 98, 0, 0, 539, 540, 5, 101, 0, 0, 540, 541, 5, 114, 0, 0, 541,
        90, 1, 0, 0, 0, 542, 543, 5, 115, 0, 0, 543, 544, 5, 101, 0, 0, 544, 545, 5, 113, 0, 0,
        545, 92, 1, 0, 0, 0, 546, 547, 5, 77, 0, 0, 547, 548, 5, 97, 0, 0, 548, 549, 5, 112, 0,
        0, 549, 94, 1, 0, 0, 0, 550, 551, 5, 115, 0, 0, 551, 552, 5, 101, 0, 0, 552, 553, 5, 116,
        0, 0, 553, 96, 1, 0, 0, 0, 554, 555, 5, 114, 0, 0, 555, 556, 5, 97, 0, 0, 556, 557, 5,
        105, 0, 0, 557, 558, 5, 115, 0, 0, 558, 559, 5, 101, 0, 0, 559, 98, 1, 0, 0, 0, 560, 561,
        5, 114, 0, 0, 561, 562, 5, 101, 0, 0, 562, 563, 5, 114, 0, 0, 563, 564, 5, 97, 0, 0, 564,
        565, 5, 105, 0, 0, 565, 566, 5, 115, 0, 0, 566, 567, 5, 101, 0, 0, 567, 100, 1, 0, 0,
        0, 568, 569, 5, 102, 0, 0, 569, 570, 5, 97, 0, 0, 570, 571, 5, 105, 0, 0, 571, 572, 5,
        108, 0, 0, 572, 573, 5, 119, 0, 0, 573, 574, 5, 105, 0, 0, 574, 575, 5, 116, 0, 0, 575,
        576, 5, 104, 0, 0, 576, 102, 1, 0, 0, 0, 577, 578, 5, 105, 0, 0, 578, 579, 5, 110, 0,
        0, 579, 580, 5, 118, 0, 0, 580, 581, 5, 97, 0, 0, 581, 582, 5, 108, 0, 0, 582, 583, 5,
        105, 0, 0, 583, 584, 5, 100, 0, 0, 584, 585, 5, 65, 0, 0, 585, 586, 5, 114, 0, 0, 586,
        587, 5, 103, 0, 0, 587, 104, 1, 0, 0, 0, 588, 589, 5, 118, 0, 0, 589, 590, 5, 97, 0, 0,
        590, 591, 5, 108, 0, 0, 591, 106, 1, 0, 0, 0, 592, 593, 5, 116, 0, 0, 593, 594, 5, 114,
        0, 0, 594, 595, 5, 121, 0, 0, 595, 108, 1, 0, 0, 0, 596, 597, 5, 102, 0, 0, 597, 598,
        5, 105, 0, 0, 598, 599, 5, 110, 0, 0, 599, 600, 5, 97, 0, 0, 600, 601, 5, 108, 0, 0, 601,
        602, 5, 108, 0, 0, 602, 603, 5, 121, 0, 0, 603, 110, 1, 0, 0, 0, 604, 605, 5, 109, 0,
        0, 605, 606, 5, 97, 0, 0, 606, 607, 5, 116, 0, 0, 607, 608, 5, 99, 0, 0, 608, 609, 5,
        104, 0, 0, 609, 112, 1, 0, 0, 0, 610, 611, 5, 119, 0, 0, 611, 612, 5, 105, 0, 0, 612,
        613, 5, 116, 0, 0, 613, 614, 5, 104, 0, 0, 614, 114, 1, 0, 0, 0, 615, 616, 5, 117, 0,
        0, 616, 617, 5, 115, 0, 0, 617, 618, 5, 101, 0, 0, 618, 116, 1, 0, 0, 0, 619, 620, 5,
        117, 0, 0, 620, 621, 5, 115, 0, 0, 621, 622, 5, 105, 0, 0, 622, 623, 5, 110, 0, 0, 623,
        624, 5, 103, 0, 0, 624, 118, 1, 0, 0, 0, 625, 626, 5, 119, 0, 0, 626, 627, 5, 104, 0,
        0, 627, 628, 5, 101, 0, 0, 628, 629, 5, 110, 0, 0, 629, 120, 1, 0, 0, 0, 630, 631, 5,
        101, 0, 0, 631, 632, 5, 120, 0, 0, 632, 633, 5, 99, 0, 0, 633, 634, 5, 101, 0, 0, 634,
        635, 5, 112, 0, 0, 635, 636, 5, 116, 0, 0, 636, 637, 5, 105, 0, 0, 637, 638, 5, 111,
        0, 0, 638, 639, 5, 110, 0, 0, 639, 122, 1, 0, 0, 0, 640, 641, 5, 111, 0, 0, 641, 642,
        5, 102, 0, 0, 642, 124, 1, 0, 0, 0, 643, 644, 5, 46, 0, 0, 644, 126, 1, 0, 0, 0, 645, 646,
        5, 46, 0, 0, 646, 647, 5, 46, 0, 0, 647, 128, 1, 0, 0, 0, 648, 649, 5, 33, 0, 0, 649, 130,
        1, 0, 0, 0, 650, 651, 5, 44, 0, 0, 651, 132, 1, 0, 0, 0, 652, 653, 5, 59, 0, 0, 653, 134,
        1, 0, 0, 0, 654, 655, 5, 58, 0, 0, 655, 136, 1, 0, 0, 0, 656, 657, 5, 60, 0, 0, 657, 658,
        5, 45, 0, 0, 658, 138, 1, 0, 0, 0, 659, 660, 5, 124, 0, 0, 660, 661, 5, 62, 0, 0, 661,
        140, 1, 0, 0, 0, 662, 663, 5, 95, 0, 0, 663, 142, 1, 0, 0, 0, 664, 665, 5, 45, 0, 0, 665,
        666, 5, 62, 0, 0, 666, 144, 1, 0, 0, 0, 667, 668, 5, 62, 0, 0, 668, 669, 5, 62, 0, 0, 669,
        146, 1, 0, 0, 0, 670, 671, 5, 43, 0, 0, 671, 148, 1, 0, 0, 0, 672, 673, 5, 45, 0, 0, 673,
        150, 1, 0, 0, 0, 674, 675, 5, 42, 0, 0, 675, 152, 1, 0, 0, 0, 676, 677, 5, 47, 0, 0, 677,
        154, 1, 0, 0, 0, 678, 679, 5, 42, 0, 0, 679, 680, 5, 42, 0, 0, 680, 156, 1, 0, 0, 0, 681,
        682, 5, 37, 0, 0, 682, 158, 1, 0, 0, 0, 683, 684, 5, 61, 0, 0, 684, 160, 1, 0, 0, 0, 685,
        686, 5, 60, 0, 0, 686, 687, 5, 62, 0, 0, 687, 162, 1, 0, 0, 0, 688, 689, 5, 60, 0, 0, 689,
        164, 1, 0, 0, 0, 690, 691, 5, 62, 0, 0, 691, 166, 1, 0, 0, 0, 692, 693, 5, 60, 0, 0, 693,
        694, 5, 61, 0, 0, 694, 168, 1, 0, 0, 0, 695, 696, 5, 62, 0, 0, 696, 697, 5, 61, 0, 0, 697,
        170, 1, 0, 0, 0, 698, 699, 5, 38, 0, 0, 699, 700, 5, 38, 0, 0, 700, 172, 1, 0, 0, 0, 701,
        702, 5, 124, 0, 0, 702, 703, 5, 124, 0, 0, 703, 174, 1, 0, 0, 0, 704, 705, 5, 60, 0, 0,
        705, 706, 5, 60, 0, 0, 706, 707, 5, 60, 0, 0, 707, 176, 1, 0, 0, 0, 708, 709, 5, 62, 0,
        0, 709, 710, 5, 62, 0, 0, 710, 711, 5, 62, 0, 0, 711, 178, 1, 0, 0, 0, 712, 713, 5, 38,
        0, 0, 713, 714, 5, 38, 0, 0, 714, 715, 5, 38, 0, 0, 715, 180, 1, 0, 0, 0, 716, 717, 5,
        124, 0, 0, 717, 718, 5, 124, 0, 0, 718, 719, 5, 124, 0, 0, 719, 182, 1, 0, 0, 0, 720,
        721, 5, 94, 0, 0, 721, 722, 5, 94, 0, 0, 722, 723, 5, 94, 0, 0, 723, 184, 1, 0, 0, 0, 724,
        725, 5, 126, 0, 0, 725, 726, 5, 126, 0, 0, 726, 727, 5, 126, 0, 0, 727, 186, 1, 0, 0,
        0, 728, 729, 5, 110, 0, 0, 729, 730, 5, 111, 0, 0, 730, 731, 5, 116, 0, 0, 731, 188,
        1, 0, 0, 0, 732, 733, 5, 58, 0, 0, 733, 734, 5, 63, 0, 0, 734, 190, 1, 0, 0, 0, 735, 736,
        5, 40, 0, 0, 736, 192, 1, 0, 0, 0, 737, 738, 5, 41, 0, 0, 738, 194, 1, 0, 0, 0, 739, 740,
        5, 123, 0, 0, 740, 196, 1, 0, 0, 0, 741, 742, 5, 125, 0, 0, 742, 198, 1, 0, 0, 0, 743,
        744, 5, 91, 0, 0, 744, 200, 1, 0, 0, 0, 745, 746, 5, 93, 0, 0, 746, 202, 1, 0, 0, 0, 747,
        748, 5, 34, 0, 0, 748, 204, 1, 0, 0, 0, 749, 750, 5, 105, 0, 0, 750, 751, 5, 102, 0, 0,
        751, 206, 1, 0, 0, 0, 752, 753, 5, 101, 0, 0, 753, 754, 5, 108, 0, 0, 754, 755, 5, 105,
        0, 0, 755, 756, 5, 102, 0, 0, 756, 208, 1, 0, 0, 0, 757, 758, 5, 101, 0, 0, 758, 759,
        5, 108, 0, 0, 759, 760, 5, 115, 0, 0, 760, 761, 5, 101, 0, 0, 761, 210, 1, 0, 0, 0, 762,
        763, 5, 124, 0, 0, 763, 212, 1, 0, 0, 0, 764, 768, 7, 11, 0, 0, 765, 767, 7, 11, 0, 0,
        766, 765, 1, 0, 0, 0, 767, 770, 1, 0, 0, 0, 768, 766, 1, 0, 0, 0, 768, 769, 1, 0, 0, 0,
        769, 214, 1, 0, 0, 0, 770, 768, 1, 0, 0, 0, 771, 772, 7, 12, 0, 0, 772, 216, 1, 0, 0, 0,
        18, 0, 220, 230, 234, 242, 247, 254, 262, 267, 273, 276, 286, 299, 307, 309, 326,
        332, 768, 1, 6, 0, 0
    ]


class FSharpLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    WHITE_SPACE = 1
    COMMENT = 2
    INT = 3
    FLOAT = 4
    INTERPOLATIONSIGN = 5
    CHAR = 6
    STRING = 7
    INTERPOLATED_STRING = 8
    BOOL = 9
    UNIT = 10
    REC = 11
    PUBLIC = 12
    PRIVATE = 13
    INTERNAL = 14
    MUTABLE = 15
    LET = 16
    FUN = 17
    WHILE = 18
    DO = 19
    FOR = 20
    TO = 21
    DOWNTO = 22
    IN = 23
    DOLLAR = 24
    TYPE = 25
    MODULE = 26
    OPEN = 27
    NAMESPACE = 28
    CLASS = 29
    END = 30
    STRUCT = 31
    WITH_AND = 32
    INTERFACE = 33
    GET = 34
    INHERIT = 35
    OVERRIDE = 36
    DEFAULT = 37
    ABSTRACT = 38
    BASE = 39
    ASYNC = 40
    TASK = 41
    NEW = 42
    THEN = 43
    THIS = 44
    MEMBER = 45
    SEQ = 46
    MAP = 47
    SET = 48
    RAISE = 49
    RERAISE = 50
    FAILWITH = 51
    INVALIDARG = 52
    VAL = 53
    TRY = 54
    FINALLY = 55
    MATCH = 56
    WITH = 57
    USE = 58
    USING = 59
    WHEN = 60
    EXCEPTION = 61
    OF = 62
    DOT = 63
    DOTDOT = 64
    EXCLAMATION_MARK = 65
    COMMA = 66
    SEMICOLON = 67
    COLON = 68
    ASSIGN = 69
    PIPE = 70
    MISSING_ARG = 71
    RIGHT_ARROW = 72
    COMPOS = 73
    ADD = 74
    MINUS = 75
    MUL = 76
    DIV = 77
    POW = 78
    MOD = 79
    EQUAL = 80
    NOT_EQUAL = 81
    LESS = 82
    GREATER = 83
    LESS_EQUAL = 84
    GREATER_EQUAL = 85
    AND = 86
    OR = 87
    LSHIFT = 88
    RSHIFT = 89
    LOG_MUL = 90
    LOG_ADD = 91
    LOG_XOR = 92
    LOG_NOT = 93
    NOT = 94
    COLON_Q = 95
    OPEN_PAREN = 96
    CLOSE_PAREN = 97
    OPEN_BRACE = 98
    CLOSE_BRACE = 99
    OPEN_BRACKET = 100
    CLOSE_BRACKET = 101
    DOUBLE_QUOTES = 102
    IF = 103
    ELIF = 104
    ELSE = 105
    VERTICAL_LINE = 106
    IDENTIFIER = 107
    SINGLE_CHARACTER = 108

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'rec'", "'public'", "'private'", "'internal'", "'mutable'",
                    "'let'", "'fun'", "'while'", "'do'", "'for'", "'to'", "'downto'",
                    "'in'", "'$'", "'type'", "'module'", "'open'", "'namespace'",
                    "'class'", "'end'", "'struct'", "'and'", "'interface'", "'get'",
                    "'inherit'", "'override'", "'default'", "'abstract'", "'base'",
                    "'async'", "'task'", "'new'", "'then'", "'this'", "'member'",
                    "'seq'", "'Map'", "'set'", "'raise'", "'reraise'", "'failwith'",
                    "'invalidArg'", "'val'", "'try'", "'finally'", "'match'", "'with'",
                    "'use'", "'using'", "'when'", "'exception'", "'of'", "'.'",
                    "'..'", "'!'", "','", "';'", "':'", "'<-'", "'|>'", "'_'", "'->'",
                    "'>>'", "'+'", "'-'", "'*'", "'/'", "'**'", "'%'", "'='", "'<>'",
                    "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", "'<<<'", "'>>>'",
                    "'&&&'", "'|||'", "'^^^'", "'~~~'", "'not'", "':?'", "'('",
                    "')'", "'{'", "'}'", "'['", "']'", "'\"'", "'if'", "'elif'",
                    "'else'", "'|'"]

    symbolicNames = ["<INVALID>",
                     "WHITE_SPACE", "COMMENT", "INT", "FLOAT", "INTERPOLATIONSIGN",
                     "CHAR", "STRING", "INTERPOLATED_STRING", "BOOL", "UNIT", "REC",
                     "PUBLIC", "PRIVATE", "INTERNAL", "MUTABLE", "LET", "FUN", "WHILE",
                     "DO", "FOR", "TO", "DOWNTO", "IN", "DOLLAR", "TYPE", "MODULE",
                     "OPEN", "NAMESPACE", "CLASS", "END", "STRUCT", "WITH_AND", "INTERFACE",
                     "GET", "INHERIT", "OVERRIDE", "DEFAULT", "ABSTRACT", "BASE",
                     "ASYNC", "TASK", "NEW", "THEN", "THIS", "MEMBER", "SEQ", "MAP",
                     "SET", "RAISE", "RERAISE", "FAILWITH", "INVALIDARG", "VAL",
                     "TRY", "FINALLY", "MATCH", "WITH", "USE", "USING", "WHEN", "EXCEPTION",
                     "OF", "DOT", "DOTDOT", "EXCLAMATION_MARK", "COMMA", "SEMICOLON",
                     "COLON", "ASSIGN", "PIPE", "MISSING_ARG", "RIGHT_ARROW", "COMPOS",
                     "ADD", "MINUS", "MUL", "DIV", "POW", "MOD", "EQUAL", "NOT_EQUAL",
                     "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "AND", "OR",
                     "LSHIFT", "RSHIFT", "LOG_MUL", "LOG_ADD", "LOG_XOR", "LOG_NOT",
                     "NOT", "COLON_Q", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE",
                     "CLOSE_BRACE", "OPEN_BRACKET", "CLOSE_BRACKET", "DOUBLE_QUOTES",
                     "IF", "ELIF", "ELSE", "VERTICAL_LINE", "IDENTIFIER", "SINGLE_CHARACTER"]

    ruleNames = ["WHITE_SPACE", "COMMENT", "INT", "FLOAT", "INTERPOLATIONSIGN",
                 "CHAR", "STRING", "INTERPOLATED_STRING", "BOOL", "UNIT",
                 "REC", "PUBLIC", "PRIVATE", "INTERNAL", "MUTABLE", "LET",
                 "FUN", "WHILE", "DO", "FOR", "TO", "DOWNTO", "IN", "DOLLAR",
                 "TYPE", "MODULE", "OPEN", "NAMESPACE", "CLASS", "END",
                 "STRUCT", "WITH_AND", "INTERFACE", "GET", "INHERIT", "OVERRIDE",
                 "DEFAULT", "ABSTRACT", "BASE", "ASYNC", "TASK", "NEW",
                 "THEN", "THIS", "MEMBER", "SEQ", "MAP", "SET", "RAISE",
                 "RERAISE", "FAILWITH", "INVALIDARG", "VAL", "TRY", "FINALLY",
                 "MATCH", "WITH", "USE", "USING", "WHEN", "EXCEPTION",
                 "OF", "DOT", "DOTDOT", "EXCLAMATION_MARK", "COMMA", "SEMICOLON",
                 "COLON", "ASSIGN", "PIPE", "MISSING_ARG", "RIGHT_ARROW",
                 "COMPOS", "ADD", "MINUS", "MUL", "DIV", "POW", "MOD",
                 "EQUAL", "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL",
                 "GREATER_EQUAL", "AND", "OR", "LSHIFT", "RSHIFT", "LOG_MUL",
                 "LOG_ADD", "LOG_XOR", "LOG_NOT", "NOT", "COLON_Q", "OPEN_PAREN",
                 "CLOSE_PAREN", "OPEN_BRACE", "CLOSE_BRACE", "OPEN_BRACKET",
                 "CLOSE_BRACKET", "DOUBLE_QUOTES", "IF", "ELIF", "ELSE",
                 "VERTICAL_LINE", "IDENTIFIER", "SINGLE_CHARACTER"]

    grammarFileName = "FSharpLexer.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
