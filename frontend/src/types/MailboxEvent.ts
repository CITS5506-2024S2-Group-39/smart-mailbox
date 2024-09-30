export enum EventType {
  MailboxUnlocked = "Mailbox Unlocked",
  MailboxLocked = "Mailbox Locked",
  MailboxPasswordChanged = "Password Changed",
  MailboxIncomingMail = "New Mail",
  MailboxSecurityAlert = "Security Alert",
}

export interface MailboxEvent {
  id: number;
  time: Date; // number | string for network, once fetched, need to convert to Date for local processing
  type: string;
  comment: string;
}
