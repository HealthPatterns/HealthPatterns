<script lang="ts">
    import { createEventDispatcher } from 'svelte'
    const dispatch = createEventDispatcher();

    import BodyForm from "./BodyForm.svelte";
    import Food from "./Food.svelte";
    import Slider from "./Slider.svelte";
    import { trackingData } from '../store.js';
    import { loginData } from '../store.js';

    export let enabled : boolean;

    function toggle() {
        dispatch('toggle')
        apiSetDetails ($loginData.accessToken, $trackingData.tracking_id, $trackingData.front_regions, $trackingData.back_regions, $trackingData.intensity, $trackingData.diet)
    }

    async function apiGetDetails (api_token : string, tracking_id : string) {
    const url = `http://localhost:3000/trackings/tracking/details?tracking_id=${tracking_id}`;

    const options = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
      }
    };

    try {
      const response = await fetch(url, options);
      const statusCode = response.status;
      if (statusCode === 200) {
        console.log("API call 'GetDetails' successful.");
        const data = await response.json();
        return data;
      } else {
        console.log("Error during API call 'GetDetails'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function apiSetDetails (api_token : string, tracking_id : string, front_regions, back_regions, intensity, diet) {
    const url = `http://localhost:3000/trackings/${tracking_id}/details`;

    const options = {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
      },
      body: JSON.stringify({
        'front_regions': [
          front_regions
        ],
        'back_regions': [
          back_regions
        ],
        'intensity': intensity,
        'diet': diet
      })
    };

    try {
      const response = await fetch(url, options);
      const statusCode = response.status;
      if (statusCode === 200) {
        console.log("API call 'SetDetails' successful.");
      } else {
        console.log("Error during API call 'SetDetails'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

</script>

{#if enabled}
    <div id="AddDetails">
        <div style="display: flex; width:100%; margin-top: 2rem; justify-content:end;">
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <!-- svelte-ignore a11y-no-static-element-interactions-->
            <svg on:click={toggle} style="margin-right: 1rem;" xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-x" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M18 6l-12 12"></path>
                <path d="M6 6l12 12"></path>
             </svg>
        </div>
        <h1 style="margin-top: 1rem;">Details hinzufügen</h1>
        <div class="background-container" style="height: 70%;">
            <h2>Körperregionen</h2>
            <BodyForm></BodyForm>
        </div>

        <div class="background-container">
            <h2>Intensität</h2>
            <Slider></Slider>
        </div>
        
        <div style="margin-bottom: 0.2rem;" class="background-container">
            <h2>Ernährung</h2>
            <Food></Food>
        </div>
    </div>
{/if}

<style>

#AddDetails {
    display: flex;
    height: 98%;
    width: 95%;
    flex-direction: column;
    overflow: scroll;
    border-radius: 0.2rem;
}

h1 {
    font-size: x-large;
    font-weight: 500;
    margin-bottom: 0.6em;
}

h2 {
    font-size: large;
    font-weight: 500;
}

.background-container {
    background-color: #fff;
    margin-bottom: 0.6rem;
    border-radius: 0.2rem;
    padding: 0.5rem;
}

</style>