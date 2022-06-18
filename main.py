from app import app, db
from app.models import Article
from flask import request, url_for, render_template, redirect
import random

@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        all_articles = Article.query.all()
        count = len(all_articles)
        return render_template('index.html', all_articles=all_articles, count=count)
    

@app.route("/create/", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        if 'title' in request.form:
            title = request.form['title']
            title = title.capitalize()
            body = request.form['body']
            if title and body:
                new_article = Article(title=title, body=body)
                db.session.add(new_article)
                db.session.flush()
                post_uri = abs(hash(str(new_article.id)))
                new_article.post_uri = post_uri
                db.session.commit()
                return redirect("/")
            else:
                if not title:
                    return render_template('create.html', error = "Input valid title", title = title, body = body)
                elif not body:
                    return render_template('create.html', error = "Input valid content", title = title, body = body)
                else:
                    return render_template('create.html', error = "Something went wrong :(", title = title, body = body)
    else:
        return render_template('create.html')

@app.route("/article/<post_uri>/", methods=['GET'])
def get_article(post_uri):
    if request.method == 'GET':
        article = Article.query.filter_by(post_uri=post_uri)
        count = article.count()
        return render_template('single_article.html', article=article, count=count)


@app.route("/search/", methods=['GET', 'POST'])
def search_articles():
    if request.method == 'GET':
        return render_template('search.html')
    if request.method == 'POST':
        if 'term' in request.form:
            term = request.form['term']
            url = '/search/' + term + '/'
            return redirect(url)


@app.route("/search/<term>/", methods=['GET', 'POST'])
def search_article(term):
    if request.method == 'GET':
        articles = Article.query.filter(Article.title.contains(term))
        count = articles.count()
        return render_template('searched_articles.html', articles=articles, term=term, count=count)
        
    

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
