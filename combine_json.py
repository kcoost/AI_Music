from argparse import ArgumentParser
import glob
import os
from tqdm import tqdm
import json

if __name__ == '__main__':
    parser = ArgumentParser()
    # model args
    parser.add_argument('--data_path', type = str, default = "song_data_maestro/", help='N')#ethicscommonsense

    args = parser.parse_args()

    file_names = glob.glob(os.path.join(args.data_path, '**/*.json'), recursive=True)

    all_data = {}

    for file_name in tqdm(file_names):
        with open(file_name) as f:
            song_data = json.load(f)
        all_data.update(song_data)
    with open('all_data_maestro.json', 'w') as f:
        json.dump(all_data, f)
