<script lang="ts">
    import Header from '../../lib/Header.svelte';
    import Loader from '../../lib/Loader.svelte';
    import AddDetails from '../../lib/AddDetails.svelte';
    import { apiGetAllTrackings } from '../../lib/ApiFunctions.ts';
    import { defaultTrackingData, loginData } from '../../store.js';

    export let enablePreviousTrackingsScreen : boolean;
    export let enableTrackingScreen : boolean;
    export let enableSettingsScreen : boolean;
    let trackings = apiGetAllTrackings($loginData.accessToken);
    let enableDetails : boolean = false;
    let front_regions : Array<boolean>;
    let back_regions : Array<boolean>;
    let intensity : number;
    let diet : Array<string>;
    let tracking_id : string;

  function toggleDetails(tracking) {
    enableDetails = !enableDetails;
    tracking_id = tracking.id;
    front_regions = tracking.front_regions || $defaultTrackingData.front_regions;
    back_regions = tracking.back_regions || $defaultTrackingData.back_regions;
    intensity = tracking.intensity || $defaultTrackingData.intensity;
    diet = tracking.diet || $defaultTrackingData.diet;
  }

</script>

<main>
    {#if enablePreviousTrackingsScreen && !enableDetails}
    <div id="PreviousScreen">
        <Header
            bind:enableTrackingScreen={enableTrackingScreen}
            bind:enablePreviousTrackingsScreen={enablePreviousTrackingsScreen}
            bind:enableSettingsScreen={enableSettingsScreen}>
        </Header>
        <h1 style="margin-top: 1.4rem; margin-bottom: 1.4rem">Trackingeinträge</h1>
        {#await trackings}
            <Loader></Loader>
        {:then trackingsData}
          {#if trackingsData === 'NO_TRACKINGS'}
              <p>Es wurde noch kein Tracking gestartet.</p>
          {:else if trackingsData === 'ERROR'}
              <p>Ein Fehler ist aufgetreten.</p>
          {:else}
            {#each trackingsData as tracking}
                <!-- svelte-ignore a11y-click-events-have-key-events -->
                <!-- svelte-ignore a11y-no-static-element-interactions-->
                <div class="row" on:click={() => toggleDetails(tracking)}>
                    <div class="column-item">
                        <div class="date">{new Date(tracking.time_start * 1000).toLocaleDateString()}</div>
                        <div class="time">
                            {new Date(tracking.time_start * 1000).toLocaleTimeString()} bis {new Date(tracking.time_end * 1000).toLocaleTimeString()} Uhr
                        </div>
                        <div class="duration">
                          Dauer {`${Math.floor((tracking.time_end - tracking.time_start) / 3600)}:${Math.floor(((tracking.time_end - tracking.time_start) % 3600) / 60).toString().padStart(2, '0')}:${((tracking.time_end - tracking.time_start) % 60).toString().padStart(2, '0')}`}
                        </div>
                    </div>
                    <div class="column-button">
                      <svg xmlns="http://www.w3.org/2000/svg"  width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="#cccccc" fill="none" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M7.82054 20.7313C8.21107 21.1218 8.84423 21.1218 9.23476 20.7313L15.8792 14.0868C17.0505 12.9155 17.0508 11.0167 15.88 9.84497L9.3097 3.26958C8.91918 2.87905 8.28601 2.87905 7.89549 3.26958C7.50497 3.6601 7.50497 4.29327 7.89549 4.68379L14.4675 11.2558C14.8581 11.6464 14.8581 12.2795 14.4675 12.67L7.82054 19.317C7.43002 19.7076 7.43002 20.3407 7.82054 20.7313Z"></path>
                      </svg>
                    </div>
                </div>
            {/each}
          {/if}
        {/await}
    </div>
    {:else if enableDetails}
    <div class="details">
      <AddDetails 
          on:toggle={toggleDetails}
          enabled={enableDetails}
          bind:front_regions={front_regions}
          bind:back_regions={back_regions}
          bind:intensity={intensity}
          bind:diet={diet}
          bind:tracking_id={tracking_id}
      ></AddDetails>
    </div>
    {:else}
        <Loader></Loader>
    {/if}
</main>
  
<style>
  main {
      display: flex;
      height: 100%;
      width: 100%;
      font-family: 'Montserrat';
      align-items: center;
      justify-content: center;
      background-color: #fff;
      position: relative;
  }
  .details {
      background-color: #f2f1e8;
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      height: 100%;
  }
  #PreviousScreen {
    display: flex;
    height: 90%;
    width: 80%;
    flex-direction: column;
    }

  h1 {
    font-size: x-large;
    font-weight: 500;
  }

  .row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    border-bottom: 1px solid #ccc;
  }

  .column-item {
    display: flex;
    flex-direction: column;
  }

  .column-button {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    justify-content: center;
  }

  .date {
    font-size: x-large;
  }

  p {
    text-align: center;
    margin: auto;
  }
</style>