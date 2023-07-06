import heapq
import os
from PIL import Image


class HuffmanNode:
    def __init__(self, frequency, pixel=None):
        self.frequency = frequency
        self.pixel = pixel
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def calculate_frequency(image):
    frequency = {}
    width, height = image.size

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            if pixel in frequency:
                frequency[pixel] += 1
            else:
                frequency[pixel] = 1
    return frequency


def build_huffman_tree(frequency):
    heap = []
    for pixel, freq in frequency.items():
        heapq.heappush(heap, HuffmanNode(freq, pixel=pixel))

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged_node = HuffmanNode(node1.frequency + node2.frequency)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(heap, merged_node)

    return heap[0]


def build_codewords_mapping(root):
    codewords_mapping = {}

    def traverse(node, current_codeword):
        if node.pixel is not None:
            codewords_mapping[node.pixel] = current_codeword
        else:
            traverse(node.left, current_codeword + '0')
            traverse(node.right, current_codeword + '1')

    traverse(root, '')

    return codewords_mapping


def compress_image(image, codewords_mapping):
    compressed_data = ''
    width, height = image.size

    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            compressed_data += codewords_mapping[pixel]

    padding_length = 8 - (len(compressed_data) % 8)
    compressed_data += '0' * padding_length
    padded_data = '{:08b}'.format(padding_length)
    compressed_data = padded_data + compressed_data

    byte_array = bytearray()
    for i in range(0, len(compressed_data), 8):
        byte = compressed_data[i:i + 8]
        byte_array.append(int(byte, 2))

    return bytes(byte_array)


def compress_image_with_huffman(image_path):
    image = Image.open(image_path)
    frequency = calculate_frequency(image)
    huffman_tree = build_huffman_tree(frequency)
    codewords_mapping = build_codewords_mapping(huffman_tree)
    compressed_data = compress_image(image, codewords_mapping)

    return compressed_data, codewords_mapping


def save_compressed_image(image_path, compressed_data):
    filename, ext = os.path.splitext(image_path)
    output_path = filename + '_compressed' + ext
    with open(output_path, 'wb') as output_file:
        output_file.write(compressed_data)
    print("Compressed image saved as", output_path)


# Contoh penggunaan
image_path = input("Masukkan path gambar: ")
compressed_data, codewords_mapping = compress_image_with_huffman(image_path)
save_compressed_image(image_path, compressed_data)

print("Compressed data:", compressed_data)
print("Codewords mapping:", codewords_mapping)
