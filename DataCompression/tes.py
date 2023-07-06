import heapq
from collections import defaultdict

def build_frequency_dict(image):
    frequency_dict = defaultdict(int)
    for pixel in image:
        frequency_dict[pixel] += 1
    return frequency_dict

def build_huffman_tree(frequency_dict):
    heap = [[weight, [pixel, ""]] for pixel, weight in frequency_dict.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]

def build_huffman_codes(tree):
    huffman_codes = {}
    for pair in tree[1:]:
        pixel = pair[0]
        code = pair[1]
        huffman_codes[pixel] = code
    return huffman_codes

image = input("Masukkan data citra yang ingin dikompresi: ")
frequency_dict = build_frequency_dict(image)
huffman_tree = build_huffman_tree(frequency_dict)
huffman_codes = build_huffman_codes(huffman_tree)
print("Kode Huffman:")
for pixel, code in huffman_codes.items():
    print(pixel, ":", code)