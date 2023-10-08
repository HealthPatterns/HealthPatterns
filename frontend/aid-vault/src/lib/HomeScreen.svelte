<script lang="ts">
    import { createEventDispatcher } from 'svelte'
    const dispatch = createEventDispatcher();

    import Timer from "./Timer.svelte"
    import ButtomCard from './ButtomCard.svelte';

    export let username : string;
    export let enabled : boolean;
    export let navbarEnabled : boolean;
    
    export let isTracking = false;
    let timerComponet : Timer;

    function toggle() {
        dispatch('toggle')
    }

</script>

{#if enabled}
<div id="HomeScreen">
    <div style="display: flex; width:100%; justify-content:space-between; flex-direction:row; margin-top:1rem">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions-->
        <svg on:click={()=>{navbarEnabled = !navbarEnabled}} xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-menu-2" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
            <path d="M4 6l16 0"></path>
            <path d="M4 12l16 0"></path>
            <path d="M4 18l16 0"></path>
         </svg>
         <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-user-circle" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
            <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"></path>
            <path d="M12 10m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"></path>
            <path d="M6.168 18.849a4 4 0 0 1 3.832 -2.849h4a4 4 0 0 1 3.834 2.855"></path>
         </svg>
    </div>

    <h1 style="margin-top: 1.4rem;">Guten Morgen {username}!</h1>
    <div class="time"> 
        
        <Timer bind:this={timerComponet} bind:isRunning={isTracking}></Timer>

    </div>
    
    <div style="display:flex; align-items: center; flex-direction:column; width:100%; margin-top: auto; ">

        {#if isTracking}
        <button class="details-button" on:click={toggle}>Details hinzufügen</button>
        {/if}
        <button on:click={() => {isTracking ? timerComponet.stop_reset() : timerComponet.start()}} class={isTracking ? "tracking-button tracking-active" : "tracking-button"}>
            {#if !isTracking}
            <svg style="margin-right: 0.5rem;" xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-player-play-filled" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M6 4v16a1 1 0 0 0 1.524 .852l13 -8a1 1 0 0 0 0 -1.704l-13 -8a1 1 0 0 0 -1.524 .852z" stroke-width="0" fill="currentColor"></path>
            </svg>
            Schmerz tracken
            {/if}
            {#if isTracking}
            <svg style="margin-right: 0.5rem;" xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-player-stop-filled" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M17 4h-10a3 3 0 0 0 -3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3 -3v-10a3 3 0 0 0 -3 -3z" stroke-width="0" fill="currentColor"></path>
             </svg>
             Tracking beenden
            {/if}
        </button>
    </div>

    <ButtomCard enable={true}></ButtomCard>

</div>
{/if}

<style>
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