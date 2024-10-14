import { showInfo, showSuccess } from "./toast";
import { requestAPI } from "@/api";
import { setIntervalWithCancel } from "@/utils/timeout";
import { shallowReactive, shallowRef } from "vue";

const settings = shallowReactive<Record<string, string>>({});

export default settings;

interface Setting {
  key: string;
  value: string;
}

// Load initial data
requestAPI("/api/settings", undefined, (data: Setting[]) => {
  for (let { key, value } of data) {
    if (settings[key] !== value) {
      settings[key] = value;
    }
  }
});

export const updateSetting = (key: string, value: string) => {
  if (settings[key] === value) {
    return;
  }

  settings[key] = value;
  console.log(key, value);

  requestAPI(
    "/api/settings",
    {
      method: "POST",
      body: JSON.stringify([{ key, value }]), // Convert to JSON string
      headers: { "Content-Type": "application/json" },
    },
    ({ message }: { message: string }) => {
      showSuccess(message);
    },
  );
};
