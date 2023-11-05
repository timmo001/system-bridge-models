# Model
from .battery import Battery
from .cpu import Cpu
from .data import Data
from .disk import Disk
from .display import Display
from .generic import Generic
from .gpu import Gpu
from .keyboard_key import KeyboardKey
from .keyboard_text import KeyboardText
from .media import Media
from .media_directories import MediaDirectories
from .media_files import File, MediaFiles
from .memory import Memory
from .network import Network
from .notification import Notification
from .open_path import OpenPath
from .open_url import OpenUrl
from .processes import Processes
from .response import Response
from .sensors import Sensors
from .system import System

MODEL_BATTERY = "battery"
MODEL_CPU = "cpu"
MODEL_DATA = "data"
MODEL_DISK = "disk"
MODEL_DISPLAY = "display"
MODEL_GENERIC = "generic"
MODEL_GPU = "gpu"
MODEL_KEYBOARD_KEY = "keyboard_key"
MODEL_KEYBOARD_TEXT = "keyboard_text"
MODEL_MEDIA = "media"
MODEL_MEDIA_DIRECTORIES = "media_directories"
MODEL_MEDIA_FILE = "media_file"
MODEL_MEDIA_FILES = "media_files"
MODEL_MEMORY = "memory"
MODEL_NETWORK = "network"
MODEL_NOTIFICATION = "notification"
MODEL_OPEN_PATH = "open_path"
MODEL_OPEN_URL = "open_url"
MODEL_PROCESSES = "processes"
MODEL_RESPONSE = "response"
MODEL_SECRETS = "secrets"
MODEL_SENSORS = "sensors"
MODEL_SETTINGS = "settings"
MODEL_SYSTEM = "system"

MODEL_MAP = {
    MODEL_BATTERY: Battery,
    MODEL_CPU: Cpu,
    MODEL_DATA: Data,
    MODEL_DISK: Disk,
    MODEL_DISPLAY: Display,
    MODEL_GENERIC: Generic,
    MODEL_GPU: Gpu,
    MODEL_KEYBOARD_KEY: KeyboardKey,
    MODEL_KEYBOARD_TEXT: KeyboardText,
    MODEL_MEDIA_DIRECTORIES: MediaDirectories,
    MODEL_MEDIA_FILE: File,
    MODEL_MEDIA_FILES: MediaFiles,
    MODEL_MEDIA: Media,
    MODEL_MEMORY: Memory,
    MODEL_NETWORK: Network,
    MODEL_NOTIFICATION: Notification,
    MODEL_OPEN_PATH: OpenPath,
    MODEL_OPEN_URL: OpenUrl,
    MODEL_PROCESSES: Processes,
    MODEL_RESPONSE: Response,
    MODEL_SENSORS: Sensors,
    MODEL_SYSTEM: System,
}
