// src/types/MailboxEvents.ts

export enum EventType {
  MailboxUnlocked = "Mailbox Unlocked",
  MailboxLocked = "Mailbox Locked",
  MailboxPasswordChanged = "Password Changed",
  MailboxIncomingMail = "New Mail",
  MailboxSecurityAlert = "Security Alert",
}

export interface MailboxEvent {
  id: number;
  time: number;
  type: string;
  comment: string;
}
