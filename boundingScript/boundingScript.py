import os
import json


animal = 'Bear'

path = f'./data/{animal}/Label'

os.chdir(path)

output_object = {
        "version": 1,
        "type": "bounding-box-labels",
        "boundingBoxes": {}
    }

# loop over every file in dir
for file in os.listdir():
    # open every file that ends with .txt
    if file.endswith('.txt'):
        with open(file, 'r') as f:
            # append each line to list and append labels list
            boxes = [line.rstrip() for line in f]
            # set image file name
            img = file.split('.')[0]
            img_name = f'{img}.jpg'
            output_object['boundingBoxes'][img_name] = []
            for box in boxes:
                # add box to picture
                [label, x, y, w, h] = box.split(' ')
                output_object['boundingBoxes'][img_name].append({
                    'label': label,
                    'x': int(float(x)),
                    'y': int(float(y)),
                    'width': int(float(w)),
                    'height': int(float(h))
                })

output_json  = json.dumps(output_object, indent=4)

os.chdir('../../../')

with open(f'bounding_boxes.labels', 'w') as file:
    file.write(output_json)


