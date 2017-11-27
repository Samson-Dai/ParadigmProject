from _kof97_database import _kof97_database

kof = _kof97_database()
kof.reset_all_data()
kof.record_game(10, 2000, 1)
kof.write_to_files()