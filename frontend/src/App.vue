<script setup lang="ts">
import Icon from "@/components/common/Icon.vue";
import Logo from "@/components/Logo.vue";
import NavbarItem from "@/components/NavbarItem.vue";
import ToastList from "@/components/ToastList.vue";
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header
    class="fixed left-0 right-0 top-0 z-10 flex h-header-height items-center overflow-x-auto overflow-y-hidden border-b bg-white
      desktop:justify-between desktop:gap-6 desktop:px-6 mobile:gap-4 mobile:px-4"
  >
    <Logo class="flex-none text-6" />
    <div
      class="flex items-center gap-2 rounded-full bg-gray-100 p-2 desktop:absolute desktop:left-1/2 desktop:w-1/3
        desktop:-translate-x-1/2 mobile:flex-1"
    >
      <Icon type="search" class="text-6" />
      <input type="text" class="w-full bg-transparent" />
    </div>
    <Icon type="notifications" class="flex-none text-6" />
  </header>

  <nav
    class="fixed left-0 z-10 flex items-center bg-white desktop:bottom-0 desktop:top-header-height desktop:w-navbar-width
      desktop:flex-col desktop:overflow-y-auto desktop:overflow-x-hidden desktop:border-r mobile:bottom-0 mobile:right-0
      mobile:h-navbar-height mobile:flex-row mobile:overflow-x-auto mobile:overflow-y-hidden mobile:border-t"
  >
    <NavbarItem class="mobile:order-3" href="/" icon="home" title="Home" />
    <NavbarItem class="mobile:order-2" href="/timeline" icon="event_note" title="Timeline" />
    <NavbarItem class="mobile:order-1" href="/statistics" icon="leaderboard" title="Statistics" />
    <NavbarItem class="mobile:order-4" href="/settings" icon="settings" title="Settings" />
    <div class="desktop:flex-1 mobile:hidden"></div>
    <NavbarItem class="desktop:border-t mobile:order-5" href="/account" icon="account_circle" title="Account" />
  </nav>

  <aside class="pointer-events-none fixed right-0 top-header-height z-50 w-screen desktop:max-w-96 mobile:max-w-64">
    <ToastList />
  </aside>

  <div class="pt-header-height desktop:pl-navbar-width mobile:pb-navbar-height">
    <main class="desktop:p-8 mobile:p-4">
      <RouterView />
    </main>
  </div>
</template>
