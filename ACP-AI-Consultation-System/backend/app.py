from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import openai
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qa_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class QnA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1024))
    answer = db.Column(db.String(1024))
    category = db.Column(db.String(255))

    def __init__(self, question, answer, category=None):
        self.question = question
        self.answer = answer
        self.category = category

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        question = request.form['question']
        category = request.form['category']
        response = get_openai_response(question)
        if response:
            save_qna_to_database(question, response, category)
    return render_template('index.html', response=response)

def get_openai_response(question):
    try:
        # Replace 'your-api-key-here' with the actual key, and use environment variable for production
        openai.api_key = os.getenv("OPENAI_API_KEY")

        init_message = {
            "role": "system",
            "content": "您現在正在與一位精通各宗教的靈性課程講師交談。他能夠根據不同的宗教背景提供靈性指導和解答相關問題。"
        }

        user_message = {"role": "user", "content": question}

        response = openai.ChatCompletion.create(  # pylint: disable=no-member
            model="gpt-3.5-turbo",
            messages=[init_message, user_message]
        )


        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_qna_to_database(question, answer, category):
    try:
        qna_entry = QnA(question=question, answer=answer, category=category)
        db.session.add(qna_entry)
        db.session.commit()
    finally:
        db.session.close()

@app.route('/view-data')
def view_data():
    search_query = request.args.get('search', '')
    qnas = QnA.query.filter(QnA.question.contains(search_query)).all() if search_query else QnA.query.all()
    return render_template('view_data.html', qnas=qnas)

@app.route('/course-video')
def course_video():
    video_url = "https://www.youtube.com/embed/utc_yLx4hoE"
    return render_template('video.html', video_url=video_url)

@app.route('/qa', methods=['GET', 'POST'])
def qa():
    if request.method == 'POST':
        question = request.form['question']
        category = request.form['category']
        response = get_openai_response(question)
        if response:
            save_qna_to_database(question, response, category)
            return render_template('qa.html', response=response)
    return render_template('qa.html')

if __name__ == '__main__':
    app.run(debug=True)
