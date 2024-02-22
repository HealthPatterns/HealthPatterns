<script lang="ts">
  import { trackingData, loginData } from '../../store.js';
  import AddDetails from "../../lib/AddDetails.svelte";
  import Loader from "../../lib/Loader.svelte";
  import Timer from "../../lib/Timer.svelte"
  import TrackingCard from '../../lib/TrackingCard.svelte';
  import ErrorCard from '../../lib/ErrorCard.svelte';
  import Header from '../../lib/Header.svelte';

  export let enableTrackingScreen;
  export let enablePreviousTrackingsScreen;
  export let enableMessage;
  export let enableError;
  export let errorMessage;
  let enableAddDetails : boolean = false;
  let timerComponet : Timer;


  function toggleDetails () {
    enableAddDetails = !enableAddDetails;
    enableTrackingScreen = !enableTrackingScreen;
  }
</script>

<main style="background-color: { enableAddDetails ? "#F2F1E8" : "#fff" }">
    {#if enableTrackingScreen}
    <div id="HomeScreen">
        <Header
          bind:enableTrackingScreen={enableTrackingScreen}
          bind:enablePreviousTrackingsScreen={enablePreviousTrackingsScreen}>
        </Header>

        <h1 style="margin-top: 1.4rem;">Guten Morgen {$loginData.username}!</h1>
        <div class="time"> 
            
            <Timer bind:this={timerComponet}></Timer>

        </div>
        
        <div style="display:flex; align-items: center; flex-direction:column; width:100%; margin-top: auto; ">

            {#if $trackingData.isTracking}
            <button class="details-button" on:click={toggleDetails}>Details hinzufügen</button>
            {/if}
            <button on:click={() => {$trackingData.isTracking ? timerComponet.stop_reset() : timerComponet.start()}} class={$trackingData.isTracking ? "tracking-button tracking-active" : "tracking-button"}>
                {#if !$trackingData.isTracking}
                <svg style="margin-right: 0.5rem;" xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-player-play-filled" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                    <path d="M6 4v16a1 1 0 0 0 1.524 .852l13 -8a1 1 0 0 0 0 -1.704l-13 -8a1 1 0 0 0 -1.524 .852z" stroke-width="0" fill="currentColor"></path>
                </svg>
                Schmerz tracken
                {/if}
                {#if $trackingData.isTracking}
                <svg style="margin-right: 0.5rem;" xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-player-stop-filled" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                    <path d="M17 4h-10a3 3 0 0 0 -3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3 -3v-10a3 3 0 0 0 -3 -3z" stroke-width="0" fill="currentColor"></path>
                </svg>
                Tracking beenden
                {/if}
            </button>
        </div>

        <TrackingCard enable={enableMessage}></TrackingCard>
        <ErrorCard enable={enableError} message={errorMessage}></ErrorCard>

    </div>
    {/if}

    <AddDetails on:toggle={toggleDetails} enabled={enableAddDetails}></AddDetails>
    {#if !enableAddDetails && !enableTrackingScreen }
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
  
#HomeScreen {
    display: flex;
    height: 90%;
    width: 80%;
    flex-direction: column;
}

h1 {
    font-size: x-large;
    font-weight: 500;
}

.time {
    display: flex;
    flex: 1;
    font-size: 3.5rem;
    font-weight: 500;
    width: 100%;
    height:auto;
    text-align: center;
    justify-content: center;
    align-items: center;
}

.tracking-button {
    background-color: #0d698b;
    color: #f2f1e8;
    border: 0;
    border-radius: 0.4rem;
    font-size: x-large;
    font-weight: 500;
    padding: 0.5rem;
    width: 100%;
    align-items: center;
    justify-content: center;
    display: flex;
}

.details-button {
    border: 0;
    border-radius: 2rem;
    background-color: #c2d3db;
    font-size: medium;
    margin-bottom: 1.3rem;
    width: fit-content;
    padding: 0.3rem;
    padding-left: 3rem;
    padding-right: 3rem;
    font-size: 0.9rem;
}

.tracking-active {
    background-color: #e34234;
}
</style>