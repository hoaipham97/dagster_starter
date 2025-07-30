from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)
from dagster_gcp import BigQueryResource

from . import assets
import base64
import json
import os

# with open('cred.json') as f:
#     service_account_info = json.load(f)

bq_cred_b64 = os.getenv("BQ_CRED")
if not bq_cred_b64:
    raise ValueError(
        "The BQ_CRED environment variable must be set with the base64 encoded service account key."
    )

# Decode the base64 string, then parse the resulting JSON string into a dictionary.
service_account_json_str = base64.b64decode(bq_cred_b64).decode("utf-8")
service_account_info = json.loads(service_account_json_str)

bq_demo_assets = load_assets_from_modules([assets])

# Define a job that targets only the assets in the "bigquery_demo" group
bq_demo_job = define_asset_job(
    name="bq_demo_job", selection=AssetSelection.groups("bigquery_demo")
)

# Define a schedule for the job
bq_demo_schedule = ScheduleDefinition(
    job=bq_demo_job, cron_schedule="0 4 * * *", execution_timezone="UTC"
)

# Create a Definitions object that bundles all components of this pipeline.
defs = Definitions(
    assets=bq_demo_assets,
    jobs=[bq_demo_job],
    schedules=[bq_demo_schedule],
    resources={
        # 2. This is where the resource is actually configured.
        # We pass the loaded JSON credentials directly to the resource.
        "bigquery": BigQueryResource(
            project="athen-340910",
            gcp_credentials=service_account_info
        )
    },
)
