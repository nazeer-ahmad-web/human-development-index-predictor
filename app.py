from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained machine learning model
# Make sure your model file ('hdi_model.pkl') is placed in the same directory as app.py
try:
    with open('hdi_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    # Fallback placeholder if the model file isn't generated yet
    model = None
    print("Warning: 'hdi_model.pkl' not found. Please place your trained model file here.")

@app.route('/')
def dashboard():
    """Renders the main HDI Monitor dashboard with the prediction form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Processes form submission, matches feature ordering, and delivers structured outputs."""
    if request.method == 'POST':
        try:
            # 1. Extract values cleanly from form requests
            life_expectancy = float(request.form['life_expectancy'])
            expected_schooling = float(request.form['expected_schooling'])
            mean_schooling = float(request.form['mean_schooling'])
            gni = float(request.form['gni'])

            # 2. Strict feature matrix alignment matching your model training structure:
            # ["Life expectancy at birth YEARS", "Expected years of schooling YEARS", 
            #  "Mean years of schooling YEARS", "Gross national income (GNI) per capita USD"]
            features = np.array([[life_expectancy, expected_schooling, mean_schooling, gni]])
            
            # 3. Model Prediction execution with safety fallback check
            if model:
                prediction_array = model.predict(features)
                # Format to 3 decimal places typical of standard UN HDI outputs
                result = round(float(prediction_array[0]), 3)
            else:
                # Mock math calculation fallback if your .pkl isn't present yet
                result = round(0.005 * life_expectancy + 0.01 * expected_schooling + 0.015 * mean_schooling + 0.000005 * gni, 3)

            # 4. Package inputs tightly into a dictionary structure matching your result.html template expectations
            inputs = {
                "life_expectancy": life_expectancy,
                "expected_schooling": expected_schooling,
                "mean_schooling": mean_schooling,
                "gni": f"{gni:,.2f}" if gni >= 1000 else gni # Adds nice comma spacing format to currency values
            }

            # 5. Hand everything over cleanly to the layout view
            return render_template(
                "result.html",
                prediction=result,
                inputs=inputs
            )
            
        except Exception as e:
            return f"An error occurred during calculation processing: {str(e)}", 400

if __name__ == '__main__':
    # Runs the server locally at http://127.0.0.1:5000
    app.run(debug=True)