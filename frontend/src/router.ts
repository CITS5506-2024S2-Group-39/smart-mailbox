import AccountView from "@/views/AccountView.vue";
import EventView from "@/views/EventView.vue";
import HomeView from "@/views/HomeView.vue";
import SettingsView from "@/views/SettingsView.vue";
import StatisticsView from "@/views/StatisticsView.vue";
import TimelineView from "@/views/TimelineView.vue";
import { createRouter, createWebHistory } from "vue-router";
import type { NavigationGuardWithThis, RouterScrollBehavior } from "vue-router";

const routes = [
  { path: "/", component: HomeView },
  { path: "/timeline", component: TimelineView },
  { path: "/statistics", component: StatisticsView },
  { path: "/settings", component: SettingsView },
  { path: "/account", component: AccountView },
  { path: "/event/:id", component: EventView },
];

// Stores scrollY values for different router views
const scrolls = new Map<string, number>();

for (const { path } of routes) {
  // Remember scroll position for generic routes
  if (path.indexOf(":") < 0) {
    // 0 means uninitialized
    scrolls.set(path, 0);
  }
}

const saveScroll: NavigationGuardWithThis<undefined> = (to, from, next) => {
  const path = from.path;

  // Remember scroll position if needed
  if (scrolls.has(path)) {
    const { scrollY } = window;
    scrolls.set(path, scrollY);
    console.log(scrolls);
  }

  next();
};

const restoreScroll: RouterScrollBehavior = (to, from, savedPosition) => {
  // If has browser-saved position, always use the value
  if (savedPosition) {
    return savedPosition;
  }

  // If has an anchor, scroll to the corresponding element
  if (to.hash) {
    return {
      behavior: "smooth",
      el: to.hash,
    };
  }

  // Use saved scroll position if it is available
  const scrollY = scrolls.get(to.path);
  if (scrollY) {
    return {
      behavior: "instant",
      top: scrollY,
    };
  }
};

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior: restoreScroll,
});

router.beforeEach(saveScroll);

export default router;
