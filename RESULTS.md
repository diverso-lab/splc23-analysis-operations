## Endpoints Documentation

Before trying each operation, ensure that you have selected the appropriate server in the Swagger UI's servers dropdown. If you are executing the deployed API, select the Render server. If you have locally installed the API, choose the local server. 

To test each operation, simply click on the endpoint and click the "Try out" button, which allows file upload.

### Get Recommendations

Endpoint: `/api/v1/recommendations/`

This endpoint returns recommendations based on the feature model, product assortment, and a query over the product assortment and feature model. 

**Parameters:**
- `feature_model` (file): The feature model file.
- `product_assortment` (file): The product assortment file.
- `filter` (file): The filt file.
- `query` (string): The query to be performed on the product assortment and feature model.

Based on our experimentation, for the provided artifacts and Query R1, the expected result is a list of `p1`, `p3`, and `p6` in that specific order.

### Compute Restrictiveness

Endpoint: `/api/v1/recommendations/analysis/restrictiveness`

This operation computes the restrictiveness of a feature list (or unique feature). Provide the feature model, product assortment, and the name of the feature in the `features` field.

**Parameters:**
- `feature_model` (file): The feature model file.
- `product_assortment` (file): The product assortment file.
- `filter` (file): The filt file.
- `features` (string or array of strings): The name(s) of the feature(s) to compute restrictiveness.

In our experimentation, for the feature "sports", we obtained a result of 0.375 or 37.5%. For feature sets, you can add multiple features using the "Add string item" button. In our experimentation, for feature sets "sports" and "exchangelens", we obtained a result of 37.5%.

### Compute Excluding Restrictiveness

Endpoint: `/api/v1/recommendations/analysis/excluding-restrictiveness`

This operation computes the excluding restrictiveness of a set of features. Provide the feature model, product assortment, and the set of features in the `features` field.

**Parameters:**
- `feature_model` (file): The feature model file.
- `product_assortment` (file): The product assortment file.
- `filter` (file): The filt file.
- `features` (string or array of strings): The name(s) of the feature(s) to compute excluding restrictiveness.

In our experimentation, for feature set "sports" and "exchangelens", we obtained a result of 50%.

### Compute Accessibility Table

Endpoint: `/api/v1/recommendations/analysis/accessibility-table`

This endpoint computes the table shown as "Table 2: Product Occurrences in Recommendations" based on the provided artifacts.

**Parameters:**
- `feature_model` (file): The feature model file.
- `product_assortment` (file): The product assortment file.

Based on our experimentation with the provided artifacts, the expected result should be a table with the following data:

| pid | 𝑝1 | 𝑝2 | 𝑝3 | 𝑝4 | 𝑝5 | 𝑝6 | 𝑝7 | 𝑝8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| #occurrences | 31 | 7 | 15 | 31 | 3 | 15 | 3 | 15 |

### Compute Accessibility

Endpoint: `/api/v1/recommendations/analysis/accessibility`

This operation computes the accessibility of a product based on the provided feature model and product assortment.

**Parameters:**
- `feature_model` (file): The feature model file.
- `product_assortment` (file): The product assortment file.
- `filter` (file): The filt file.
- `product_name` (string): The name of the product to compute accessibility.

In our experimentation, for product `p6`, we obtained an accessibility result of 31.91%. Similarly, for product `p7`, the accessibility result was 6.38%.

### Compute Catalog Coverage

Endpoint: `/api/v1/recommendations/analysis/catalog`

This operation computes the product catalog coverage for a given feature model and its associated product assortment.

**Parameters:**
- `feature_model` (file): The feature model file.
- `product_assortment` (file): The product assortment file.
- `filter` (file): The filt file.

In our experimentation, we obtained a catalog coverage of 100%, indicating that every product in the catalog is being recommended at least once.

### Compute Visibility

Endpoint: `/api/v1/recommendations/analysis/visibility`

This operation computes the visibility of a product based on the provided feature model, product assortment, and the name of the product.

**Parameters:**
- `feature_model` (file): The feature model file.
- `product_assortment` (file): The product assortment file.
- `filter` (file): The filt file.
- `product_name` (string): The name of the product to compute visibility.

In our experimentation, the visibility of product `p5` is calculated to be 16.66% (rounded up to 16.7% in the paper).

### Compute Controversy

Endpoint: `/api/v1/recommendations/analysis/controversy`

This operation computes the controversy of a feature or a set of features based on the provided feature model, product assortment, and the name(s) of the feature(s).

**Parameters:**
- `feature_model` (file): The feature model file.
- `product_assortment` (file): The product assortment file.
- `filter` (file): The filt file.
- `features` (string or array of strings): The name(s) of the feature(s) to compute controversy.

In our experimentation, for feature "waterproof", we obtained a controversy result of 50.0%.

### Compute Global Controversy

Endpoint: `/api/v1/recommendations/analysis/global-controversy`

This operation computes the global controversy of all features based on the provided feature model and product assortment.

**Parameters:**
- `feature_model` (file): The feature model file.
- `filter` (file): The filt file.
- `product_assortment` (file): The product assortment file.

In our experimentation, we obtained a global controversy result of 25.39%.
