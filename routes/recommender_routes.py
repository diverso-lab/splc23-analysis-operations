import os
from flask import Blueprint, request, jsonify
from operations.recommender import *

recommender_bp = Blueprint('recommender_bp', __name__,
                           url_prefix='/api/v1/recommendations')

MODEL_FOLDER = './resources/models/'
PRODUCT_FOLDER = './resources/products/'
CONFIGURATION_FOLDER = './resources/configurations/'
FILTER_FOLDER = './resources/filters/'
RECOMMENDER_FOLDER = './resources/recommendations/'


@recommender_bp.route('/', methods=['POST'])
def recommend():

    # Get files
    model = request.files['model']
    products = request.files['products']
    filt = request.files['filter']
    query = request.files['query']

    # Check if files are provided
    if model.filename != '' and products.filename != '' and query.filename != '' and filt.filename != '':

        # Save files
        model.save(os.path.join(MODEL_FOLDER, model.filename))
        products.save(os.path.join(PRODUCT_FOLDER, products.filename))
        filt.save(os.path.join(FILTER_FOLDER, filt.filename))
        query.save(os.path.join(PRODUCT_FOLDER, query.filename))

        # Result
        result = get_recommendations(os.path.join(MODEL_FOLDER, model.filename), os.path.join(
            PRODUCT_FOLDER, products.filename), os.path.join(FILTER_FOLDER, filt.filename), os.path.join(PRODUCT_FOLDER, query.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, products.filename))
        os.remove(os.path.join(FILTER_FOLDER, filt.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, query.filename))

        # Return result
        return jsonify(result)

    # If no file is provided
    else:
        return 'No file uploaded'


@recommender_bp.route('/analysis/restrictiveness', methods=['POST'])
def restrictiveness_route():

    # Get files
    model = request.files['model']
    products = request.files['products']
    filt = request.files['filter']
    features = request.files['features']

    # Check if files are provided
    if model.filename != '' and products.filename != '' and filt.filename != '' and features.filename != '':

        # Save files
        model.save(os.path.join(MODEL_FOLDER, model.filename))
        products.save(os.path.join(PRODUCT_FOLDER, products.filename))
        filt.save(os.path.join(FILTER_FOLDER, filt.filename))
        features.save(os.path.join(PRODUCT_FOLDER, features.filename))

        # Result
        result = get_restrictiveness_of_features(os.path.join(MODEL_FOLDER, model.filename), os.path.join(
            PRODUCT_FOLDER, products.filename), os.path.join(FILTER_FOLDER, filt.filename), os.path.join(PRODUCT_FOLDER, features.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, products.filename))
        os.remove(os.path.join(FILTER_FOLDER, filt.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, features.filename))

        # Return result
        return str(result)

    # If no file is provided
    else:
        return 'No file uploaded'

@recommender_bp.route('/analysis/excluding-restrictiveness', methods=['POST'])
def exclude_restrictiveness_route():

    # Get files
    model = request.files['model']
    products = request.files['products']
    filt = request.files['filter']
    features = request.files['features']

    # Check if files are provided
    if model.filename != '' and products.filename != '' and filt.filename != '' and features.filename != '':

        # Save files
        model.save(os.path.join(MODEL_FOLDER, model.filename))
        products.save(os.path.join(PRODUCT_FOLDER, products.filename))
        filt.save(os.path.join(FILTER_FOLDER, filt.filename))
        features.save(os.path.join(PRODUCT_FOLDER, features.filename))

        # Result
        result = get_reverse_restrictiveness_of_features(os.path.join(MODEL_FOLDER, model.filename), os.path.join(
            PRODUCT_FOLDER, products.filename), os.path.join(FILTER_FOLDER, filt.filename), os.path.join(PRODUCT_FOLDER, features.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, products.filename))
        os.remove(os.path.join(FILTER_FOLDER, filt.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, features.filename))

        # Return result
        return str(result)

    # If no file is provided
    else:
        return 'No file uploaded'


@recommender_bp.route('/analysis/accessibility-table', methods=['POST'])
def accessibility_table_route():

    # Get files
    model = request.files['model']
    products = request.files['products']
    filt = request.files['filter']

    # Check if files are provided
    if model.filename != '' and products.filename != '' and filt.filename != '':

        # Save files
        model.save(os.path.join(MODEL_FOLDER, model.filename))
        products.save(os.path.join(PRODUCT_FOLDER, products.filename))
        filt.save(os.path.join(FILTER_FOLDER, filt.filename))

        # Result
        results, _ = get_accessibility_table_of_products(os.path.join(MODEL_FOLDER, model.filename), os.path.join(
            PRODUCT_FOLDER, products.filename), os.path.join(FILTER_FOLDER, filt.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, products.filename))
        os.remove(os.path.join(FILTER_FOLDER, filt.filename))

        # Return result
        return str(results)

    # If no file is provided
    else:
        return 'No file uploaded'

