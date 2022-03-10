from flask import Flask, render_template, abort, request
app = Flask(__name__)

class Place:
    def __init__(self, id, loc, link, lat, lng):
        self.id = id
        self.loc  = loc
        self.link = link
        self.lat  = lat
        self.lng  = lng

buffer = [
    Place('0', 'Kirchhoff Institute for Physics, Germany', 'http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg', 49.4164, 8.67208),
    Place('1', 'Butovo, Moscow, Russia', 'http://camera.butovo.com/mjpg/video.mjpg', 55.5526, 37.5512),
    Place('2', 'Tampere Hacklab, Finland', 'http://tamperehacklab.tunk.org:38001/nphMotionJpeg?Resolution=640x480&Quality=Clarity', 61.4814, 23.7888),
    Place('3', 'Rhein-Taunus-Krematorium, Germany', 'http://webcam.rhein-taunus-krematorium.de/mjpg/video.mjpg', 50.2485, 7.68492),
    Place('4', 'Kaiskuru Skistadion, Norway', 'http://77.222.181.11:8080/mjpg/video.mjpg', 69.9553, 23.3727)
]
curID = 5;

@app.route("/")
def index():
    return render_template('index.html', buffer=buffer)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    global buffer, curID
    act = request.form['act']
    if act == '0':
        loc = request.form['loc']
        link = request.form['link']
        lat = request.form['lat']
        lng = request.form['lng']
        buffer.append(Place(curID, loc, link, lat, lng))
        curID += 1
    elif act == '1':
        id = request.form['id']
        loc = request.form['loc']
        link = request.form['link']
        lat = request.form['lat']
        lng = request.form['lng']
        tmp = Place(id, loc, link, lat, lng)
        i = 0
        while i < len(buffer):
            if buffer[i].id == id:
                buffer[i] = tmp
                break
            i += 1
    else:
        id = request.form['id']
        i = 0
        while i < len(buffer):
            if buffer[i].id == id:
                buffer.remove(buffer[i])
                break
            i += 1

    return render_template('index.html', buffer=buffer)

app.run(debug=True)