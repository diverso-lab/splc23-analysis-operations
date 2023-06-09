## Endpoints Documentation

Before trying each operation, ensure that you have selected the appropriate server in the Swagger UI's servers dropdown. If you are executing the deployed API, select the Render server. If you have locally installed the API, choose the local server. 

To test each operation, simply click on the endpoint and click the "Try out" button, which allows file upload.

### Validate Recommendations

Endpoint: `/api/v1/recommendations/validate`

This endpoint checks the validity of items based on the feature model, product assortment, and a query over the product assortment and feature model.

**Parameters:**
- `feature_model` (file): The feature model file.
- `product_assortment` (file): The product assortment file.
- `query` (string): The query to be performed on the product assortment and feature model.

### Get Recommendations

Endpoint: `/api/v1/recommendations/`

This endpoint returns recommendations based on the feature model, product assortment, and a query over the product assortment and feature model. 

**Parameters:**
- `feature_model` (file): The feature model file.
- `product_assortment` (file): The product assortment file.
- `query` (string): The query to be performed on the product assortment and feature model.

Based on our experimentation, for the provided artifacts and Query R1, the expected result is a list of `p1`, `p3`, and `p6` in that specific order.

### Compute Restrictiveness

Endpoint: `/api/v1/recommendations/analysis/restrictiveness`

This operation computes the restrictiveness of a feature list (or unique feature). Provide the feature model, product assortment, and the name of the feature in the `features` field.

**Parameters:**
- `feature_model` (file): The feature model file.
- `product_assortment` (file): The product assortment file.
- `features` (string or array of strings): The name(s) of the feature(s) to compute restrictiveness.

In our experimentation, for the feature "sports", we obtained a result of 0.375 or 37.5%. For feature sets, you can add multiple features using the "Add string item" button. In our experimentation, for feature sets "sports" and "exchangelens", we obtained a result of 25%.

### Compute Excluding Restrictiveness

Endpoint: `/api/v1/recommendations/analysis/excluding-restrictiveness`

This operation computes the excluding restrictiveness of a set of features. Provide the feature model, product assortment, and the set of features in the `features` field.

**Parameters:**
- `feature_model` (file): The feature model file.
- `product_assortment` (file): The product assortment file.
- `features` (string or array of strings): The name(s) of the feature(s) to compute excluding restrictiveness.

In our experimentation, for feature set "sports" and "exchangelens", we obtained a result of 50%.
