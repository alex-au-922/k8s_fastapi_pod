import random
import string


def random_paths() -> list[str]:
    return [
        "".join(
            random.choices(
                string.ascii_lowercase + string.digits + string.ascii_uppercase, k=10
            )
        )
        for _ in range(10)
    ]
