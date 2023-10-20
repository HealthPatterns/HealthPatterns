<script lang="ts">
    import { createEventDispatcher } from 'svelte'
    const dispatch = createEventDispatcher();

    import BodyForm from "./BodyForm.svelte";
    import Food from "./Food.svelte";
    import Slider from "./Slider.svelte";
    import { trackingData, loginData } from '../store.js';

    export let enabled : boolean;

    function toggle() {
        dispatch('toggle')
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