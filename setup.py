"""Setup script using uv - run this to initialize the project."""

import subprocess
import sys
import os


def run_command(cmd):
    """Run a shell command and print output."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result.returncode == 0


def main():
    """Setup the project with uv."""
    print("Setting up Farm OS MCP project with uv...")
    print("=" * 60)
    
    # Check if uv is installed
    if not run_command("uv --version"):
        print("\nERROR: uv is not installed!")
        print("Install uv from: https://docs.astral.sh/uv/")
        print("\nOn Windows (PowerShell):")
        print("  irm https://astral.sh/uv/install.ps1 | iex")
        sys.exit(1)
    
    # Sync dependencies
    print("\n1. Syncing dependencies...")
    if not run_command("uv sync"):
        print("ERROR: Failed to sync dependencies")
        sys.exit(1)
    
    print("\n2. Installing dependencies...")
    if not run_command("uv pip install -e ."):
        print("ERROR: Failed to install dependencies")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("Setup complete!")
    print("\nTo run the server:")
    print("  uv run python farmos_server.py")
    print("\nTo test the tools:")
    print("  uv run python test_server.py")
    print("=" * 60)


if __name__ == "__main__":
    main()

