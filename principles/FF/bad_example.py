class BackupJob:
    def __init__(self, config: dict[str, str]) -> None:
        self.config = config

    def run(self) -> None:
        print(f"Scanning files in {self.config['source_dir']}...")
        print(f"Preparing destination {self.config['destination_dir']}...")

        # The job starts work before learning whether the configuration is valid.
        compression_level = int(self.config["compression_level"])

        print(f"Compressing files with level {compression_level}...")
        print("Backup completed.")


if __name__ == "__main__":
    config = {
        "source_dir": "./documents",
        "destination_dir": "./backup",
        "compression_level": "high",
    }

    job = BackupJob(config)
    job.run()
