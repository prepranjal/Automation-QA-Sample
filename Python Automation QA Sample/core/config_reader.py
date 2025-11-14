# wrapstore_automation_py/core/config_reader.py

import os
import io
import configparser
import yaml


class ConfigReader:
    """
    Centralized configuration loader for the Wrapstore Automation Framework.
    Supports both .properties and .yaml configuration formats.
    """

    _props = configparser.ConfigParser()
    _yaml_config = None
    _config_loaded = False

    @classmethod
    def _load_config(cls):
        """Loads the configuration from resources/config/config.properties or config.yaml once."""
        if cls._config_loaded:
            return

        base_dir = os.path.dirname(__file__)
        # ✅ Correct relative path (core → ../resources/config)
        prop_path = os.path.abspath(os.path.join(base_dir, "..", "resources", "config", "config.properties"))
        yaml_path = os.path.abspath(os.path.join(base_dir, "..", "resources", "config", "config.yaml"))

        # Prefer YAML if available
        if os.path.exists(yaml_path):
            with open(yaml_path, "r", encoding="utf-8") as f:
                cls._yaml_config = yaml.safe_load(f)
                print(f"✅ Loaded configuration from: {yaml_path}")
        elif os.path.exists(prop_path):
            with io.open(prop_path, "r", encoding="utf-8") as f:
                content = f.read()
                if not content.strip().startswith("[DEFAULT]"):
                    # Add a fake section header for ConfigParser compatibility
                    content = "[DEFAULT]\n" + content
                cls._props.read_string(content)
                print(f"✅ Loaded configuration from: {prop_path}")
        else:
            raise FileNotFoundError(f"⚠️ No configuration file found at:\n{prop_path}\nor\n{yaml_path}")

        cls._config_loaded = True

    # ======================================================================
    # Public getters (used across framework)
    # ======================================================================

    @classmethod
    def get_base_url(cls):
        return cls.get_string("base_url", "https://wrapstore.in/")

    @classmethod
    def get_browser(cls):
        return cls.get_string("browser", "chrome").lower()

    @classmethod
    def get_timeout_seconds(cls):
        return cls.get_int("timeout", 10)

    @classmethod
    def is_headless(cls):
        return cls.get_boolean("headless", False)

    # ======================================================================
    # Generic access helpers
    # ======================================================================

    @classmethod
    def get_string(cls, key, default_value=None):
        cls._load_config()
        if cls._yaml_config:
            # YAML source
            value = cls._yaml_config.get(key, default_value)
            return str(value).strip() if value is not None else str(default_value)
        else:
            # Properties source
            if "DEFAULT" not in cls._props:
                raise KeyError("No DEFAULT section found in config.properties")
            value = cls._props["DEFAULT"].get(key)
            if value is None:
                return str(default_value)
            return value.strip()

    @classmethod
    def get_int(cls, key, default_value):
        try:
            return int(cls.get_string(key, default_value))
        except ValueError:
            return default_value

    @classmethod
    def get_boolean(cls, key, default_value=False):
        value = str(cls.get_string(key, default_value)).strip().lower()
        return value in ("true", "1", "yes")

    # ======================================================================
    # Optional utility to print loaded config (for debugging)
    # ======================================================================

    @classmethod
    def print_loaded_config(cls):
        cls._load_config()
        print("\n--- Loaded Configuration ---")
        if cls._yaml_config:
            for k, v in cls._yaml_config.items():
                print(f"{k} = {v}")
        else:
            for k, v in cls._props["DEFAULT"].items():
                print(f"{k} = {v}")
        print("-----------------------------\n")


# Example usage:
# ConfigReader.print_loaded_config()
# browser = ConfigReader.get_browser()
# base_url = ConfigReader.get_base_url()
# headless = ConfigReader.is_headless()
