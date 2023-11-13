from flask import Flask, request, render_template
from image_processor import extract_number_plate
from utils import read_csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['image_name']
    if uploaded_file.filename != '':
        file_path = 'uploads/' + uploaded_file.filename
        uploaded_file.save(file_path)
        result = extract_number_plate(file_path)
        gis_data = read_csv("gis.csv", result["number_plate"])
        result.update(gis_data)
        return f'Number Plate: {result["number_plate"]}<br>Vehicle Type: {result["description"]} <br>Last Seen: {result["last_seen"]} <br>Last Known Location: {result["last_location"]} <br>Latitude: {result["latitude"]} <br>Longitude: {result["longitude"]}'
    return 'No file uploaded!'

if __name__ == "__main__":
    app.run(debug=True)