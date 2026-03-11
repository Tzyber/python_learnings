from abc import ABC, abstractmethod

class Cloudnstance(ABC):
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

class AWSInstance(Cloudnstance):
    def start(self):
        print("AWS Instance gestartet")

    def stop(self):
        print("AWS Instance gestoppt")

    def get_status(self):
        print("AWS Instance Status: Running")

class AWSProvider(CloudProvider):
    def create_instance(self):
        return AWSInstance()

class AzureInstance(Cloudnstance):
    def start(self):
        print("Azure Instance gestartet")

    def stop(self):
        print("Azure Instance gestoppt")

    def get_status(self):
        print("Azure Instance Status: Running")

class AzureProvider(CloudProvider):
    def create_instance(self):
        return AzureInstance()

class GCPInstance(Cloudnstance):
    def start(self):
        print("GCP Instance gestartet")

    def stop(self):
        print("GCP Instance gestoppt")

    def get_status(self):
        print("GCP Instance Status: Running")

class GCPProvider(CloudProvider):
    def create_instance(self):
        return GCPInstance()


def deploy(provider: CloudProvider):
    instance = provider.create_instance()
    instance.start()
    instance.get_status()
    instance.stop()


if __name__ == "__main__":
    aws_provider = AWSProvider()
    azure_provider = AzureProvider()
    gcp_provider = GCPProvider()

    print("Deploying on AWS:")
    deploy(aws_provider)

    print("\nDeploying on Azure:")
    deploy(azure_provider)

    print("\nDeploying on GCP:")
    deploy(gcp_provider)
