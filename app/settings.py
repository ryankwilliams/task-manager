import os

__all__ = [
    "settings",
]


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

    @classmethod
    def check(cls) -> None:
        if not cls.host_url:
            raise RuntimeError(
                "Host url is not set! Make sure the environment variable "
                "'HOST_URL is set and its value is a valid route where "
                "this application is deployed.",
            )

        if not cls.db_url:
            raise RuntimeError(
                "POSTGRESQL_DATABASE_HOST is not set! Set it and try again.",
            )

        if not cls.db_name:
            raise RuntimeError("POSTGRESQL_DATABASE is not set! Set it and try again.")

        if not cls.db_user:
            raise RuntimeError("POSTGRESQL_USER is not set! Set it and try again.")

        if not cls.db_password:
            raise RuntimeError("POSTGRESQL_PASSWORD is not set! Set it and try again.")


settings: Settings = Settings()
