# Domain annotation tool

## Description
In this repo, we implement a tool for annotating scientific abstracts about coastal areas within 11 domains:
- Ecology
- Sedimentology
- Geomorphology
- Oceanography
- Hydrology
- Climatology
- Engineering
- Social Sciences & Humanities
- Chemistry
- Policy and Governance
- Public Health

One abstract might have multiple labels.

The aim is to evaluate Llama on text classification into topics, multi-label.

## Requirements
Please install all the necessary libraries noted in [requirements.txt](./requirements.txt) using this command:

```
pip install -r requirements.txt
```

## How to use
```
python app.py
```

In the app, click on any class to attribute it to an abstract. The application has an autosave function, which means it will save at each modification. Your annotations will be available in `./annotations/annotations.json`. DO NOT DELETE THIS FILE, AS YOU WOULD LOSE ALL YOUR ANNOTATIONS.

## Contributors:

- :wheel: [DELAUNAY Julien](https://github.com/jdelaunay) :wheel: