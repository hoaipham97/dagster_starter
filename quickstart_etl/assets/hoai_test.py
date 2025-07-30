import base64
import json
import os
from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
import requests
from dagster import AssetExecutionContext, MaterializeResult, MetadataValue, asset


@asset(group_name="hoaipham_test", compute_kind="hoaipham_test Dagster")
def test1() -> None:
  print("ahihi")


@asset(deps=[test1], group_name="hoaipham_test", compute_kind="hoaipham_test Dagster")
def test2(context: AssetExecutionContext) -> int:
    print("test2_hihi")
    result = 1 + 3
    context.log.info(f"Result is {result}")
    return result
