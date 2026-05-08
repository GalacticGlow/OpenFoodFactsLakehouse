**OpenFoodFacts Lakehouse**

This is a lakehouse built and hosted on **Databricks** which contains processed, open-source data of the world's largest food product database, openfoodfacts.org. The data is **updated daily at 12:00 am EEST (GMT +3)**, and is stored in AWS S3 and is **accessible to everyone** who wishes to use the data via Databricks Delta Share and the config.share file attached above. Attached is also **python** file containing a **simple example script** on how to access the tables of the lakehouse locally using **PySpark** (**pandas** can also be used)

This dataset will be useful to data analysts, data scientists and AI/ML engineers who wish to work with clean and structured data about various grocery products from all around the world, such as their country of origin, ingredients, images of the product for AI training, nutrition data, micronutrient contents, etc.

