import App from "./App.vue";
import "./main.css";
import router from "./routes";
import { createApp } from "vue";

const app = createApp(App);
app.use(router);
app.mount("#app");
