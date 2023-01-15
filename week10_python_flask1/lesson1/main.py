from flask import Flask,render_template
import markdown

app = Flask(__name__)

@app.route("/exercices")
def exercices():
    with open('templates/exercices.md', 'r') as f:
        markdown_text = f.read()
    html = markdown.markdown(markdown_text)
    return html

@app.route("/lesson")
def lesson():
    with open('templates/in-this-chapter.md', 'r') as f:
        markdown_text = f.read()
    html = markdown.markdown(markdown_text)
    return html

if __name__ == "__main__":
    app.run()