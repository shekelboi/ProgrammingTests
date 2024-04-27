# API homework

Note that all the following steps should be done within Python, except for the last one, which can be done manually.

## Generate a random number

Generate a random number between 5 and 15 using the [Random Number API](https://www.randomnumberapi.com/).
Store the generated number in a variable, since we will use it in the next step.

## Download pictures of Shiba Inus

Using [shibe.online](https://shibe.online/) download as many pictures of Shiba Inus
as the random number generated in the previous step. The names of the files can be the names of the original files.

## Zip the images

[Zip](https://docs.python.org/3/library/zipfile.html) the downloaded images
(using ZIP_DEFLATED compression method), remove the original images, only keeping the zip file.

## Upload the zip file to 0x0.st

Upload the created zip file to [0x0.st](https://0x0.st/) with 48h expiration.
Remove your local zip file (don't forget to close the filestream first if you're not using the with keyword).

## Send the link

In the thread where I sent the homework, reply with the link to your zip file.