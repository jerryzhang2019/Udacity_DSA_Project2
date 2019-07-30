# Problem 3: Huffman Coding 问题3:霍夫曼编码

import sys
class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1

        return frequency

    def make_heap(self, frequency):
        for char, freq in frequency.items():
            node = HeapNode(char, freq)
            self.heap.append(node)

    def merge_nodes(self):
        while len(self.heap) > 1:
            node1 = self.heap[0]
            del self.heap[0]
            node2 = self.heap[0]
            del self.heap[0]
            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            self.heap.append(merged)

    def make_codes_helper(self, root, current_code):
        if (root == None):
            return

        if (root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self, text):

        frequency = self.make_frequency_dict(text)
        self.make_heap(frequency)

        self.merge_nodes()
        self.root = self.heap[0]

        current_code = ""
        self.make_codes_helper(self.root, current_code)

    def huffman_encoding(self, text):
        self.make_codes(text)
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def huffman_decoding(self, data, tree):
        current_code = ""
        decoded_text = ""

        for bit in data:
            current_code += bit
            if (current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text


if __name__ == "__main__":
    codes = {}
# Test case1
a_great_sentence = "The bird is the word"
print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))
huffmanCoding = HuffmanCoding()
encodedText = huffmanCoding.huffman_encoding(a_great_sentence)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encodedText, base=2))))
print ("The content of the encoded data is: {}\n".format(encodedText))
decodedText = huffmanCoding.huffman_decoding(encodedText, None)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decodedText)))
print ("The content of the encoded data is: {}\n".format(decodedText))
# Test case2
a_SameChr_sentence = "AAAAAAAAAAAAAA."
print ("The size of the data is: {}\n".format(sys.getsizeof(a_SameChr_sentence)))
print ("The content of the data is: {}\n".format(a_SameChr_sentence))
huffmanCoding = HuffmanCoding()
encodedText = huffmanCoding.huffman_encoding(a_SameChr_sentence)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encodedText, base=2))))
print ("The content of the encoded data is: {}\n".format(encodedText))
decodedText = huffmanCoding.huffman_decoding(encodedText, None)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decodedText)))
print ("The content of the encoded data is: {}\n".format(decodedText))

# Test case3
a_empty_sentence = "No data to encode!"
print ("The size of the data is: {}\n".format(sys.getsizeof(a_empty_sentence)))
print ("The content of the data is: {}\n".format(a_empty_sentence))
huffmanCoding = HuffmanCoding()
encodedText = huffmanCoding.huffman_encoding(a_empty_sentence)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encodedText, base=2))))
print ("The content of the encoded data is: {}\n".format(encodedText))
decodedText = huffmanCoding.huffman_decoding(encodedText, None)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decodedText)))
print ("The content of the encoded data is: {}\n".format(decodedText))
