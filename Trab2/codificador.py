from skimage import io
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('important_names', metavar='N', type=str, nargs='+', help='texts')
args = parser.parse_args()

img = io.imread(args.important_names[0])
x, y, rgb = img.shape

with open(args.important_names[1]) as f:
    text_data = f.read()
f.closed

plano_bits = int(args.important_names[2])
list = []
for c in text_data:
    list.append(format(ord(c), '07b'))
list.append(format(3, '07b'))

n_letter = 0
letter_bit_pos = 0
cur_word = list[0]

#Loop Principal responsável pela codificação da Imagem
for i in range(0, x):
    for j in range(0, y):
        for k in range(0, rgb):
            if n_letter < len(list):
                #Proxima Palavra eh colocada
                if letter_bit_pos >= len(cur_word):
                    letter_bit_pos = 0
                    n_letter = n_letter+1
                    if (n_letter) < len(list):
                        cur_word = list[n_letter]
                    else:
                        break
                if list[n_letter][letter_bit_pos] == '1':
                    img[i,j,k] = img[i,j,k]|(1<<plano_bits)
                else:
                    img[i,j,k] = img[i,j,k]&(255&(0<<plano_bits))
                letter_bit_pos = letter_bit_pos +1
            else:
                break

io.imsave(args.important_names[3], img)
