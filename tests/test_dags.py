import pytest
from dags.etl_dag import dag

def test_dag_loaded():
    """Test that the DAG loads without errors."""
    assert dag is not None

def test_dag_id():
    """Test that the DAG has the correct ID."""
    assert dag.dag_id == "zaalima_main_pipeline"

def test_dag_schedule():
    """Test that the DAG is scheduled daily."""
    assert dag.schedule_interval == "@daily"

def test_dag_has_tasks():
    """Test that the DAG has at least one task."""
    assert len(dag.tasks) > 0