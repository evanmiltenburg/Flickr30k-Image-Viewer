# Image Annotation Tools
*For the Flickr30k dataset*

This repository contains all the code you need to look through the
Flickr30k images and write notes about them, right in your browser.
There are two separate tools: one general tool that I made for the annotation of unwarranted inferences (but that you can also just use to page through the data), and one tool that I made to quickly add tags to a subset of the images. Both tools were made using Flask.

If you use this tool in your research, I'd appreciate it if you cite [this paper](https://arxiv.org/abs/1605.06083).

```
@inproceedings{miltenburg2016stereotyping,
Author = {Emiel van Miltenburg},
Booktitle = {Proceedings of Multimodal Corpora: Computer vision and language processing (MMC 2016)},
Date-Added = {2016-05-15 16:08:52 +0000},
Date-Modified = {2016-05-15 16:11:58 +0000},
Editor = {Jens Edlund and Dirk Heylen and Patrizia Paggio},
Keywords = {ulm2},
Pages = {1-4},
Title = {Stereotyping and Bias in the Flickr30k Dataset},
Url = {http://www.lrec-conf.org/proceedings/lrec2016/workshops/LREC2016Workshop-MCC-2016-proceedings.pdf},
pdf = {http://www.lrec-conf.org/proceedings/lrec2016/workshops/LREC2016Workshop-MCC-2016-proceedings.pdf},
Year = {2016}}
```

**Requirements**

* Flask
* Python 3 (the code may also work on Python 2, but I only tested it on 3)
* The Flickr30kEntities dataset (images + descriptions)

**Set-up**

* Clone this repository
* Copy the Flickr30k data to the relevant folders in `./static/`
* Install Flask

## General tool
The general tool is very versatile. It features navigation (so you can go to the first, previous, random, next, and last image), and several text boxes for annotation.

The top four input fields are easily modifiable through Javascript (see `templates/image_page.html`). I made them so that the annotations get written to the larger text area in a standardized (machine-readable) format. Just write down your thoughts in any of the four categories and press Enter. The text area contains everything that will be saved to an external file called `comments.txt`. When you're done annotating an image, press 'submit' and your annotations are appended to the comments file.

<img src="screenshots/image_viewer.png" alt="Screenshot of the image viewer tool">

Start this tool by running `python image_viewer.py` on the command line. Python will then serve the image viewer at `http://127.0.0.1:5000/`.

## Subset tagger
This tool is useful if you want to quickly tag a portion of the data, for example a sample of the files that contain the word 'baby'. Here is how to use this tool:

1. Write all the relevant file IDs to a `.txt` file in the `noun_files` directory. E.g. `baby.txt`.

2. Start this tool by running `python annotate_selection.py` on the command line. Python will then serve the image viewer at `http://127.0.0.1:5000/`.

3. Enter the file name in the 'Submit file' window:
<img src="screenshots/annotate_selection1.png" alt="Screenshot of the subset annotation tool">

4. Start tagging. The tool will automatically add new tags that you enter in the 'other' text box.
<img src="screenshots/annotate_selection2.png" alt="Screenshot of the subset annotation tool">
