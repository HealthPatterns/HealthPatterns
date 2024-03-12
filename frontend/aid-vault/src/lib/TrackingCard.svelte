<script lang="ts">
  import { trackingData, defaultTrackingData } from '../store.js';
    import AddDetails from "./AddDetails.svelte";
    import "../app.css";
    export let enable : boolean;
    let enableDetails : boolean = false;

    function toggleDetails () {
        enableDetails = !enableDetails;
    }

    function closeCard() {
        $trackingData = structuredClone($defaultTrackingData);
        enable = false;
    }
</script>

{#if enable && !enableDetails}
    <div class="BackgroundFilter">
        <div id="TrackingCard">
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <!-- svelte-ignore a11y-no-static-element-interactions-->
            <div style="width: 100%; display:flex; justify-content:flex-end;"> 
                <svg on:click={closeCard} style="margin-right: 1rem;" xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-x" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                    <path d="M18 6l-12 12"></path>
                    <path d="M6 6l12 12"></path>
                </svg>
            </div>
            <svg width="3rem" height="3rem" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M17 3.34a10 10 0 1 1 -14.995 8.984l-.005 -.324l.005 -.324a10 10 0 0 1 14.995 -8.336zm-1.293 5.953a1 1 0 0 0 -1.32 -.083l-.094 .083l-3.293 3.292l-1.293 -1.292l-.094 -.083a1 1 0 0 0 -1.403 1.403l.083 .094l2 2l.094 .083a1 1 0 0 0 1.226 0l.094 -.083l4 -4l.083 -.094a1 1 0 0 0 -.083 -1.32z" stroke-width="0" fill="#0d698b"></path>
            </svg>
            <p class="card-title">Tracking gespeichert</p>
            <button class="card-button" on:click={toggleDetails}> Details hinzufügen </button>
        </div>
    </div>
{:else if enableDetails}
<div class="BackgroundFilter">
    <div class="details">
        <AddDetails
            on:toggle={toggleDetails}
            enabled={enableDetails}
            bind:front_regions={$trackingData.front_regions}
            bind:back_regions={$trackingData.back_regions}
            bind:intensity={$trackingData.intensity}
            bind:diet={$trackingData.diet}
            bind:tracking_id={$trackingData.tracking_id}
        ></AddDetails>
    </div>
</div>
{/if}


<style>
    .details {
        background-color: #f2f1e8;
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 100%;
    }
    #TrackingCard {
        padding: 2rem;
        background-color: white;
        width: 100%;
        height: 30%;
        position: absolute;
        bottom: 0;
        left: 0;
        display: flex;
        justify-content: center;
        border-radius: 1.2rem 1.2rem 0 0;
        flex-direction: column;
        align-items: center;
    }

    .card-title {
        font-size: larger;
        font-weight: 500;
        margin-bottom: 1.8rem;
        margin-top: 0.5rem;
    }

    .card-button {
        background-color: #e9eff3;
        border-radius: 0.6rem;
        padding: 0.6rem 1.7rem 0.6rem 1.7rem;
        font-weight: 500;
        font-size: 0.9rem;
    }

    
</style>