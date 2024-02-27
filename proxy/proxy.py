class RealSubject:
    def request(self):
        print("RealSubject: Handling request.")


class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
        else:
            print("Proxy: Access denied.")

    def check_access(self):
        # Additional logic to check access (e.g., authentication)
        return True


if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    # Client interacts with the proxy, not the real subject directly
    proxy.request()
