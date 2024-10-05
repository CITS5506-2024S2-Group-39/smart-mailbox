const map = new WeakMap<object, number>();
let counter = Number.MIN_SAFE_INTEGER;

// Returns the unique identity of an object
export default function id(obj: object): number {
  let id = map.get(obj);
  if (id) {
    return id;
  }
  id = counter;
  counter += 1;
  map.set(obj, id);
  return id;
}
