<script setup lang="ts">
// Mitigates the abrupt size change for block element children
const onBeforeLeave = (el: Element) => {
  const e = el as HTMLElement;
  const { offsetWidth, offsetHeight } = e;
  e.style.width = `${offsetWidth}px`;
  e.style.height = `${offsetHeight}px`;
};
</script>

<template>
  <TransitionGroup tag="div" name="list" class="relative" @before-leave="onBeforeLeave">
    <slot></slot>
  </TransitionGroup>
</template>

<style>
.list-enter-from,
.list-leave-to {
  @apply opacity-0;
  @apply -translate-y-full;
}
.list-enter-to,
.list-leave-from {
  @apply opacity-100;
}
.list-enter-active,
.list-leave-active {
  @apply transition-all;
}
/* Enable list move */
/* https://vuejs.org/guide/built-ins/transition-group.html#move-transitions */
.list-move {
  @apply transition-all;
}
.list-leave-active {
  @apply absolute;
}
</style>
