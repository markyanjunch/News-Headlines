import requests as requests
from flask import Flask, render_template
from secrets import api_key

app = Flask(__name__)


def get_top5_stories():
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params = {'api-key': api_key}
    results = requests.get(base_url, params).json()['results']
    return results[:5]


@app.route('/')
def welcome():
    return '<h1>Welcome!</h1>'


@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name=nm)


@app.route('/headlines/<nm>')
def show_headlines(nm):
    articles = get_top5_stories()
    headlines = [a['title'] for a in articles]
    return render_template('headlines.html',
                           name=nm,
                           headlines=headlines)


@app.route('/links/<nm>')
def show_links(nm):
    articles = get_top5_stories()
    headlines = [a['title'] for a in articles]
    links = [a['url'] for a in articles]
    return render_template('links.html',
                           name=nm,
                           headlines=headlines,
                           links=links)


@app.route('/images/<nm>')
def show_images(nm):
    articles = get_top5_stories()
    headlines = [a['title'] for a in articles]
    links = [a['url'] for a in articles]
    images = [a['multimedia'][0]['url'] for a in articles]
    return render_template('table.html',
                           name=nm,
                           headlines=headlines,
                           links=links,
                           images=images)


if __name__ == '__main__':
    app.run()
