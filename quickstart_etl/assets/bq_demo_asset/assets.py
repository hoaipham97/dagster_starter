# import os
# import pandas as pd
# from dagster import AssetExecutionContext, MaterializeResult, MetadataValue, asset
# from dagster_gcp import BigQueryResource
#
# # This variable was missing. You must define which BigQuery dataset to use.
# # Replace 'your_dataset_name' with your actual dataset.
# BQ_DATASET = "athen_wiki"
#
# @asset(group_name="bigquery_demo", compute_kind="bigquery")
# def source_table_a(
#     context: AssetExecutionContext,
#     # Dagster injects the resource configured in __init__.py here
#     bigquery: BigQueryResource
# ) -> pd.DataFrame:
#     """Reads data from table_a in BigQuery."""
#
#     table_name = "athen_wiki_data"
#     query = f"SELECT * FROM `{bigquery.project}.{BQ_DATASET}.{table_name}`"
#     context.log.info(f"Executing query: {query}")
#
#     with bigquery.get_client() as client:
#         df = client.query(query).to_dataframe()
#
#     context.log.info(f"Read {len(df)} rows from {table_name}.")
#     return df
#
#
# @asset(group_name="bigquery_demo", compute_kind="bigquery")
# def destination_table_b(
#     context: AssetExecutionContext,
#     source_table_a: pd.DataFrame,
#     bigquery: BigQueryResource,
# ) -> MaterializeResult:
#     """Transforms data and loads it into table_b in BigQuery."""
#
#     transformed_df = source_table_a.copy()
#     transformed_df["processed_by"] = "dagster"
#
#     table_name = "dagster_sample_wiki"
#     table_id = f"{bigquery.project}.{BQ_DATASET}.{table_name}"
#     context.log.info(f"Loading {len(transformed_df)} rows into table '{table_id}'.")
#
#     with bigquery.get_client() as client:
#         job = client.load_table_from_dataframe(
#             dataframe=transformed_df,
#             destination=table_id,
#         )
#         job.result()
#
#     return MaterializeResult(
#         metadata={
#             "num_rows": len(transformed_df),
#             "table_id": table_id,
#             "preview": MetadataValue.md(transformed_df.head().to_markdown()),
#         }
#     )

from dagster import AssetExecutionContext, asset

@asset(group_name="hoaipham_test2", compute_kind="hoaipham_test Dagster")
def test1(context: AssetExecutionContext) -> None:
  """A simple asset that prints a message."""
  print("ahihi")


@asset(deps=[test1], group_name="hoaipham_test2", compute_kind="hoaipham_test Dagster")
def test2(context: AssetExecutionContext) -> int:
    """A simple asset that depends on test1 and returns a value."""
    print("test2_hihi")
    result = 1 + 3
    context.log.info(f"Result is {result}")
    return result
