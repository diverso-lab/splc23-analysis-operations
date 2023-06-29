import os
import csv

import pandas as pd

from typing import NewType
from flamapy.core.discover import DiscoverMetamodels
from itertools import combinations


def get_recommendations(model, products, filt, query):
    """
    Get the recommendations of a model based on a query and a filter.

    Parameters
    ----------
    model : str
        Path to the model.
    products : str
        Path to the products.
    filt : str
        Path to the filter.
    query : str
        Path to the query.

    Returns
    -------
    list
        List of recommended products.
    """
    query_df = pd.read_csv(query, header=None)
    filt_df = pd.read_csv(filt, header=None)
    products_df = pd.read_csv(products, header=None)

    restrictions = []
    for index, row in filt_df.iterrows():
        for index2, row2 in query_df.iterrows():
            values = row2.values.tolist()
            if row2[0] == row[0] and row2[1] == row[1]:
                restrictions.append(row[2])

    products = {}
    is_valid = True
    for index, row in products_df.iterrows():
        for restriction in restrictions:
            values = row.values.tolist()
            if "!=" not in restriction and restriction not in values:
                is_valid = False
            elif "!=" in restriction and restriction.replace("!", "") in values:
                is_valid = False
        if is_valid:
            products.update({row[0]: row[7]})
        is_valid = True

    return sorted(products, key=products.get, reverse=True)


def get_restrictiveness_of_features(model, products, filt, query):
    """
    Get the restrictiveness of a query based on a filter.

    Parameters
    ----------
    model : str
        Path to the model.
    products : str
        Path to the products.
    filt : str
        Path to the filter.
    query : str
        Path to the query.

    Returns
    -------
    float
        Restrictiveness of the query.
    """
    products_df = pd.read_csv(products, header=None)
    product_list = get_recommendations(model, products, filt, query)

    return len(product_list) / len(products_df)


def get_reverse_restrictiveness_of_features(model, products, filt, query):
    """
    Get the reverse restrictiveness of a query based on a filter.

    Parameters
    ----------
    model : str
        Path to the model.
    products : str
        Path to the products.
    filt : str
        Path to the filter.
    query : str
        Path to the query.

    Returns
    -------
    float
        Reverse restrictiveness of the query.
    """
    query_df = pd.read_csv(query, header=None)
    filt_df = pd.read_csv(filt, header=None)
    products_df = pd.read_csv(products, header=None)

    restrictions = []
    for index, row in filt_df.iterrows():
        for index2, row2 in query_df.iterrows():
            values = row2.values.tolist()
            if row2[0] == row[0] and row2[1] == row[1]:
                restrictions.append(row[2])

    restrictions = list(set(restrictions))

    products = []
    is_valid = True
    for index, row in products_df.iterrows():
        for restriction in restrictions:
            values = row.values.tolist()
            if "!=" not in restriction and restriction in values:
                is_valid = False
            elif "!=" in restriction and restriction.replace("!", "") not in values:
                is_valid = False
        if is_valid:
            products.append(row[0])
        is_valid = True

    return len(products) / len(products_df)


