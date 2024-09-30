<template>
  <a href="/" class="group relative inline-block h-[1.25em] px-[.5em]">
    <div class="font-logo leading-normal">
      <span class="font-bold">Mail</span>
      <span>Sense</span>
    </div>
    <div class="absolute left-[-0.125em] top-[-0.0625em]">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="size-[1em] -rotate-45"
        viewBox="0 -960 960 960"
        fill="currentColor"
      >
        <path
          class="mailbox-body"
          d="M240-560h-80v400h640v-400H400v-80h400q33 0 56.5 23.5T880-560v400q0 33-23.5 56.5T800-80H160q-33 0-56.5-23.5T80-160v-400q0-33 23.5-56.5T160-640h80Z"
        />
        <path class="mailbox-flag" d="M240-480v-160-240h320v160H320v320h-80Z" />
      </svg>
    </div>
    <div class="absolute right-[-0.0625em] top-[-0.0625em]">
      <svg class="size-[1em] rotate-45" xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960" fill="currentColor">
        <path
          class="outer-circle"
          d="M204-150q-57-55-90.5-129.5T80-440q0-83 31.5-156T197-723q54-54 127-85.5T480-840q83 0 156 31.5T763-723q54 54 85.5 127T880-440q0 86-33.5 161T756-150l-56-56q46-44 73-104.5T800-440q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 69 27 129t74 104l-57 57Z"
        />
        <path
          class="inner-circle"
          d="M317-263q-35-33-56-78.5T240-440q0-100 70-170t170-70q100 0 170 70t70 170q0 53-21 99t-56 78l-57-57q25-23 39.5-54t14.5-66q0-66-47-113t-113-47q-66 0-113 47t-47 113q0 36 14.5 66.5T374-320l-57 57Z"
        />
        <path
          d="M480-360q-33 0-56.5-23.5T400-440q0-33 23.5-56.5T480-520q33 0 56.5 23.5T560-440q0 33-23.5 56.5T480-360Z"
        />
      </svg>
    </div>
  </a>
</template>

<style>
@font-face {
  /* https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap */
  font-family: "Open Sans";
  src: url(https://fonts.gstatic.com/s/opensans/v40/memvYaGs126MiZpBA-UvWbX2vVnXBbObj2OVTS-muw.woff2) format("woff2");
  font-display: block;
}
.font-logo {
  font-family: "Open Sans";
}
@keyframes mailboxBodyAnimation {
  0%,
  100% {
    transform: rotate(0deg);
  }
  50% {
    transform: rotate(-3deg);
  }
}
@keyframes mailboxFlagAnimation {
  0%,
  100% {
    transform: rotate(0deg);
  }
  50% {
    transform: rotate(3deg);
  }
}
.group:hover .mailbox-body {
  animation: mailboxBodyAnimation 0.5s infinite;
}
.group:hover .mailbox-flag {
  animation: mailboxFlagAnimation 0.5s infinite;
}
@keyframes innerCircleAnimation {
  0%,
  25% {
    opacity: 0;
  }
  26%,
  100% {
    opacity: 1;
  }
}
@keyframes outerCircleAnimation {
  0%,
  66% {
    opacity: 0;
  }
  67%,
  100% {
    opacity: 1;
  }
}
.group:hover .inner-circle,
.group:focus-visible .inner-circle {
  animation: innerCircleAnimation 0.5s infinite;
}
.group:hover .outer-circle,
.group:focus-visible .outer-circle {
  animation: outerCircleAnimation 0.5s infinite;
}
</style>
