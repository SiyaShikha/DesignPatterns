from singleton.dbconnection.db_connection import DatabaseConnection

def test_returns_same_instance():
    db1 = DatabaseConnection.get_instance()
    db2 = DatabaseConnection.get_instance()

    assert db1 is db2

def test_shared_state():
    db1 = DatabaseConnection.get_instance()
    db2 = DatabaseConnection.get_instance()

    db1.connected = False
    assert db2.connected is False