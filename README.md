**OpenFoodFacts Lakehouse**

This is a lakehouse built and hosted on **Databricks** which contains processed, open-source data of the world's largest food product database, openfoodfacts.org. The data is **updated daily at 12:00 am EEST (GMT +3)**, and is stored in AWS S3 and is **accessible to everyone** who wishes to use the data via Databricks Delta Share and the config.share file attached above. Attached is also **python** file containing a **simple example script** on how to access the tables of the lakehouse locally using **PySpark** (**pandas** can also be used)

This dataset will be useful to data analysts, data scientists and AI/ML engineers who wish to work with clean and structured data about various grocery products from all around the world, such as their country of origin, ingredients, images of the product for AI training, nutrition data, micronutrient contents, etc.

This data is open-source and may be used by anyone for any purpose, however please credit this repository as your source

Here is the data catalog for all 3 tables, with all the information you will need:

**1. gold.dim_brands**
- Purpose: Stores standardized information about product brands and brand ownership
- **Columns:**

| Column Name   | Data Type | Description                                             |
| ------------- | --------- | ------------------------------------------------------- |
| `brand_id`    | int       | Unique identifier of the brand.                         |
| `brands_list` | string    | List or name of brands associated with a product entry. |
| `brand_owner` | string    | Company or organization that owns the brand.            |

**2. gold.dim_products**
- Purpose: Contains detailed information about food products from OpenFoodFacts, including packaging, ingredients, nutritional values, environmental metrics, classifications, and product media links.
- **Columns:**

| Column Name                 | Data Type | Description                                                                  |
| --------------------------- | --------- | ---------------------------------------------------------------------------- |
| `product_id`                | string    | Unique identifier of the product (typically barcode or product code).        |
| `product_page_url`          | string    | URL of the product page in OpenFoodFacts.                                    |
| `product_name`              | string    | Name of the product.                                                         |
| `packaging_type`            | string    | Type of product packaging (e.g., bottle, box, can).                          |
| `packaging_details`         | string    | Detailed information about packaging materials or characteristics.           |
| `manufacturing_locations`   | string    | Locations where the product is manufactured.                                 |
| `purchasing_locations`      | string    | Locations where the product is available for purchase.                       |
| `countries`                 | string    | Countries where the product is distributed or sold.                          |
| `ingridients_description`   | string    | Textual description of the product ingredients.                              |
| `allergens`                 | string    | Allergens contained in the product.                                          |
| `serving_quantity`          | double    | Quantity of a single serving of the product.                                 |
| `nova_group`                | int       | NOVA food classification group representing the level of food processing.    |
| `pnns_groups_2`             | string    | Secondary food category classification according to PNNS nutritional groups. |
| `environmental_score_score` | int       | Numerical environmental impact score of the product.                         |
| `environmental_score_grade` | string    | Letter-based environmental impact grade of the product.                      |
| `product_weight`            | double    | Total weight of the product.                                                 |
| `unique_scan_count`         | int       | Number of unique scans or recorded interactions for the product.             |
| `product_image_url`         | string    | URL of the main product image.                                               |
| `image_ingredients_url`     | string    | URL of the product ingredients image.                                        |
| `image_nutrition_data_url`  | string    | URL of the nutrition facts image.                                            |
| `energy_kj_100g`            | double    | Energy content in kilojoules per 100g.                                       |
| `energy_kcal_100g`          | double    | Energy content in kilocalories per 100g.                                     |
| `fat_100g`                  | double    | Total fat content per 100g.                                                  |
| `saturated_fat_100g`        | double    | Saturated fat content per 100g.                                              |
| `cholesterol_100g`          | double    | Cholesterol content per 100g.                                                |
| `carbohydrates_100g`        | double    | Carbohydrate content per 100g.                                               |
| `sugars_100g`               | double    | Sugar content per 100g.                                                      |
| `lactose_100g`              | double    | Lactose content per 100g.                                                    |
| `starch_100g`               | double    | Starch content per 100g.                                                     |
| `fiber_100g`                | double    | Dietary fiber content per 100g.                                              |
| `proteins_100g`             | double    | Protein content per 100g.                                                    |
| `salt_100g`                 | double    | Salt content per 100g.                                                       |
| `sodium_100g`               | double    | Sodium content per 100g.                                                     |
| `alcohol_100g`              | double    | Alcohol content per 100g.                                                    |
| `vitamin_a_100g`            | double    | Vitamin A content per 100g.                                                  |
| `vitamin_d_100g`            | double    | Vitamin D content per 100g.                                                  |
| `vitamin_e_100g`            | double    | Vitamin E content per 100g.                                                  |
| `vitamin_k_100g`            | double    | Vitamin K content per 100g.                                                  |
| `vitamin_c_100g`            | double    | Vitamin C content per 100g.                                                  |
| `vitamin_b1_100g`           | double    | Vitamin B1 content per 100g.                                                 |
| `vitamin_b2_100g`           | double    | Vitamin B2 content per 100g.                                                 |
| `vitamin_b6_100g`           | double    | Vitamin B6 content per 100g.                                                 |
| `vitamin_b9_100g`           | double    | Vitamin B9 (folate) content per 100g.                                        |
| `vitamin_b12_100g`          | double    | Vitamin B12 content per 100g.                                                |
| `potassium_100g`            | double    | Potassium content per 100g.                                                  |
| `calcium_100g`              | double    | Calcium content per 100g.                                                    |
| `phosphorus_100g`           | double    | Phosphorus content per 100g.                                                 |
| `iron_100g`                 | double    | Iron content per 100g.                                                       |
| `magnesium_100g`            | double    | Magnesium content per 100g.                                                  |
| `zinc_100g`                 | double    | Zinc content per 100g.                                                       |
| `copper_100g`               | double    | Copper content per 100g.                                                     |
| `iodine_100g`               | double    | Iodine content per 100g.                                                     |
| `caffeine_100g`             | double    | Caffeine content per 100g.                                                   |
| `carbon_footprint_100g`     | double    | Estimated carbon footprint of the product per 100g.                          |

**3. gold.fact_product_entries**
- Purpose: Stores metadata about product entries in OpenFoodFacts, including creators, completeness, timestamps, and relationships to products and brands. Used for tracking product creation and update history.
- **Columns:**

| Column Name                       | Data Type | Description                                                                     |
| --------------------------------- | --------- | ------------------------------------------------------------------------------- |
| `entry_id`                        | int       | Unique identifier of the product entry.                                         |
| `product_id`                      | string    | Identifier of the related product. Used to link to the product dimension table. |
| `brand_id`                        | int       | Identifier of the related brand. Used to link to the brand dimension table.     |
| `entry_creator`                   | string    | Username or identifier of the user who created the product entry.               |
| `product_data_completeness`       | string    | Indicator of how complete the product information is.                           |
| `product_creation_datetime`       | timestamp | Date and time when the product entry was originally created.                    |
| `last_user_modification_datetime` | timestamp | Date and time of the latest modification made by a user.                        |
| `last_system_update_datetime`     | timestamp | Date and time when the system last updated the entry.                           |
| `last_product_image_datetime`     | timestamp | Date and time when the latest product image was uploaded or updated.            |
