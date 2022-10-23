"""Support for Paperspace."""
import json
import logging

import requests
import voluptuous as vol

from homeassistant.const import CONF_API_KEY, Platform
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType
from homeassistant.util import Throttle

from .const import DATA_PAPERSPACE, DOMAIN, MIN_TIME_BETWEEN_UPDATES, PAPERSPACE_URL

_LOGGER = logging.getLogger(__name__)

PAPERSPACE_PLATFORMS = [Platform.BINARY_SENSOR]

CONFIG_SCHEMA = vol.Schema(
    {DOMAIN: vol.Schema({vol.Required(CONF_API_KEY): cv.string})},
    extra=vol.ALLOW_EXTRA,
)


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Paperspace component."""

    conf = config[DOMAIN]
    api_key = conf[CONF_API_KEY]

    paperspace = Paperspace(api_key)

    hass.data[DATA_PAPERSPACE] = paperspace

    return True


class Paperspace:
    """Handle all communication with the Paperspace API."""

    def __init__(self, api_key):
        """Initialize the Paperspace connection."""

        self.api_key = api_key
        self.machines = self._machines()

    def _machines(self):
        """List information about all machines available to either the current authenticated user or the team."""
        path = PAPERSPACE_URL + "machines/getMachines"
        headers = {
            "X-API-Key": self.api_key,
            "ps_client_name": "homeassistant-paperspace",
        }
        params = None
        json_data = None
        response = requests.get(
            path, params=params, headers=headers, json=json_data, timeout=10
        )
        _LOGGER.debug("Response content: %s", response.content)
        try:
            machines = json.loads(response.content)
        except json.JSONDecodeError:
            _LOGGER.error("Invalid JSON in Paperspace API response")
            raise
        return machines

    def start_machine(self, machine_id):
        """Start Paperspace machine."""
        path = PAPERSPACE_URL + "machines/" + machine_id + "/start"
        headers = {
            "X-API-Key": self.api_key,
            "ps_client_name": "homeassistant-paperspace",
        }
        params = None
        json_data = None
        response = requests.post(
            path, params=params, headers=headers, json=json_data, timeout=10
        )
        _LOGGER.debug("Response content: %s", response.content)

    def stop_machine(self, machine_id):
        """Stop Paperspace machine."""
        path = PAPERSPACE_URL + "machines/" + machine_id + "/stop"
        headers = {
            "X-API-Key": self.api_key,
            "ps_client_name": "homeassistant-paperspace",
        }
        params = None
        json_data = None
        response = requests.post(
            path, params=params, headers=headers, json=json_data, timeout=10
        )
        _LOGGER.debug("Response content: %s", response.content)

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Use the data from Paperspace API."""
        _LOGGER.debug("UPDATING PAPERSPACE MACHINES")
        self.machines = self._machines()
