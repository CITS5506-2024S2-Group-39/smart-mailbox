export function setTimeoutWithCancel(handler: TimerHandler, timeout?: number, ...args: any[]): () => void {
  const id = setTimeout(handler, timeout, ...args);
  const cancel = () => clearTimeout(id);
  return cancel;
}

export function setIntervalWithCancel(handler: TimerHandler, delay?: number, ...args: any[]): () => void {
  const id = setInterval(handler, delay, ...args);
  const cancel = () => clearInterval(id);
  return cancel;
}
