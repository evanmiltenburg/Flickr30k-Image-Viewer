from flask import Flask, url_for, request, render_template, redirect
import csv
app = Flask(__name__)

categories = set()
id_to_category_dict = dict()

def image_url(image_id):
    image_id = image_id.strip()
    return ''.join(['/static/images/', image_id ,'.jpg'])

def url_to_id(url):
    return url.split('/')[-1].split('.')[0]

@app.route('/')
def main_page():
    return render_template('listfiles.html')

@app.route('/submit_filelist', methods=['POST'])
def load_first_time():
    """
    Called with the POST method to pass a filename. Load the file (and the image
    IDs therein), and initialize all relevant variables for the annotation.
    """
    # Globals used in this function:
    global image_url_list   # defined
    global annotations_file # defined
    global max_index        # defined
    filename = request.form['files']
    annotations_file = filename.replace('.txt','-annotated.tsv')
    with open('noun_files/'+filename) as f:
        image_url_list = [image_url(image_id) for image_id in f if not image_id=='']
        print(image_url_list)
    max_index = len(image_url_list) - 1
    return render_template('custom_annotate_images.html',
                           image_url=image_url_list[0],
                           categories=categories)

@app.route('/submit_category', methods=['POST'])
def submit_category():
    """
    Called when a category label is submitted for an image.
    Adds the category label to the dict.
    If we're done, writes out the data to a file.
    If not, goes to the next item.
    """
    # Globals used in this function:
    global categories           # defined before, modified here.
    global max_index            # defined before, modified here.
    global image_url_list       # defined before.
    global url_to_category_dict # defined before, modified here.
    global annotations_file     # defined before.
    cat = request.form['category']
    if cat == 'OTHER':
        cat = request.form['other']
        categories.add(cat)
    image_url = request.form['image_url']
    image_id = url_to_id(image_url)
    id_to_category_dict[image_id] = cat
    current_index = image_url_list.index(image_url)
    if current_index == max_index:
        with open(annotations_file, 'w') as f:
            writer = csv.writer(f,delimiter='\t')
            writer.writerows(id_to_category_dict.items())
        return render_template('done.html')
    return render_template('custom_annotate_images.html',
                           image_url=image_url_list[current_index+1],
                           categories=categories)

if __name__ == '__main__':
    app.debug = True
    app.run()
