from dagster import AssetExecutionContext, asset

@asset(group_name="hoaipham_test", compute_kind="hoaipham_test Dagster")
def test1(context: AssetExecutionContext) -> None:
  """A simple asset that prints a message."""
  print("ahihi")


@asset(deps=[test1], group_name="hoaipham_test", compute_kind="hoaipham_test Dagster")
def test2(context: AssetExecutionContext) -> int:
    """A simple asset that depends on test1 and returns a value."""
    print("test2_hihi")
    result = 1 + 3
    context.log.info(f"Result is {result}")
    return result
