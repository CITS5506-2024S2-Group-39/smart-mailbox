import events from "@/api/events";
import { showError } from "@/stores/toast";
import sleep from "@/utils/sleep";

export interface JsonResponse {
  data?: any;
  error?: string;
}

function mockResponse(data: any) {
  let json: JsonResponse = { data };

  return new Response(
    JSON.stringify(json), //
    { status: 200, headers: { "Content-Type": "application/json" } },
  );
}

function mockError(code: number) {
  let json: JsonResponse = { error: `code ${code}` };

  return new Response(
    JSON.stringify(json), //
    { status: code },
  );
}

async function mockFetch(url: RequestInfo | URL, init?: RequestInit): Promise<Response> {
  await sleep(50 + Math.random() * 500); // simulate network latency
  if (url === "/api/events") {
    return mockResponse(events);
  }
  return mockError(404);
}

export async function requestAPI(input: RequestInfo | URL, init: RequestInit | undefined, callback: Function) {
  try {
    let response = await mockFetch(input, init); // change to fetch() in production
    let _json = await response.json();
    let json = _json as JsonResponse;
    if (!json.error) {
      callback(json.data);
    } else {
      showError(json.error);
    }
  } catch (e) {
    let error = e as Error;
    showError(error.message);
  }
}
