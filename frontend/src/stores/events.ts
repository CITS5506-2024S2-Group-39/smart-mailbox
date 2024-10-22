import { getAPI, postAPI } from "@/api";
import { setIntervalWithCancel } from "@/utils/timeout";
import { shallowReactive } from "vue";

export enum EventType {
  MailboxUnlocked = "Mailbox Unlocked",
  MailboxLocked = "Mailbox Locked",
  MailboxPasswordChanged = "Password Changed",
  MailboxIncomingMail = "New Mail",
  MailboxSecurityAlert = "Security Alert",
}

interface EventData {
  summary: string;
  image: string;
  // The following are for "New Mail" events only
  recipient_name: string | null;
  recipient_address: {
    street: string | null;
    city: string | null;
    state: string | null;
    postal_code: string | null;
  };
  sender_name: string | null;
  sender_address: {
    street: string | null;
    city: string | null;
    state: string | null;
    postal_code: string | null;
  };
  tracking_number: string | null;
  postage_information: string | null;
  mail_type: string;
}

export const MailTypes = ["Official", "Personal", "Commercial", "Advertising", "Parcel", "Unknown"];

export interface MailboxEvent {
  id: number;
  time: Date; // number | string for network, once fetched, need to convert to Date for local processing
  type: string; // one of EventType
  data: EventData;
}

const events = shallowReactive<MailboxEvent[]>([]);
export default events;

// Handler to load latest events list from backend
export const fullUpdate = () => {
  getAPI("/api/events", (data: MailboxEvent[]) => {
    // Convert JSON format to Date object
    for (const event of data) {
      const time = event.time;
      event.time = new Date(time);
    }

    // Replace all existing events with new value
    events.splice(0, events.length, ...data);
  });
};

export const deltaUpdate = () => {
  const latest = events[0];
  if (!latest) {
    return fullUpdate();
  }

  postAPI("/api/events", { id: latest.id }, (data: MailboxEvent[]) => {
    // Convert JSON format to Date object
    for (const event of data) {
      const time = event.time;
      event.time = new Date(time);
    }

    const latest = events[0];
    const id = latest.id;

    // Add new events to the array
    data = data.reverse();
    for (const event of data) {
      // This comparision handles case when
      // request deltaUpdate -> request fullUpdate -> receive fullUpdate -> receive deltaUpdate
      if (event.id > id) {
        events.unshift(event);
      }
    }
  });
};

// Load initial data
fullUpdate();

// Refresh data with a certain interval
const interval = 1 * 1000;
let count = 0;
setIntervalWithCancel(() => {
  count += 1;
  count %= 64;
  if (count === 0) {
    // Perform full update
    fullUpdate();
  } else {
    // load only deltas
    deltaUpdate();
  }
}, interval);
