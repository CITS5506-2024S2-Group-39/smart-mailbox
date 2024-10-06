import { showError } from "@/stores/toast";

export async function requestAPI(input: RequestInfo | URL, init: RequestInit | undefined, callback: Function) {
  try {
    const response = await fetch(input, init);
    const data = await response.json();
    if (data && typeof data === "object" && "error" in data) {
      // Show error message from backend
      showError(data.error);
    } else {
      // Pass data to
      callback(data);
    }
  } catch (e) {
    // Show error message from frontend
    const error = e as Error;
    showError(error.message);
  }
}
