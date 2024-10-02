type Primitive = string | number | boolean;

export default function arrayEqual<T extends Primitive>(a: T[], b: T[]): boolean {
  const m = a.length;
  const n = b.length;
  if (m !== n) {
    return false;
  }
  for (let i = 0; i < m; ++i) {
    if (a[i] !== b[i]) {
      return false;
    }
  }
  return true;
}
