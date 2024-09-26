export default [
  {
    id: 0,
    time: new Date("2024-09-25 08:00").getTime(),
    type: "Password Changed",
    comment: "You have reset your mailbox password in dashboard.",
  },
  {
    id: 1,
    time: new Date("2024-09-25 13:00").getTime(),
    type: "New Mail",
    comment: String.raw`The mail cover features the recipient, JAMESON FIELDS, at 24 ELMWOOD DRIVE, BRIGHTON CA 90210, and is sent from P.O. BOX 1234, BIRCHWOOD HEIGHTS, ONTARIO K1A 0B1, Toronto, Canada. It includes prepaid postage, a tracking number (XPQ 876-5), and a barcode, indicating it is likely official business correspondence. The back of the envelope shows "BUSINESS REPLY PAID" information, suggesting it contains important documents.`,
  },
  {
    id: 2,
    time: new Date("2024-09-25 17:00").getTime(),
    type: "New Mail",
    comment: String.raw`A mail cover shows that the recipient, EMILY JOHNSON, is at 12 PARK AVENUE, BRISBANE QLD 4000, and it was sent from PO BOX 456, GOLD COAST QLD 4217. This package includes a return address, a tracking code (ABC 123-4), and indicates that it contains merchandise from an online retailer.`,
  },
  {
    id: 3,
    time: new Date("2024-09-26 08:00").getTime(),
    type: "Mailbox Unlocked",
    comment: "The mailbox was unlocked successfully, allowing you to retrieve incoming mail.",
  },
  {
    id: 4,
    time: new Date("2024-09-26 08:05").getTime(),
    type: "Mailbox Locked",
    comment: "The mailbox has been locked after retrieval to ensure security.",
  },
  {
    id: 5,
    time: new Date("2024-09-26 12:05").getTime(),
    type: "New Mail",
    comment: String.raw`The mail cover indicates the recipient, ALEX SMITH, residing at 88 HILL STREET, PERTH WA 6000, received a letter from LOCKED BAG 123, MELBOURNE VIC 3000. It features prepaid postage and suggests that it is an official communication from a government department.`,
  },
  {
    id: 6,
    time: new Date("2024-09-27 08:00").getTime(),
    type: "New Mail",
    comment: String.raw`A mail cover shows that the recipient, SARA WILSON, is at 20 OCEAN DRIVE, ADELAIDE SA 5000, and it was sent from PO BOX 789, SYDNEY NSW 2000. This envelope includes a tracking number (XYZ 987-6) and indicates it is an important document from a financial institution.`,
  },
  {
    id: 7,
    time: new Date("2024-09-28 09:00").getTime(),
    type: "New Mail",
    comment: String.raw`The mail cover features the recipient, MIKE BROWN, at 15 MOUNTAIN ROAD, HOBART TAS 7000, sent from 300 MAILING STREET, CANBERRA ACT 2600. It has prepaid postage and contains a promotional brochure from a travel agency.`,
  },
  {
    id: 8,
    time: new Date("2024-09-28 10:00").getTime(),
    type: "Security Alert",
    comment:
      "Multiple failed attempts to unlock the mailbox have been detected within a short period. This may indicate unauthorized access attempts.",
  },
  {
    id: 9,
    time: new Date("2024-09-28 12:00").getTime(),
    type: "You can put anything here",
    comment:
      "The type and the comment will be displayed as it is. However, if the type is not recognized, its icon will be the same as the one of security alert.",
  },
].reverse();
