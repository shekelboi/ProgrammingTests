# Subtitle shifter

SRT files are used for storing subtitles of videos. Sometimes these subtitles are out of sync, and we want
to shift them by a certain duration to fix them.

Create a program that can load an SRT file and shift it by an arbitrary number of seconds
(the second can be floating point, this way enabling shifting even by milliseconds if the fraction part is specified).
The tool we are recreating is just like the one on [this website](https://subshifter.bitsnbites.eu/), however
we do not need to implement the `Linear correction` version. This website may also serve useful for you to
verify whether your program is working as expected by comparing the shifted values from the websites and
your program.

Considering the length of these files, it would be practical to do the comparison by a diff tool such as kdiff3.

## Outline

The following segment is a suggestion for the steps of implementing the subtitle shifting program.

1. Download an SRT file (any, [here is an example](https://dl.opensubtitles.org/en/download/file/1952867448) which has simply UTF-8 encoding without [BOM](https://en.wikipedia.org/wiki/Byte_order_mark)). Try to analyze it a bit to see the structure of it and recurring patterns. Feel free to
read about the structure of it.
2. Load the data, preferably into classes to make the workflow more structured and easier to reuse. Before starting
the loading process try to come up with a structure for storing the data. For the timestamps you may use timedelta or
come up with your own implementation.
3. Before implementing the shifting algorithm it would make sense to write the subtitle into a file to recreate the
original SRT that way ensuring that the data is loaded correctly.
4. Once you ensured that the loading process works as expected, you may start working on the shifting algorithm. If you
are using timedeltas, implementing the shifting process is quite straightforward. Make sure that the output timestamps
cannot be negative (the user can only shift as much in negative direction as the first timestamp in the subtitle file).

## Common pitfalls

- Be careful to load the subtitles with the correct encoding (use encoding='utf-8-sig'
if the encoding is UTF8 with BOM or convert it to UTF8 without BOM)
- If you are working with a datetime object, there is no native way using `strftime` to display milliseconds.
Feel free to use microseconds instead and truncate the last 3 characters.
- If you try another subtitle file than the one I provided, and you get an exception, make sure that the subtitle
file follows correct format everywhere

## Extra tasks

### Add an option to replace text

Add an option to replace text within the blocks of subtitles with something else.
You may build it as case-sensitive to make the implementation easier.

### Number of occurrences of a word

Count and print the number of occurrences of a word in the movie (make it case-insensitive). Pay attention to remove any
unnecessary characters, such as commas, periods, etc. while processing the text.