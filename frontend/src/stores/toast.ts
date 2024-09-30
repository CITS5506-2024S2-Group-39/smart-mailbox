import { shallowReactive } from "vue";

export interface Toast {
  icon: string;
  title: string;
  message: string;
  timeout?: number;
}

export const toasts = shallowReactive<Toast[]>([]);

function hideToast(toast: Toast) {
  const { length } = toasts;
  for (let i = 0; i < length; ++i) {
    // Use object identity as identifier
    if (toasts[i] === toast) {
      toasts.splice(i, 1);
      return;
    }
  }
}

function showToast(toast: Toast) {
  toasts.push(toast);
  const timeout = toast.timeout || 5000;
  setTimeout(hideToast, timeout, toast);
  return toast;
}

export function showError(message: string, timeout?: number) {
  return showToast({
    icon: "error",
    title: "Error",
    message: message,
    timeout: timeout,
  });
}

export function showInfo(message: string, timeout?: number) {
  return showToast({
    icon: "info",
    title: "Info",
    message: message,
    timeout: timeout,
  });
}

export function showSuccess(message: string, timeout?: number) {
  return showToast({
    icon: "check_circle",
    title: "Success",
    message: message,
    timeout: timeout,
  });
}
