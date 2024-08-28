# logger client
import sqlite3
from sqlite3 import Connection, Cursor
import datetime


class _Logger(object):
    def __init__(self) -> None:
        self.month: int = datetime.datetime.now().month
        self.current_log: str = f"./logs/{self.month}.db"
        self.current_time = lambda: datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        self.conn: Connection = sqlite3.connect(self.current_log)

    # -----------------------------------------------------------
    def new_log(self) -> None:
        cur: Cursor = self.conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS info_log (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            DATETIME TEXT,
                            STATUS TEXT,
                            MESSAGE TEXT
                            )"""
        )
        self.conn.commit()

    # ---------------------------------------------------------
    def log(self, status, message) -> None:
        cur: Cursor = self.conn.cursor()
        cur.execute(
            """INSERT INTO info_log (DATETIME, STATUS, MESSAGE) VALUES (?,?,?)""",
            (
                self.current_time(),
                status,
                message,
            ),
        )
        self.conn.commit()

    # ---------------------------------------------------------
    def info(self, message) -> None:
        cur: Cursor = self.conn.cursor()
        cur.execute(
            """INSERT INTO info_log (DATETIME, STATUS, MESSAGE) VALUES (?,?,?)""",
            (
                self.current_time(),
                "INFO",
                message,
            ),
        )
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()


if __name__ == "__main__":
    logger = _Logger()
    logger.new_log()
    logger.log("info", "test")
    print(logger.current_time)
    logger.close()
