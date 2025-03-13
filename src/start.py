from blog import infrastructure, usecases
from utils import load_config


def main():
    service_config = load_config()

    storage_config = infrastructure.storage.StorageConfig(
        **service_config.storage_config
    )
    storage = infrastructure.storage.Storage(storage_config=storage_config)
    post_usecases = usecases.PostUsecases(storage)
    server = infrastructure.api_server.FastAPIServer(post_usecases)
    server.start()


if __name__ == "__main__":
    main()
