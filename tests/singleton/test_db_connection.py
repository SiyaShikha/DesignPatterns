from singleton.db_connection import DatabaseConnection

def test_returns_same_instance():
    db1 = DatabaseConnection.get_instance()
    db2 = DatabaseConnection.get_instance()

    assert db1 is db2