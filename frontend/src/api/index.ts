import { showError } from "@/stores/toast";

async function requestAPI(input: RequestInfo | URL, init: RequestInit | undefined, callback: Function) {
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

export function getAPI(input: RequestInfo | URL, callback: Function) {
  return requestAPI(input, undefined, callback);
}

export function postAPI(input: RequestInfo | URL, body: any, callback: Function) {
  body = JSON.stringify(body);
  return requestAPI(
    input,
    {
      method: "POST",
      body: body,
      headers: { "Content-Type": "application/json" },
    },
    callback,
  );
}

export function putAPI(input: RequestInfo | URL, body: any, callback: Function) {
  body = JSON.stringify(body);
  return requestAPI(
    input,
    {
      method: "PUT",
      body: body,
      headers: { "Content-Type": "application/json" },
    },
    callback,
  );
}
