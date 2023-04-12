import argparse
from pathlib import Path

def get_maps(directory):
    for f in Path(directory).iterdir():
        if f.is_file() and f.name.endswith(".osu"):
            yield str(f)

def parse(beatmap_dir):
    objects = {}
    
    with open(beatmap_dir, "r", encoding="utf8") as f:
        in_hitobjects = False
        
        for line in f:
            # Check if in HitObjects section of file, if so then add a note to the timestamp
            if in_hitobjects:
                note_time = line.split(",")[2]
                objects[note_time] = objects.get(note_time, 0) + 1

            if '[HitObjects]' in line:
                in_hitobjects = True

    return objects

def compare(*beatmaps):
    # Create a set of all the points in all the beatmaps
    all_points = set()
    for beatmap in beatmaps:
        all_points.update(beatmap.keys())
        
    # Check for differences at each point across all beatmaps
    differences = []
    for point in all_points:
        values = set()
        for beatmap in beatmaps:
            values.add(beatmap.get(point, 0))
        if len(values) > 1:
            differences.append(point)
            
    return differences

def main():
    parser = argparse.ArgumentParser(description="Compare the hit objects of one or more beatmaps")
    parser.add_argument("--input_dir", "-i", nargs="?", default="input",
                        help="The directory containing the .osu files to compare (default: 'input')")
    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    if not input_dir.is_dir():
        print(f"Error: '{input_dir}' is not a valid directory.")
        return

    parsed_beatmaps = [parse(beatmap_dir) for beatmap_dir in get_maps(input_dir)]
    differences = compare(*parsed_beatmaps)

    if not differences:
        print("All beatmaps are identical!")
    else:
        print("The following timestamps have different hit objects:")
        print(differences)

if __name__ == "__main__":
    main()
