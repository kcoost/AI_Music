# AI_Music

## How to use
run data_analysis.py to analyse your midi data
```bash 
python data_analysis.py --midi_path [where you have your midis stored] --data_path [where you want your jsons to be stored]
```

it just stores each song individually, so use combine_json.py to turn the jsons into a single file
```bash 
python combine_json.py --data_path [where you have your jsons stored]
```

plots.ipynb can be used to analyse this json file

## Results
I have used Michael's files, MAESTRO and Composing (https://composing.ai/dataset).
Check out the plots.ipynb file for results
