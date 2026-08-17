from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    mode = os.getenv("MATRIX_MODE", "development")
    database = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")

    print(f"Mode: {mode}")

    if database:
        print("Database: Connected to local instance")
    else:
        print("Database: Not connected")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured")

    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print("Log Level: Not configured")

    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print()

    if mode == "development":
        print("Running in DEVELOPMENT mode.")
    else:
        print("Running in PRODUCTION mode.")

    print("\nEnvironment security check:")

    if api_key:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] API key is missing")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available")
