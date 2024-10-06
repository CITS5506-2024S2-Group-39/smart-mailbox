import { requestAPI } from "@/api";
import { setIntervalWithCancel } from "@/utils/timeout";
import { shallowRef } from "vue";

export enum EventType {
  MailboxUnlocked = "Mailbox Unlocked",
  MailboxLocked = "Mailbox Locked",
  MailboxPasswordChanged = "Password Changed",
  MailboxIncomingMail = "New Mail",
  MailboxSecurityAlert = "Security Alert",
}

interface EventData {
  summary: string;
  // Different event type will have different custom fields here
}

interface MailEventData extends EventData {
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

export interface MailboxEvent {
  id: number;
  time: Date; // number | string for network, once fetched, need to convert to Date for local processing
  type: string; // one of EventType
  data: EventData | MailEventData;
}

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
