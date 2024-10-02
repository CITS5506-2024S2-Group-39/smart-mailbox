import AccountView from "@/views/AccountView.vue";
import EventView from "@/views/EventView.vue";
import HomeView from "@/views/HomeView.vue";
import SettingsView from "@/views/SettingsView.vue";
import StatisticsView from "@/views/StatisticsView.vue";
import TimelineView from "@/views/TimelineView.vue";
import { createRouter, createWebHistory } from "vue-router";

export default createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", component: HomeView },
    { path: "/timeline", component: TimelineView },
    { path: "/event/:id", component: EventView },
    { path: "/statistics", component: StatisticsView },
    { path: "/settings", component: SettingsView },
    { path: "/account", component: AccountView },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: "smooth",
      };
    }
  },
});
