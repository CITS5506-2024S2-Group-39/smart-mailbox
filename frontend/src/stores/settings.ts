import { showInfo, showSuccess } from "./toast";
import { getAPI, postAPI } from "@/api";
import { setIntervalWithCancel } from "@/utils/timeout";
import { shallowReactive, shallowRef } from "vue";

const settings = shallowReactive<Record<string, string>>({});

export default settings;

interface Setting {
  key: string;
  value: string;
}

// Load initial data
getAPI("/api/settings", (data: Setting[]) => {
  for (let { key, value } of data) {
    if (settings[key] !== value) {
      settings[key] = value;
    }
  }
});

export const updateSetting = (key: string, value: string) => {
  settings[key] = value;
  postAPI("/api/settings", [{ key, value }], () => {
    showSuccess("Settings updated successfully.");
  });
};
