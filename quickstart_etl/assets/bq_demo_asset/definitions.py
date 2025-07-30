# from dagster import (
#     AssetSelection,
#     Definitions,
#     ScheduleDefinition,
#     define_asset_job,
#     load_assets_from_modules,
# )
# from dagster_gcp import BigQueryResource
#
# from . import assets
# # import binascii
# # import base64
# import json
# import os
#
# service_account_info = os.getenv("BQ_CRED")
# # service_account_info = json.loads(bq_cred_b64)
#
# bq_demo_assets = load_assets_from_modules([assets])
#
# # Define a job that targets only the assets in the "bigquery_demo" group
# bq_demo_job = define_asset_job(
#     name="bq_demo_job", selection=AssetSelection.groups("bigquery_demo")
# )
#
# # Define a schedule for the job
# bq_demo_schedule = ScheduleDefinition(
#     job=bq_demo_job, cron_schedule="0 4 * * *", execution_timezone="UTC"
# )
#
# # Create a Definitions object that bundles all components of this pipeline.
# defs = Definitions(
#     assets=bq_demo_assets,
#     jobs=[bq_demo_job],
#     schedules=[bq_demo_schedule],
#     resources={
#         # 2. This is where the resource is actually configured.
#         # We pass the loaded JSON credentials directly to the resource.
#         "bigquery": BigQueryResource(
#             project="athen-340910",
#             gcp_credentials=service_account_info
#         )
#     },
# )


from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)

from . import assets

# Load all asset definitions from the `assets.py` file in this folder
hoaipham_test_assets = load_assets_from_modules([assets])

# Define a job that targets only the assets in the "hoaipham_test" group
hoaipham_test_job = define_asset_job(
    name="hoaipham_test_job2", selection=AssetSelection.groups("hoaipham_test2")
)

# Define a schedule for the job
hoaipham_test_schedule = ScheduleDefinition(
    job=hoaipham_test_job, cron_schedule="0 7 * * *", execution_timezone="UTC"
)

# Create a Definitions object that bundles all components of this pipeline.
# Dagster will discover and load this object.
defs = Definitions(
    assets=hoaipham_test_assets,
    jobs=[hoaipham_test_job],
    schedules=[hoaipham_test_schedule],
)