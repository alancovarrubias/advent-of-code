FILENAME = "files/08.txt"
WIDTH = 25
HEIGHT = 6
LAYER_LENGTH = WIDTH * HEIGHT

def get_layers(filename):
    with open(filename) as f:
        image_bits = list(map(int, list(f.readline().rstrip())))
        layers = [image_bits[i:i+LAYER_LENGTH] for i in range(0, len(image_bits), LAYER_LENGTH)]
        return layers

layers = get_layers(FILENAME)
zero_counts = list(map(lambda layer: layer.count(0), layers))
min_zeros = min(zero_counts)
min_zero_index = zero_counts.index(min_zeros)
min_zero_layer = layers[min_zero_index]
print(min_zero_layer.count(1) * min_zero_layer.count(2))

decoded_image = [None for i in range(LAYER_LENGTH)]
for layer in layers:
    for i in range(LAYER_LENGTH):
        if decoded_image[i] == None and layer[i] != 2:
            decoded_image[i] = layer[i]
    print(decoded_image)
decoded_image = list(map(str, decoded_image))
