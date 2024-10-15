class EventType:
    # Must be same as the frontend definitions
    MailboxUnlocked = "Mailbox Unlocked"
    MailboxLocked = "Mailbox Locked"
    MailboxPasswordChanged = "Password Changed"
    MailboxIncomingMail = "New Mail"
    MailboxSecurityAlert = "Security Alert"
    # Currently, Only used by device for internal processing
    MailboxPasswordInput = "Password Input"
