import { getAPI, postAPI } from "@/api";
import { showSuccess } from "@/stores/toast";
import { shallowReactive } from "vue";

const settings = shallowReactive<Record<string, string>>({});

export default settings;

interface Setting {
  key: string;
  value: string;
}

// Load initial data
getAPI("/api/settings", (data: Setting[]) => {
  for (const { key, value } of data) {
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