def get_accessibility_table_of_products(model, products, filt):
    """
    Get the accessibility table of a model based on a filter.

    Parameters
    ----------
    model : str
        Path to the model.
    products : str
        Path to the products.
    filt : str
        Path to the filter.

    Returns
    -------
    dict
        Dictionary with the accessibility table of the model.
    """
    dm = DiscoverMetamodels()

    fm = dm.use_transformation_t2m(model, "fm")
    features = [feature.name for feature in fm.get_features() if feature.is_leaf()]

    combinations_list = []
    for i in range(1, len(features) + 1):
        combinations_list += list(combinations(features, i))

    dict_counter = {}
    valid_recommendations = 0
    for combination in combinations_list:
        with open("resources/recommender/test.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for feature in combination:
                writer.writerow([feature, True])

        recommendations = get_recommendations(
            model, products, filt, "resources/recommender/test.csv"
        )
        if len(recommendations) > 0:
            valid_recommendations += 1
            for value in recommendations:
                if value in dict_counter:
                    dict_counter[value] += 1
                else:
                    dict_counter[value] = 1

    os.remove("resources/recommender/test.csv")
    dict_counter = {
        k: v for k, v in sorted(dict_counter.items(), key=lambda item: item[0])
    }
    return dict_counter, valid_recommendations


def get_accessibility_of_products(model, products, product, filt):
    """
    Get the accessibility of a product based on a filter.

    Parameters
    ----------
    model : str
        Path to the model.
    products : str
        Path to the products.
    product : str
        Product to get the accessibility.
    filt : str
        Path to the filter.

    Returns
    -------
    float
        Accessibility of the product.
    """
    dict_counter, total = get_accessibility_table_of_products(model, products, filt)

    product = "product=" + product
    return dict_counter[product] / total


def get_product_catalog_coverage(model, products, filt):
    """
    Get the product catalog coverage of a model based on a filter.

    Parameters
    ----------
    model : str
        Path to the model.
    products : str
        Path to the products.
    filt : str
        Path to the filter.

    Returns
    -------
    float
        Product catalog coverage of the model.
    """
    catalog_coverage = get_accessibility_table_of_products(model, products, filt)

    recommended = 0
    for key, value in catalog_coverage[0].items():
        if value > 0:
            recommended += 1

    return recommended / len(catalog_coverage[0])


def get_visibility_of_products(model, products, product, filt):
    """
    Get the visibility of a product based on a filter.

    Parameters
    ----------
    model : str
        Path to the model.
    products : str
        Path to the products.
    product : str
        Product to get the visibility.
    filt : str
        Path to the filter.

    Returns
    -------
    float
        Visibility of the product.
    """
    dm = DiscoverMetamodels()

    fm = dm.use_transformation_t2m(model, "fm")
    features = [feature.name for feature in fm.get_features() if feature.is_leaf()]

    combinations_list = []
    for i in range(1, len(features) + 1):
        combinations_list += list(combinations(features, i))

    appearances = []
    for combination in combinations_list:
        with open("resources/recommender/test.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for feature in combination:
                writer.writerow([feature, True])

        recommendations = get_recommendations(
            model, products, filt, "resources/recommender/test.csv"
        )
        if len(recommendations) > 0 and "product=" + product in recommendations:
            appearances.append(recommendations)

    os.remove("resources/recommender/test.csv")

    index = 0
    total = 0
    for appearance in appearances:
        index += appearance.index("product=" + product) + 1
        total += len(appearance)

    return 1 - (index / total)


def get_controversy_of_features(model, products, filt, query):
    """
    Get the controversy of a list of features based on a filter.

    Parameters
    ----------
    model : str
        Path to the model.
    products : str
        Path to the products.
    filt : str
        Path to the filter.
    query : str
        Query to get the controversy.

    Returns
    -------
    float
        Controversy of the list of features.
    """
    dm = DiscoverMetamodels()

    fm = dm.use_transformation_t2m(model, "fm")
    features = [feature.name for feature in fm.get_features() if feature.is_leaf()]

    combinations_list = []
    for i in range(1, len(features) + 1):
        combinations_list += list(combinations(features, i))


    controversial_queries = []
    for combination in combinations_list:
        with open("resources/recommender/test.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for feature in combination:
                writer.writerow([feature, True])

        recommendations = get_recommendations(
            model, products, filt, "resources/recommender/test.csv"
        )
        if len(recommendations) <= 0:
            controversial_queries.append(combination)

    os.remove("resources/recommender/test.csv")

    feature_list = []
    query_df = pd.read_csv(query, header=None)
    print(query_df)
    for index, row in query_df.iterrows():
        if row[1] == True:
            feature_list.append(row[0])

    print(feature_list)
    count = 0
    for query in controversial_queries:
        if set(feature_list).issubset(query):
            count += 1

    return count / len(controversial_queries)


def get_global_controversy_of_features(model, products, filt):
    """
    Get the global controversy of a model based on a filter.

    Parameters
    ----------
    model : str
        Path to the model.
    products : str
        Path to the products.
    filt : str
        Path to the filter.

    Returns
    -------
    float
        Global controversy of the model.
    """
    dm = DiscoverMetamodels()

    fm = dm.use_transformation_t2m(model, "fm")
    features = [feature.name for feature in fm.get_features() if feature.is_leaf()]

    combinations_list = []
    for i in range(1, len(features) + 1):
        combinations_list += list(combinations(features, i))

    controversial_queries = []
    for combination in combinations_list:
        with open("resources/recommender/test.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for feature in combination:
                writer.writerow([feature, True])

        recommendations = get_recommendations(
            model, products, filt, "resources/recommender/test.csv"
        )
        if len(recommendations) <= 0:
            controversial_queries.append(combination)

    os.remove("resources/recommender/test.csv")

    return len(controversial_queries) / len(combinations_list)
