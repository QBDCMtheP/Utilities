def get_k8s_secret(secret_name: str, key: str, namespace: str = 'kubeflow'):
        """
        Retrieves a decoded value from a specified Kubernetes secret.
        
        This function is designed to be a standalone utility function, not a component of a Kubeflow Pipeline.
        It can be used within any Python code that has appropriate access to the Kubernetes API.

        Parameters:
            secret_name (str): The name of the Kubernetes secret.
            key (str): The key within the secret to retrieve.
            namespace (str): The namespace where the secret is stored, defaults to 'kubeflow'.
        
        Returns:
            str: The decoded string value of the secret or None if an error occurs.
        """
        
        from kubernetes import client, config
        import base64

        try:
            # Load Kubernetes configuration to enable API access
            config.load_incluster_config()
            # Initialize the Kubernetes client for the Core V1 API
            v1 = client.CoreV1Api()

            # Fetch the secret from the specified namespace
            secret_data = v1.read_namespaced_secret(secret_name, namespace).data[key]

            # Decode the base64 encoded data and return the decoded string
            decoded_value = base64.b64decode(secret_data).decode('utf-8')
            return decoded_value
        
        except Exception as e:
            # Handle any exceptions that occur and print an error message
            print(f"Error retrieving secret {secret_name} key {key}: {e}")
            return None