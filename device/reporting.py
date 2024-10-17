import requests
import threading
import time
from config import EventReportConfig


def worker(interrupt, report_queue):
    print("Event report thread started")

    while not interrupt.is_set():
        try:
            data = report_queue.get(timeout=EventReportConfig.RETRY_INTERVAL)
        except:  # queue.Empty
            continue

        # Try to resend later if the report cannot be completed
        # But, if too much failure, will just drop the event
        for retry in range(0, EventReportConfig.MAX_RETRY):
            try:
                response = requests.put(EventReportConfig.URL, json=data, timeout=10)
                response.raise_for_status()
                break  # Break on success
            except Exception as e:
                print("Report event error:", e, "Try again later")
                time.sleep(EventReportConfig.RETRY_INTERVAL)
                # Always break if interrupt is set
                if interrupt.is_set():
                    break

    print("Event report thread stopped")


def init(interrupt, report_queue):
    # Start the event reporting thread
    thread = threading.Thread(target=worker, args=(interrupt, report_queue))
    thread.start()
    return thread
