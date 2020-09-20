import random
import sys
import json


class Model:
    def __init__(self):
        self.data = dict()

    def learn(self, new_data):
        for word in new_data.keys():
            if word in self.data:
                self.data[word].extend(new_data[word])
            else:
                self.data[word] = [new_data[word]]

    def generate(self, cnt_words):
        word = random.choice(list(self.data.keys()))
        text = [word]
        print(word)
        for i in range(cnt_words):
            if word in self.data:
                word = random.choice(self.data[word])
            else:
                word = random.choice(list(self.data.keys()))
                text.append('.')
            text.append(word[0][0])
            word = word[0][0]
        return text

def main():
    input, output = sys.argv[1:3]
    data = json.loads(open(input, "r").read())
    model = Model()
    model.learn(data)
    cnt_words = int(sys.argv[3])
    open(output, 'w').write(' '.join(model.generate(cnt_words)))



if __name__ == '__main__':
    main()