const map = new WeakMap<object, symbol>();

// Returns the unique identity of an object.
// Fuck Vue PropertyKey type
export default function id(obj: object): symbol {
  let id = map.get(obj);
  if (id) {
    return id;
  }
  id = Symbol();
  map.set(obj, id);
  return id;
}
