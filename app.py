from flask import Flask, request, render_template
import requests
app = Flask(__name__)
# Endpoint of the model running in Google Colab (ngrok URL)
colab_model_url = "https://6687-35-227-171-114.ngrok-free.app/generate"  # Replace with your actual Ngrok URL
def get_model_response(user_msg):
    data = {"prompt": user_msg}
    response = requests.post(colab_model_url, json=data)
    if response.status_code == 200:
        return response.json().get('response', 'No response key in JSON')
    else:
        return "Error communicating with the model."
@app.route('/')
def input():
    return render_template('input.html')
@app.route('/subjective_output', methods=['POST'])
def subjective_output():
    subjective_question = request.form['subjective_question']
    response = get_model_response("1"+subjective_question)
    return render_template('output_subjective.html', subjective_question=subjective_question, response=response)
@app.route('/objective_output', methods=['POST'])
def objective_output():
    objective_question = request.form['objective_question']
    choice_a = request.form['choice_a']
    choice_b = request.form['choice_b']
    choice_c = request.form['choice_c']
    choice_d = request.form['choice_d']
    response = get_model_response("2"+objective_question +"||||"+ choice_a +"||||" +choice_b +"||||"+choice_c +"||||"+choice_d +"||||")
    return render_template('output_objective.html', objective_question=objective_question, choice_a=choice_a, choice_b=choice_b, choice_c=choice_c, choice_d=choice_d, response=response)
if __name__ == '__main__':
    app.run(debug=True)
