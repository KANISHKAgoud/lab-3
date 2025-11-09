import heapq

# Node class for Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison for priority queue (min-heap)
    def __lt__(self, other):
        return self.freq < other.freq


# Function to generate Huffman codes
def huffman_encoding(chars, freqs):
    # Step 1: Create a min heap with (frequency, node)
    heap = [Node(chars[i], freqs[i]) for i in range(len(chars))]
    heapq.heapify(heap)  # convert list into min-heap

    # Step 2: Combine two smallest nodes until one tree remains
    while len(heap) > 1:
        # Extract two smallest frequency nodes
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new internal node with combined frequency
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        # Add new node back to heap
        heapq.heappush(heap, new_node)

    # Step 3: Generate codes from the Huffman tree
    root = heap[0]
    codes = {}

    def generate_codes(node, current_code):
        if node is None:
            return
        # If it's a leaf node → store the character and code
        if node.char is not None:
            codes[node.char] = current_code
            return
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root, "")

    return codes


# Example usage:
chars = ['A', 'B', 'C', 'D', 'E', 'F']
freqs = [5, 9, 12, 13, 16, 45]

codes = huffman_encoding(chars, freqs)

print("Character\tFrequency\tHuffman Code")
for ch in chars:
    print(f"{ch}\t\t{freqs[chars.index(ch)]}\t\t{codes[ch]}")
