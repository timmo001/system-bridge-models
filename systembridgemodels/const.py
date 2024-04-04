"""Model constants."""

from enum import StrEnum

from .keyboard_key import KeyboardKey
from .keyboard_text import KeyboardText
from .media_directories import MediaDirectory
from .media_files import MediaFile, MediaFiles
from .modules import Module, ModulesData
from .modules.battery import Battery
from .modules.cpu import CPU
from .modules.disks import Disks
from .modules.displays import Display
from .modules.gpus import GPU
from .modules.media import Media
from .modules.memory import Memory
from .modules.networks import Networks
from .modules.processes import Process
from .modules.sensors import Sensors
from .modules.system import System
from .notification import Notification
from .open_path import OpenPath
from .open_url import OpenUrl
from .response import Response


class Model(StrEnum):
    """Model Enums."""

    BATTERY = Module.BATTERY
    CPU = Module.CPU
    DATA = "data"
    DISKS = Module.DISKS
    DISPLAYS = Module.DISPLAYS
    GPUS = Module.GPUS
    KEYBOARD_KEY = "keyboard_key"
    KEYBOARD_TEXT = "keyboard_text"
    MEDIA = Module.MEDIA
    MEDIA_DIRECTORIES = "media_directories"
    MEDIA_FILE = "media_file"
    MEDIA_FILES = "media_files"
    MEMORY = Module.MEMORY
    NETWORKS = Module.NETWORKS
    NOTIFICATION = "notification"
    OPEN_PATH = "open_path"
    OPEN_URL = "open_url"
    PROCESSES = Module.PROCESSES
    RESPONSE = "response"
    SECRETS = "secrets"
    SENSORS = Module.SENSORS
    SETTINGS = "settings"
    SYSTEM = Module.SYSTEM


MODEL_MAP = {
    Model.BATTERY: Battery,
    Model.CPU: CPU,
    Model.DATA: ModulesData,
    Model.DISKS: Disks,
    Model.DISPLAYS: Display,  # Map to Display not list[Display] so it can be mapped
    Model.GPUS: GPU,  # Map to GPU not list[GPU] so it can be mapped
    Model.KEYBOARD_KEY: KeyboardKey,
    Model.KEYBOARD_TEXT: KeyboardText,
    Model.MEDIA_DIRECTORIES: MediaDirectory,  # Map to MediaDirectory not list[MediaDirectory] so it can be mapped
    Model.MEDIA_FILE: MediaFile,
    Model.MEDIA_FILES: MediaFiles,
    Model.MEDIA: Media,
    Model.MEMORY: Memory,
    Model.NETWORKS: Networks,
    Model.NOTIFICATION: Notification,
    Model.OPEN_PATH: OpenPath,
    Model.OPEN_URL: OpenUrl,
    Model.PROCESSES: Process,  # Map to Process not list[Process] so it can be mapped
    Model.RESPONSE: Response,
    Model.SENSORS: Sensors,
    Model.SYSTEM: System,
}
