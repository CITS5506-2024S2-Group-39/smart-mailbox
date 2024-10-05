import { requestAPI } from "@/api";
import type { MailboxEvent } from "@/types/MailboxEvent";
import { setIntervalWithCancel } from "@/utils/timeout";
import { shallowRef } from "vue";

const events = shallowRef<MailboxEvent[]>([]);
export default events;

// Handler to load latest events list from backend
const update = () => {
  requestAPI("/api/events", undefined, (data: MailboxEvent[]) => {
    for (const event of data) {
      // Convert JSON format to Date object
      const time = event.time;
      event.time = new Date(time);
    }
    events.value = data;
  });
};

// Load initial data
update();

// Refresh data with a certain interval
// A possible optimization could be only loading updates
// However, it will be tricky because content of existing items could also be updated
// Avoiding premature optimization for now
const interval = 10 * 1000;
const cancel = setIntervalWithCancel(update, interval);
