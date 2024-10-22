<script setup lang="ts">
import Icon from "@/components/common/Icon.vue";
import Logo from "@/components/Logo.vue";
import NavbarItem from "@/components/NavbarItem.vue";
import ToastList from "@/components/ToastList.vue";
import { RouterView } from "vue-router";
</script>

<template>
  <header
    class="fixed inset-x-0 top-0 z-20 flex h-header-height items-center justify-between gap-std overflow-x-auto bg-neutral-900
      px-std text-white"
  >
    <Logo class="text-6" />
    <Icon type="notifications" class="text-6" />
  </header>
  <nav
    class="fixed bottom-0 left-0 z-10 flex items-center bg-neutral-900 text-white desktop:top-header-height desktop:w-navbar-width
      desktop:flex-col desktop:overflow-y-auto mobile:right-0 mobile:h-navbar-height mobile:flex-row mobile:gap-std
      mobile:overflow-x-auto mobile:px-std"
  >
    <div class="w-full border-b border-neutral-800 mobile:hidden"></div>
    <NavbarItem class="mobile:order-3" href="/" icon="home" title="Home" />
    <NavbarItem class="mobile:order-2" href="/timeline" icon="event_note" title="Timeline" />
    <NavbarItem class="mobile:order-1" href="/statistics" icon="leaderboard" title="Statistics" />
    <NavbarItem class="mobile:order-4" href="/settings" icon="settings" title="Settings" />
    <div class="w-full flex-1 border-b border-neutral-800 mobile:hidden"></div>
    <NavbarItem class="mobile:order-5" href="/account" icon="account_circle" title="Account" />
  </nav>
  <ToastList />
  <main
    class="min-h-screen bg-neutral-100 pt-header-height text-neutral-900 desktop:pl-navbar-width mobile:pb-navbar-height"
  >
    <RouterView v-slot="{ Component }">
      <KeepAlive :include="['HomeView', 'StatisticsView', 'TimelineView']">
        <component :is="Component" :key="$route.fullPath"></component>
      </KeepAlive>
    </RouterView>
  </main>
</template>
