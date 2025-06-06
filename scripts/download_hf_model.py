import os
from huggingface_hub import HfApi


def download_model(model_name: str, token: str, target_dir: str = "models"):
    os.makedirs(target_dir, exist_ok=True)
    api = HfApi(token=token)
    api.download_repo(repo_id=model_name, repo_type="model", local_dir=target_dir)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Download a model from Hugging Face Hub")
    parser.add_argument("model_name", help="Model name or repository ID")
    parser.add_argument("--token", dest="token", default=os.getenv("HF_API_TOKEN"), help="Hugging Face access token")
    parser.add_argument("--target", dest="target_dir", default="models", help="Directory to store the model")

    args = parser.parse_args()

    if not args.token:
        parser.error("No token provided. Set --token or HF_API_TOKEN environment variable.")

    download_model(args.model_name, args.token, args.target_dir)
