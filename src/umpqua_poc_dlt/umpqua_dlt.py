"""
Docs:
AutoLoader Options - https://docs.databricks.com/en/ingestion/auto-loader/options.html
Data Quality - https://docs.databricks.com/en/delta-live-tables/expectations.html
Event Hooks - https://docs.databricks.com/en/delta-live-tables/event-hooks.html
Monitoring - https://docs.databricks.com/en/delta-live-tables/observability.html


Mode                            Behavior on reading new column

addNewColumns (default)         Stream fails. New columns are added to the schema. Existing columns do not evolve data types.

rescue                          Schema is never evolved and stream does not fail due to schema changes. All new columns are recorded in the rescued data column.

failOnNewColumns                Stream fails. Stream does not restart unless the provided schema is updated, or the offending data file is removed.

none                            Does not evolve the schema, new columns are ignored, and data is not rescued unless the rescuedDataColumn option is set. Stream does not fail due to schema changes.


COMMON OPTIONS:
cloudFiles.validateOptions
cloudFiles.partitionColumns
cloudFiles.backfillInterval
cloudFiles.schemaEvolutionMode
cloudFiles.schemaHints
cloudFiles.inferColumnTypes
"""

from pyspark.sql import SparkSession, DataFrame


def bronze_with_dlt(
    spark: SparkSession, source_path: str, options: dict[str, str]
) -> DataFrame:
    df = spark.readStream.format("cloudFiles").options(**options).load(source_path)
    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
