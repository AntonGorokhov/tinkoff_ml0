import json
import string
import sys
from model import Model


def read_text(input):
    content = open(input, "r").read()
    data = dict()
    new_content = ""
    for char in content:
        if char not in string.punctuation:
            new_content += char
    content = new_content
    content = content.lower().split()
    for i in range(len(content) - 1):
        if content[i] in data:
            data[content[i]].append(content[i + 1])
        else:
            data[content[i]] = [content[i + 1]]
    return data


def read_model(input):
    content = json.load(open(input).read())
    return content


def main():
    model = Model()
    input, output = sys.argv[1:3]
    data = read_text(input)
    model.learn(data)
    open(output, 'w').write(json.dumps(model.data))


if __name__ == '__main__':
    main()

