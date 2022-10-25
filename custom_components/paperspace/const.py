"""Constants for Paperspace Integration."""
from datetime import timedelta

ATTR_MACHINE_ID = "machine_id"
ATTR_NAME = "name"
ATTR_OS = "os"
ATTR_RAM = "ram"
ATTR_CPUS = "cpus"
ATTR_GPU = "gpu"
ATTR_STORAGE_TOTAL = "storage_total"
ATTR_STORAGE_USED = "storage_used"
ATTR_MACHINE_TYPE = "machine_type"
ATTR_USAGE_RATE = "usage_rate"
ATTR_AGENT_TYPE = "agent_type"
ATTR_CREATED_AT = "created_at"
ATTR_MACHINE_STATE = "machine_state"
ATTR_UPDATES_PENDING = "updates_pending"
ATTR_PUBLIC_IP = "public_ip"
ATTR_REGION = "region"

ATTRIBUTION = "Data provided by Paperspace"

DATA_PAPERSPACE = "data_paperspace"

DOMAIN = "paperspace"

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=2)

PAPERSPACE_URL = "https://api.paperspace.io/"

ICON_ON = "mdi:server"
ICON_OFF = "mdi:server-off"

DEFAULT_NAME = "Machine"
