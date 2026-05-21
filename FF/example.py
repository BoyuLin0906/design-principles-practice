class BackupConfig:
    def __init__(
        self,
        source_dir: str,
        destination_dir: str,
        compression_level: int,
    ) -> None:
        if not source_dir:
            raise ValueError("source_dir must not be empty")

        if not destination_dir:
            raise ValueError("destination_dir must not be empty")

        if not 0 <= compression_level <= 9:
            raise ValueError("compression_level must be between 0 and 9")

        self.source_dir = source_dir
        self.destination_dir = destination_dir
        self.compression_level = compression_level


class BackupJob:
    def __init__(self, config: BackupConfig) -> None:
        self.config = config

    def run(self) -> None:
        print(f"Scanning files in {self.config.source_dir}...")
        print(f"Preparing destination {self.config.destination_dir}...")
        print(f"Compressing files with level {self.config.compression_level}...")
        print("Backup completed.")


if __name__ == "__main__":
    try:
        config = BackupConfig(
            source_dir="./documents",
            destination_dir="./backup",
            compression_level=12,
        )
    except ValueError as error:
        print(f"Configuration error: {error}")
    else:
        job = BackupJob(config)
        job.run()
