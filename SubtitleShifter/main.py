import datetime as dt
import argparse


class SubtitleBlock:
    @staticmethod
    def timedelta_to_timestamp(delta: dt.timedelta):
        dummy = dt.datetime(1900, 1, 1)
        return (dummy + delta).strftime('%H:%M:%S,%f')[:-3]

    @staticmethod
    def timestamp_to_timedelta(text: str):
        parts = text.split(',')
        milliseconds = int(parts[1])
        timestamp = [int(p) for p in parts[0].split(':')]
        return dt.timedelta(hours=timestamp[0], minutes=timestamp[1], seconds=timestamp[2], milliseconds=milliseconds)

    def __init__(self, text: str):
        lines = text.splitlines()
        self.id = int(lines[0])
        timestamps = lines[1].split(' --> ')
        deltas = [SubtitleBlock.timestamp_to_timedelta(timestamp) for timestamp in timestamps]
        self.start = deltas[0]
        self.end = deltas[1]
        self.text = '\n'.join(lines[2:])

    def shift_by(self, seconds):
        shift = dt.timedelta(seconds=seconds)
        # We have to shift by at least the negative value of the starting point in the given block
        # I.e. we cannot shift below 0, as it would not make sense in case of a subtitle,
        # since the smallest starting point is 00:00:00,000
        if -self.start <= shift:
            self.start += shift
            self.end += shift
        else:
            raise Exception('Output value of the timestamp cannot be lower than 0.')

    def get_words(self):
        words = []
        text = self.text.lower()
        current = ''
        for i in range(len(text)):
            if text[i].isalpha() or text[i] == "'":
                current += text[i]
            elif current:
                words.append(current)
                current = ""
        if current:
            words.append(current)
        return words

    def __str__(self):
        deltas = [self.start, self.end]
        timestamps = [SubtitleBlock.timedelta_to_timestamp(delta) for delta in deltas]
        timestamps = ' --> '.join(timestamps)
        return f'{self.id}\n{timestamps}\n{self.text}'


class Subtitle:
    def __init__(self, text_blocks):
        self.blocks = []
        for t in text_blocks:
            self.blocks.append(SubtitleBlock(t))

    def write_to_file(self, path):
        with open(path, 'w', encoding='utf-8') as file:
            file.write('\n\n'.join(str(block) for block in self.blocks))

    def shift_by(self, seconds):
        for b in self.blocks:
            b.shift_by(seconds)

    def replace_text(self, original, modified):
        for b in self.blocks:
            b.text = b.text.replace(original, modified)
            b.text = b.text.replace(original.lower(), modified)

    def count_words(self):
        words = {}
        for b in self.blocks:
            for w in b.get_words():
                if w in words:
                    words[w] += 1
                else:
                    words[w] = 1
        return words


# In order to use these arguments, execute the Python script from the CLI
parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', default='The Social Network.srt', metavar='"input file"')
parser.add_argument('--output', '-o', default='modified.srt', metavar='"output file"')
parser.add_argument('--shiftby', '-s', metavar='seconds', type=float)
parser.add_argument('--replace', '-r', metavar='original/modified')
parser.add_argument('--count', '-c', metavar='word')
args = parser.parse_args()

with open(args.input, encoding='utf-8') as file:
    text_blocks = file.read().split('\n\n')

subtitle = Subtitle(text_blocks)

if args.shiftby:
    subtitle.shift_by(args.shiftby)
if args.replace:
    original, modified = args.replace.split('/')
    subtitle.replace_text(original, modified)
if args.count:
    d = subtitle.count_words()
    word = args.count.lower()
    val = d.get(word)
    print(val if val else "It is not said in the movie.")
    # If you want to display the entire dictionary sorted by the values:
    # print(sorted(d.items(), key=lambda t: t[1], reverse=True))
subtitle.write_to_file(args.output)
