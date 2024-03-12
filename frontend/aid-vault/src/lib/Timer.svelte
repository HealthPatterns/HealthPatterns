<script lang="ts">
  import { onMount, onDestroy } from "svelte";
  import { loginData, trackingData } from '../store.js';
  import { apiStartTracking, apiStopTracking } from './ApiFunctions.ts'

  let hour: number = 0, minute: number = 0, second: number = 0;
  let hrString: string, minString: string, secString: string;

  createStrings();

  const unsubscribe = trackingData.subscribe(() => {
    stopWatch();
  })

  export function start() {
    $trackingData.unixtime = Math.floor(Date.now() / 1000);
    $trackingData.isTracking = true;
    apiStartTracking($loginData.accessToken);
    stopWatch();
  }

  export function stop_reset() {
    $trackingData.isTracking = false;
    apiStopTracking($loginData.accessToken, $trackingData.tracking_id);
    $trackingData.unixtime = Math.floor(Date.now() / 1000);
    hour = 0;
    minute = 0;
    second= 0;
    createStrings();
  }

  function createStrings() {
    hrString = hour < 10 ? "0" + hour.toString() : hour.toString();
    minString = minute < 10 ? "0" + minute.toString() : minute.toString();
    secString = second < 10 ? "0" + second.toString() : second.toString();
  }

  function stopWatch() {

    if ($trackingData.isTracking) {
      const currentTime = Math.floor(Date.now() / 1000);
      let count = currentTime - $trackingData.unixtime;
      hour = Math.floor(count / 3600);
      count -= hour * 3600;
      minute = Math.floor(count / 60);
      second = count - minute * 60;
      createStrings();
      setTimeout(stopWatch, 1000);
    }
  }

  onDestroy(unsubscribe);

</script>

<div class="circle"><p style="font-size: 3rem;">{hrString}:{minString}:{secString}</p></div>

<style>
  .circle {
    background-color: var(--secondary-background-color);
    height: 50%;
    aspect-ratio: 1 / 1;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
