import os
import json
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, jsonify
import threading
import time

app = Flask(__name__)

# Load the dataset and initialize variables
dataset_path = "./data/sample.json"
os.makedirs("./annotations", exist_ok=True)
save_path = "./annotations/annotations.json"

dataset = pd.read_json(dataset_path)
annotations = [[] for _ in range(len(dataset))]
current_index = 0

# List of available classes
class_options = [
    "Biology",
    "Ecotoxicology",
    "Geology",
    "Ecology",
    "Sedimentology",
    "Geomorphology",
    "Oceanography",
    "Hydrology",
    "Climatology",
    "Engineering",
    "Social Sciences & Humanities",
    "Chemistry",
    "Policy and Governance",
    "Public Health",
]

# Load annotations if available
if os.path.exists(save_path):
    saved_data = pd.read_json(save_path, orient="records", lines=True)
    annotations = saved_data["annotation"].tolist()
    current_index = len([a for a in annotations if a])


def save_annotations():
    """Save annotations to the file."""
    dataset["annotation"] = annotations
    dataset.to_json(save_path, orient="records", lines=True)


def auto_save():
    """Auto-save annotations every 10 minutes and archive with datetime."""
    while True:
        time.sleep(600)
        save_annotations()
        archive_save()


def archive_save():
    """Archive the current annotations with a timestamp."""
    os.makedirs("./archives/", exist_ok=True)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    archive_path = f"./archives/annotations_{timestamp}.json"
    dataset["annotation"] = annotations
    dataset.to_json(archive_path, orient="records", lines=True)


# Start auto-saving in a background thread
auto_save_thread = threading.Thread(target=auto_save, daemon=True)
auto_save_thread.start()


@app.route("/")
def index():
    """Render the main page with the current text."""
    return render_template(
        "index.html",
        text=dataset.iloc[current_index],
        current_index=current_index + 1,
        total=len(dataset),
        class_options=class_options,
    )


@app.route("/classify", methods=["POST"])
def classify():
    """Handle the classification of text."""
    global current_index
    classifications = request.form.get("classification").split(",")
    if classifications:
        annotations[current_index] = classifications
        current_index += 1
        if current_index >= len(dataset):
            save_annotations()
            return render_template("done.html")
    return redirect(url_for("index"))


@app.route("/navigate/<direction>")
def navigate(direction):
    """Navigate through the dataset."""
    global current_index
    if direction == "left" and current_index > 0:
        current_index -= 1
    elif direction == "right" and current_index < len(dataset) - 1:
        current_index += 1
    return redirect(url_for("index"))


@app.route("/menu")
def menu():
    """Display the menu for selecting texts."""
    menu_items = [
        {"index": idx, "text": f"Text {idx + 1}", "classified": bool(annotations[idx])}
        for idx in range(len(dataset))
    ]
    return render_template("menu.html", menu_items=menu_items)


@app.route("/select/<int:index>")
def select_text(index):
    """Select a specific text to annotate."""
    global current_index
    current_index = index
    return redirect(url_for("index"))


@app.route("/autosave", methods=["POST"])
def autosave():
    """Auto-save annotations as soon as they are modified."""
    global current_index
    data = request.json
    classification = data.get("classification", [])

    if classification is not None:
        annotations[current_index] = classification
        save_annotations()
        return jsonify({"message": "Saved successfully!"}), 200
    else:
        return jsonify({"error": "Invalid data"}), 400


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