@recommender_bp.route('/analysis/accessibility', methods=['POST'])
def accessibility_route():

    # Get files
    model = request.files['model']
    products = request.files['products']
    filt = request.files['filter']
    product = request.form.getlist('product')

    # Check if files are provided
    if model.filename != '' and products.filename != '' and filt.filename != '' and len(product) > 0:

        # Save files
        model.save(os.path.join(MODEL_FOLDER, model.filename))
        products.save(os.path.join(PRODUCT_FOLDER, products.filename))
        filt.save(os.path.join(FILTER_FOLDER, filt.filename))

        # Result
        results = get_accessibility_of_products(os.path.join(MODEL_FOLDER, model.filename), os.path.join(
            PRODUCT_FOLDER, products.filename), product[0], os.path.join(FILTER_FOLDER, filt.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, products.filename))
        os.remove(os.path.join(FILTER_FOLDER, filt.filename))

        # Return result
        return str(results)

    # If no file is provided
    else:
        return 'No file uploaded'


@recommender_bp.route('/analysis/catalog', methods=['POST'])
def catalog_coverage_route():
    # Get files
    model = request.files['model']
    products = request.files['products']
    filt = request.files['filter']

    # Check if files are provided
    if model.filename != '' and products.filename != '' and filt.filename != '':

        # Save files
        model.save(os.path.join(MODEL_FOLDER, model.filename))
        products.save(os.path.join(PRODUCT_FOLDER, products.filename))
        filt.save(os.path.join(FILTER_FOLDER, filt.filename))

        # Result
        result = get_product_catalog_coverage(os.path.join(MODEL_FOLDER, model.filename), os.path.join(
            PRODUCT_FOLDER, products.filename), os.path.join(FILTER_FOLDER, filt.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, products.filename))
        os.remove(os.path.join(FILTER_FOLDER, filt.filename))

        # Return result
        return str(result)

    # If no file is provided
    else:
        return 'No file uploaded'


@recommender_bp.route('/analysis/visibility', methods=['POST'])
def visibility_route():
    # Get files
    model = request.files['model']
    products = request.files['products']
    filt = request.files['filter']
    product = request.form.getlist('product')

    # Check if files are provided
    if model.filename != '' and products.filename != '' and filt.filename != '' and len(product) > 0:

        # Save files
        model.save(os.path.join(MODEL_FOLDER, model.filename))
        products.save(os.path.join(PRODUCT_FOLDER, products.filename))
        filt.save(os.path.join(FILTER_FOLDER, filt.filename))

        # Result
        result = get_visibility_of_products(os.path.join(MODEL_FOLDER, model.filename), os.path.join(
            PRODUCT_FOLDER, products.filename), product[0], os.path.join(FILTER_FOLDER, filt.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, products.filename))
        os.remove(os.path.join(FILTER_FOLDER, filt.filename))

        # Return result
        return str(result)

    # If no file is provided
    else:
        return 'No file uploaded'


@recommender_bp.route('/analysis/controversy', methods=['POST'])
def controversy_route():
    # Get files
    model = request.files['model']
    products = request.files['products']
    filt = request.files['filter']
    features = request.files['features']

    # Check if files are provided
    if model.filename != '' and products.filename != '' and filt.filename != '' and features.filename != '':

        # Save files
        model.save(os.path.join(MODEL_FOLDER, model.filename))
        products.save(os.path.join(PRODUCT_FOLDER, products.filename))
        filt.save(os.path.join(FILTER_FOLDER, filt.filename))
        features.save(os.path.join(PRODUCT_FOLDER, features.filename))

        result = get_controversy_of_features(os.path.join(MODEL_FOLDER, model.filename), os.path.join(
            PRODUCT_FOLDER, products.filename), os.path.join(FILTER_FOLDER, filt.filename), os.path.join(PRODUCT_FOLDER, features.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, products.filename))
        os.remove(os.path.join(FILTER_FOLDER, filt.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, features.filename))

        # Return result
        return str(result)
    # If no file is provided
    else:
        return 'No file uploaded'


@recommender_bp.route('/analysis/global-controversy', methods=['POST'])
def global_controversy_route():
    # Get files
    model = request.files['model']
    products = request.files['products']
    filt = request.files['filter']

    # Check if files are provided
    if model.filename != '' and products.filename != '' and filt.filename != '':

        # Save files
        model.save(os.path.join(MODEL_FOLDER, model.filename))
        products.save(os.path.join(PRODUCT_FOLDER, products.filename))
        filt.save(os.path.join(FILTER_FOLDER, filt.filename))

        # Result
        result = get_global_controversy_of_features(os.path.join(MODEL_FOLDER, model.filename), os.path.join(
            PRODUCT_FOLDER, products.filename), os.path.join(FILTER_FOLDER, filt.filename))

        # Remove files
        os.remove(os.path.join(MODEL_FOLDER, model.filename))
        os.remove(os.path.join(PRODUCT_FOLDER, products.filename))
        os.remove(os.path.join(FILTER_FOLDER, filt.filename))

        # Return result
        return str(result)

    # If no file is provided
    else:
        return 'No file uploaded'
