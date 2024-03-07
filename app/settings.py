import dataclasses
import os

__all__ = [
    "settings",
]


@dataclasses.dataclass
class Settings:
    """Global application settings."""

    # General application settings
    api_path_str: str = "/api"
    host_url: str = os.getenv("HOST_URL", "http://0.0.0.0:8080")

    # Database settings
    db_url: str = os.getenv("POSTGRESQL_DATABASE_HOST", "")
    db_name: str = os.getenv("POSTGRESQL_DATABASE", "")
    db_user: str = os.getenv("POSTGRESQL_USER", "")
    db_password: str = os.getenv("POSTGRESQL_PASSWORD", "")
    sqlalchemy_database_url: str = f"postgresql://{db_user}:{db_password}@{db_url}/{db_name}"

    def check(self) -> None:
        if not self.host_url:
            raise RuntimeError(
                "Host url is not set! Make sure the environment variable "
                "'HOST_URL is set and its value is a valid route where "
                "this application is deployed.",
            )

        if not self.db_url:
            raise RuntimeError("POSTGRESQL_DATABASE_HOST is not set!")

        if not self.db_name:
            raise RuntimeError("POSTGRESQL_DATABASE is not set!")

        if not self.db_user:
            raise RuntimeError("POSTGRESQL_USER is not set!")

        if not self.db_password:
            raise RuntimeError("POSTGRESQL_PASSWORD is not set!")


settings = Settings()
