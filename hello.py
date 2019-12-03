import io
from flask import Flask
from flask import render_template
from flask import Response
from graph import create_figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html', name='Channing!')


@app.route('/plot.png')
def plot():
    fig = create_figure()

    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/graph')
def graph():
    return render_template("hello.html", Test="Yo !")


if __name__ == '__main__':
    app.run(debug=True)
