## Beatmap Comparator

This tool compares two or more .osu beatmap files to find differences in the number of notes at each timestamp. Useful for finding missing notes when doing hitsound stuff.

### Usage

	python beatmap_parser.py [-h] [--files FILES [FILES ...]] [--directory DIRECTORY]

The following command-line arguments are supported:

* `-h`, `--help`: Show help message and exit.
* `-i`, `--input_dir`: The path to the directory containing the beatmap files. Defaults to `input`.

### Example Usage

Compare all `.osu` files in the input directory:

	python beatmap_parser.py

Compare all `.osu` files in `C:\Users\Konomi\AppData\Local\osu!\Songs\example`:

	python beatmap_parser.py -i "C:\Users\Konomi\AppData\Local\osu!\Songs\example"