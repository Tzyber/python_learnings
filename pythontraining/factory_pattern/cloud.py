from abc import ABC, abstractmethod

class CloudInstance(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

class CloudProvider(ABC):
    @abstractmethod
    def create_instance(self):
        pass

class AWSInstance(CloudInstance):
    def start(self):
        print("AWS Instance gestartet")

    def stop(self):
        print("AWS Instance gestoppt")

    def get_status(self):
        print("AWS Instance Status: Running")

class AWSProvider(CloudProvider):
    def create_instance(self):
        return AWSInstance()

class AzureInstance(CloudInstance):
    def start(self):
        print("Azure Instance gestartet")

    def stop(self):
        print("Azure Instance gestoppt")

    def get_status(self):
        print("Azure Instance Status: Running")

class AzureProvider(CloudProvider):
    def create_instance(self):
        return AzureInstance()

class GCPInstance(CloudInstance):
    def start(self):
        print("GCP Instance gestartet")

    def stop(self):
        print("GCP Instance gestoppt")

    def get_status(self):
        print("GCP Instance Status: Running")

class GCPProvider(CloudProvider):
    def create_instance(self):
        return GCPInstance()


def deploy(cloud_provider: CloudProvider):
    instance = cloud_provider.create_instance()
    instance.start()
    instance.get_status()
    instance.stop()

def provider_config(config_name):
    providers = {
        "AWS": AWSProvider,
        "AZURE": AzureProvider,
        "GCP": GCPProvider
    }
    provider_class = providers.get(config_name)

    if not provider_class:
        raise ValueError(f"Unbekannter Cloud-Provider: {config_name}")

    return provider_class()

if __name__ == "__main__":

    config_list = ["AWS", "AZURE", "GCP"]
    for config in config_list:
        print(f"Deploying to {config}...")
        provider = provider_config(config)
        deploy(provider)

    print("Versuch mit unbekanntem Provider:")
    try:
        bad_list = ["AWs", "AZURe", "GCp"]
        provider = provider_config(bad_list[1])
        deploy(provider)
    except ValueError as e:
        print(e)
