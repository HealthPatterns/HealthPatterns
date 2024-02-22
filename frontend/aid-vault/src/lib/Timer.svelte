<script lang="ts">
  import { onMount } from "svelte";
  import { loginData, trackingData, defaultTrackingData } from '../store.js';
  import { writable } from 'svelte/store';
  
  let hour: number = 0, minute: number = 0, second: number = 0;
  let hrString: string, minString: string, secString: string;

  createStrings();

  onMount(() => {
    if ($trackingData.isTracking) {
      stopWatch();
    }
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
    $trackingData = structuredClone($defaultTrackingData);
    $trackingData.unixtime = Math.floor(Date.now() / 1000);
    $trackingData.count = hour = minute = second = 0;
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
      $trackingData.count = currentTime - $trackingData.unixtime;
      hour = Math.floor($trackingData.count / 3600);
      $trackingData.count -= hour * 3600;
      minute = Math.floor($trackingData.count / 60);
      second = $trackingData.count - minute * 60;
      createStrings();

      setTimeout(stopWatch, 1000);
    }
  }

  async function apiStartTracking(api_token: string) {
    const current_time = Math.floor(Date.now() / 1000);
    const url = "https://localhost/api/trackings";

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
      },
      body: JSON.stringify({
        'time_start': current_time
      })
    };

    try {
      const response = await fetch(url, options);
      const statusCode = response.status;
      if (statusCode === 201) {
        console.log("API call 'StartTracking' successful.");
        const data = await response.json();
        $trackingData.tracking_id = data.id;
      } else {
        console.log("Error during API call 'StartTracking'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function apiStopTracking(api_token: string, tracking_id: string) {
    const current_time = Math.floor(Date.now() / 1000);
    const url = `https://localhost/api/trackings/${tracking_id}`;

    const options = {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
      },
      body: JSON.stringify({
        'time_end': current_time
      })
    };

    try {
      const response = await fetch(url, options);
      const statusCode = response.status;
      if (statusCode === 200) {
        console.log("API call 'StopTracking' successful.");
      } else {
        console.log("Error during API call 'StopTracking'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }
</script>

<div class="circle"><p style="font-size: 3rem;">{hrString}:{minString}:{secString}</p></div>

<style>
  .circle {
    background-color: #F2F1E8;
    height: 50%;
    aspect-ratio: 1 / 1;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
