class Database:
    def start(self):
        print("[database] starting database...")
        print("[database] connecting with Mysql...")
        print("[database] running migrations...")
        print("[database] database running...")

    def stop(self):
        print("[database] stopping...")
        print("[database] database shut down successfully...")


class Server:
    def start(self):
        print("[server] starting server...")
        print("[server] loading deps...")
        print("[server] solving dependencies problems...")
        print("[server] server running...")

    def stop(self):
        print("[server] stopping...")
        print("[server] server shut down successfully...")


class Core:
    def __init__(self, config={}) -> None:
        self._database = config.get("database", Database())
        self._server = config.get("server", Server())

    def start(self):
        print("[core] starting...")
        self._database.start()
        self._server.start()
        print("[core] running...")

        return True

    def stop(self):
        print("[core] stopping...")
        self._database.stop()
        self._server.stop()
        print("[core] shut down successfully...")

        return True


# Tests to core, to keep it simple I'll not add an external framework to test


class Mock:

    def start(self):
        print("[mock] start")

    def stop(self):
        print("[mock] stop")


def test_core():
    subject = Core({"database": Mock(), "server": Mock()})

    assert subject.start()
    assert subject.stop()


if __name__ == "__main__":
    core = Core()
    try:
        core.start()
        core.stop()
    except Exception:
        print("Something went wrong...")

    print("#" * 10)
    test_core()
    print("#" * 10)
