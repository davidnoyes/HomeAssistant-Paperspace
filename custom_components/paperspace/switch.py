"""Support for interacting with Paperspace machine."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import (
    ATTR_AGENT_TYPE,
    ATTR_CPUS,
    ATTR_CREATED_AT,
    ATTR_GPU,
    ATTR_MACHINE_ID,
    ATTR_MACHINE_STATE,
    ATTR_MACHINE_TYPE,
    ATTR_NAME,
    ATTR_OS,
    ATTR_PUBLIC_IP,
    ATTR_RAM,
    ATTR_REGION,
    ATTR_STORAGE_TOTAL,
    ATTR_STORAGE_USED,
    ATTR_UPDATES_PENDING,
    ATTR_USAGE_RATE,
    ATTRIBUTION,
    DATA_PAPERSPACE,
    ICON_OFF,
    ICON_ON,
)

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "Machine"


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the Paperspace machine switch."""
    if not (paperspace := hass.data.get(DATA_PAPERSPACE)):
        return

    dev = []
    for machine in paperspace.machines:
        dev.append(PaperspaceSwitch(paperspace, machine))

    add_entities(dev, True)


class PaperspaceSwitch(SwitchEntity):
    """Representation of a Paperspace machine switch."""

    _attr_attribution = ATTRIBUTION

    def __init__(self, paperspace, machine):  # pylint: disable=invalid-name
        """Initialize a new Paperspace switch."""
        self._paperspace = paperspace
        self.set_data(machine)

    @property
    def machine_id(self) -> str:
        """Return the machine id of the sensor."""
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """Set the machine id of the sensor."""
        self._machine_id = machine_id

    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return self._name

    @name.setter
    def name(self, name):
        """Set the name of the sensor."""
        self._name = name

    @property
    def os(self) -> str:  # pylint: disable=invalid-name
        """Return the os of the sensor."""
        return self._os

    @os.setter
    def os(self, os):  # pylint: disable=invalid-name
        """Set the os of the sensor."""
        self._os = os

    @property
    def ram(self):
        """Return the ram of the sensor."""
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Set the ram of the sensor."""
        self._ram = ram

    @property
    def cpus(self):
        """Return the cpus of the sensor."""
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        """Set the cpus of the sensor."""
        self._cpus = cpus

    @property
    def gpu(self):
        """Return the gpu of the sensor."""
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Set the gpu of the sensor."""
        self._gpu = gpu

    @property
    def storage_total(self):
        """Return the storage_total of the sensor."""
        return self._storage_total

    @storage_total.setter
    def storage_total(self, storage_total):
        """Set the storage_total of the sensor."""
        self._storage_total = storage_total

    @property
    def storage_used(self):
        """Return the storage_used of the sensor."""
        return self._storage_used

    @storage_used.setter
    def storage_used(self, storage_used):
        """Set the storage_used of the sensor."""
        self._storage_used = storage_used

    @property
    def machine_type(self) -> str:
        """Return the machine_type of the sensor."""
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """Set the machine_type of the sensor."""
        self._machine_type = machine_type

    @property
    def usage_rate(self):
        """Return the usage_rate of the sensor."""
        return self._usage_rate

    @usage_rate.setter
    def usage_rate(self, usage_rate):
        """Set the usage_rate of the sensor."""
        self._usage_rate = usage_rate

    @property
    def agent_type(self) -> str:
        """Return the agent_type of the sensor."""
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """Set the agent_type of the sensor."""
        self._agent_type = agent_type

    @property
    def created_at(self):
        """Return the created_at of the sensor."""
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Set the created_at of the sensor."""
        self._created_at = created_at

    @property
    def machine_state(self) -> str:
        """Return the machine_state of the sensor."""
        return self._machine_state

    @machine_state.setter
    def machine_state(self, machine_state):
        """Set the machine_state of the sensor."""
        self._machine_state = machine_state

    @property
    def updates_pending(self):
        """Return the updates_pending of the sensor."""
        return self._updates_pending

    @updates_pending.setter
    def updates_pending(self, updates_pending):
        """Set the updates_pending of the sensor."""
        self._updates_pending = updates_pending

    @property
    def public_ip(self):
        """Return the public_ip of the sensor."""
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Set the public_ip of the sensor."""
        self._public_ip = public_ip

    @property
    def region(self):
        """Return the region of the sensor."""
        return self._region

    @region.setter
    def region(self, region):
        """Set the region of the sensor."""
        self._region = region

    @property
    def is_on(self) -> bool:
        """Return true if the switch is on."""
        return self.machine_state != "off"

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes of the Paperspace machine."""
        return {
            ATTR_MACHINE_ID: self.machine_id,
            ATTR_NAME: self.name,
            ATTR_OS: self.os,
            ATTR_RAM: self.ram,
            ATTR_CPUS: self.cpus,
            ATTR_GPU: self.gpu,
            ATTR_STORAGE_TOTAL: self.storage_total,
            ATTR_STORAGE_USED: self.storage_used,
            ATTR_MACHINE_TYPE: self.machine_type,
            ATTR_USAGE_RATE: self.usage_rate,
            ATTR_AGENT_TYPE: self.agent_type,
            ATTR_CREATED_AT: self.created_at,
            ATTR_MACHINE_STATE: self.machine_state,
            ATTR_UPDATES_PENDING: self.updates_pending,
            ATTR_PUBLIC_IP: self.public_ip,
            ATTR_REGION: self.region,
        }

    def set_data(self, machine):
        """Set machine data."""
        self.machine_id = machine["id"]
        self.name = machine["name"]
        self.os = machine["os"]  # pylint: disable=invalid-name
        self.ram = machine["ram"]
        self.cpus = machine["cpus"]
        self.gpu = machine["gpu"]
        self.storage_total = machine["storageTotal"]
        self.storage_used = machine["storageUsed"]
        self.machine_type = machine["machineType"]
        self.usage_rate = machine["usageRate"]
        self.agent_type = machine["agentType"]
        self.created_at = machine["dtCreated"]
        self.machine_state = machine["state"]
        self.updates_pending = machine["updatesPending"]
        self.public_ip = machine["publicIpAddress"]
        self.region = machine["region"]

        if self.is_on:
            self._attr_icon = ICON_ON
        else:
            self._attr_icon = ICON_OFF

    def turn_on(self, **kwargs: Any) -> None:
        """Start the machine."""
        if self.machine_state == "off":
            self._paperspace.start_machine(self._machine_id)

    def turn_off(self, **kwargs: Any) -> None:
        """Stop the machine."""
        if self.machine_state != "off":
            self._paperspace.stop_machine(self.machine_id)

    def update(self) -> None:
        """Update state of sensor."""
        _LOGGER.debug("UPDATING PAPERSPACE MACHINE SWITCH")
        self._paperspace.update()

        for machine in self._paperspace.machines:
            if machine["id"] == self.machine_id:
                self.set_data(machine)
