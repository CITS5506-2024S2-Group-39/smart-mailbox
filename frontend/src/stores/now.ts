import { shallowRef } from "vue";

const now = shallowRef(new Date());

setInterval(() => {
  now.value = new Date();
}, 1000);

export default now;
