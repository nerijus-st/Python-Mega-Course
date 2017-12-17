from flask import Flask, render_template, request, send_file
import pandas
from geopy.geocoders import Nominatim
import datetime


app = Flask(__name__)
geolocator = Nominatim()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    global filename

    if request.method == "POST":
        file = request.files['file']
        df = pandas.read_csv(file)
        try:
            df["coordinates"] = df["Address"].apply(geolocator.geocode)
            df["Latitude"] = df["coordinates"].apply(lambda x: x.latitude if x is not None else None)
            df["Longitude"] = df["coordinates"].apply(lambda x: x.longitude if x is not None else None)
            df = df.drop("coordinates", 1)

            filename = datetime.datetime.now().strftime("uploads/%Y-%m-%d-%H-%M-%S-%f" + ".csv")
            df.to_csv(filename, index=None)
            df = df.to_html()
            return render_template("success.html", btn="download.html", tbl=df)
        except:
            return render_template("index.html", text="Please make sure you have an address column<br>")


@app.route("/download")
def download():
    return send_file(filename, attachment_filename="yourfile.csv", as_attachment=True)

if __name__ == "__main__":
    app.debug = True
    app.run()
