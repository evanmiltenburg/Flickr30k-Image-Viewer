from flask import Flask, url_for, request, render_template, redirect
from glob import iglob
import random
import os
app = Flask(__name__)

#setup:
def make_image_dict():
    d = dict()
    text_files = iglob('static/Flickr30kEntities/Sentences/*.txt')
    for text_file in text_files:
        image_number = text_file.split('/')[-1].strip('.txt')
        image_file = ''.join(['/static/images/', image_number ,'.jpg'])
        d[image_number] = (text_file, image_file)
    return d

image_dict = make_image_dict()
all_image_numbers = sorted(image_dict.keys(), key = lambda x:int(x))
total = len(all_image_numbers)
maxnum = total - 1
# Pages
@app.route('/')
def main_page():
    image_number = all_image_numbers[0]
    return redirect('/image/'+str(image_number))

@app.route('/image/<image_number>',methods=['GET','POST'])
def image_page(image_number):
    if request.method == "POST":
        comment = request.form['comments']
        save_comment(comment, image_number)
        comment_saved = 'comment saved'
    elif request.method == 'GET':
        comment_saved = ''
        if image_number == 'RANDOM':
            image_number = random.choice(all_image_numbers)
        elif image_number == 'FIRST':
            image_number = all_image_numbers[0]
        elif image_number == 'LAST':
            image_number = all_image_numbers[-1]
    current = all_image_numbers.index(image_number)
    if current > 0:
        previous = url_for_image(all_image_numbers[current-1])
    else:
        previous = None
    if current < maxnum:
        following = url_for_image(all_image_numbers[current+1])
    else:
        following = None
    if image_number in image_dict:
        captions, image = image_dict[image_number]
        with open(captions) as f:
            caption_data = dict(enumerate(f.readlines()))
        return render_template('image_page.html',
                                image = image,
                                image_number = image_number,
                                comment_saved = comment_saved,
                                current = current,
                                total = total,
                                captions = caption_data,
                                previous = previous,
                                following = following)

# Logic
def url_for_image(image_number):
    return url_for('image_page', image_number=image_number)

def save_comment(comment, image_number):
    with open('comments.txt', 'a') as f:
        f.write('\n------------------\nImage: ' + str(image_number) + '\n')
        f.write(comment)

if __name__ == '__main__':
    app.debug = True
    app.run()
