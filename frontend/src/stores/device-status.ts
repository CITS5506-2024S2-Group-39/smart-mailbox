import { getAPI, postAPI } from "@/api";
import { setIntervalWithCancel } from "@/utils/timeout";
import { shallowReactive } from "vue";

interface DeviceStatus {
  online: boolean;
  since: Date;
  lastseen: Date;
  locked: boolean;
}

const deviceStatus = shallowReactive<DeviceStatus>({
  online: false,
  since: new Date(1970, 0, 1),
  lastseen: new Date(1970, 0, 1),
  locked: true,
});
export default deviceStatus;

// Handler to load latest events list from backend
const update = () => {
  postAPI("/api/devstat", {}, (data: DeviceStatus) => {
    // Convert JSON format to Date object
    deviceStatus.online = data.online;
    deviceStatus.since = new Date(data.since);
    deviceStatus.lastseen = new Date(data.lastseen);
    deviceStatus.locked = data.locked;
  });
};

// Load initial data
update();

// Refresh data with a certain interval
const interval = 1 * 1000;
const cancel = setIntervalWithCancel(update, interval);
