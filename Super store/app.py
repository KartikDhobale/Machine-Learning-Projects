from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained KNN model
with open("knn_regression_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from form
    item_weight = float(request.form["item_weight"])
    item_fat_content = int(request.form["item_fat_content"])
    item_visibility = float(request.form["item_visibility"])
    item_mrp = float(request.form["item_mrp"])

    outlet_size = int(request.form["outlet_size"])
    outlet_location_type = int(request.form["outlet_location_type"])
    outlet_establishment_year = int(request.form["outlet_establishment_year"])

    # One-hot encoded columns from your notebook
    item_type = request.form["item_type"]
    outlet_identifier = request.form["outlet_identifier"]
    outlet_type = request.form["outlet_type"]

    # Create input dataframe
    input_data = pd.DataFrame({
        "Item_Weight": [item_weight],
        "Item_Fat_Content": [item_fat_content],
        "Item_Visibility": [item_visibility],
        "Item_MRP": [item_mrp],
        "Outlet_Establishment_Year": [outlet_establishment_year],
        "Outlet_Size": [outlet_size],
        "Outlet_Location_Type": [outlet_location_type]
    })

    # Add Item_Type dummy columns
    item_type_columns = [
        "Item_Type_Breads",
        "Item_Type_Breakfast",
        "Item_Type_Canned",
        "Item_Type_Dairy",
        "Item_Type_Frozen Foods",
        "Item_Type_Fruits and Vegetables",
        "Item_Type_Hard Drinks",
        "Item_Type_Health and Hygiene",
        "Item_Type_Household",
        "Item_Type_Meat",
        "Item_Type_Others",
        "Item_Type_Seafood",
        "Item_Type_Snack Foods",
        "Item_Type_Soft Drinks",
        "Item_Type_Starchy Foods"
    ]

    for col in item_type_columns:
        input_data[col] = 0

    selected_item_col = "Item_Type_" + item_type

    if selected_item_col in input_data.columns:
        input_data[selected_item_col] = 1

    # Add Outlet Identifier columns
    outlet_columns = [
        "Outlet_Identifier_OUT013",
        "Outlet_Identifier_OUT017",
        "Outlet_Identifier_OUT018",
        "Outlet_Identifier_OUT019",
        "Outlet_Identifier_OUT027",
        "Outlet_Identifier_OUT035",
        "Outlet_Identifier_OUT045",
        "Outlet_Identifier_OUT046",
        "Outlet_Identifier_OUT049"
    ]

    for col in outlet_columns:
        input_data[col] = 0

    selected_outlet = "Outlet_Identifier_" + outlet_identifier

    if selected_outlet in input_data.columns:
        input_data[selected_outlet] = 1

    # Add Outlet Type dummy columns
    outlet_type_columns = [
        "Outlet_Type_Supermarket Type1",
        "Outlet_Type_Supermarket Type2",
        "Outlet_Type_Supermarket Type3"
    ]

    for col in outlet_type_columns:
        input_data[col] = 0

    selected_type = "Outlet_Type_" + outlet_type

    if selected_type in input_data.columns:
        input_data[selected_type] = 1

    # Make sure columns are in EXACT training order
    # This is very important for KNN.
    training_columns = model.feature_names_in_

    input_data = input_data.reindex(
        columns=training_columns,
        fill_value=0
    )

    # Prediction
    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=round(prediction, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)