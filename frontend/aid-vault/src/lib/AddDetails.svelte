<script lang="ts">
    import { apiSetDetails } from './ApiFunctions.ts';
    import { loginData } from '../store.js';
    import { createEventDispatcher } from 'svelte'
    const dispatch = createEventDispatcher();

    import BodyForm from "./BodyForm.svelte";
    import Food from "./Food.svelte";
    import Slider from "./Slider.svelte";

    export let enabled : boolean;
    export let back_regions : Array<boolean>;
    export let front_regions : Array<boolean>;
    export let intensity : number;
    export let diet : Array<string>;
    export let tracking_id : string;

    function toggle() {
        dispatch('toggle')
    }

    function setDetails() {
        apiSetDetails ($loginData.accessToken, tracking_id, front_regions, back_regions, intensity, diet);
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
            <BodyForm
                on:setDetails={setDetails}
                bind:back_regions={back_regions}
                bind:front_regions={front_regions}
            ></BodyForm>
        </div>

        <div class="background-container">
            <h2>Intensität</h2>
            <Slider
                on:setDetails={setDetails}
                bind:intensity={intensity}
            ></Slider>
        </div>
        
        <div style="margin-bottom: 0.2rem;" class="background-container">
            <h2>Ernährung</h2>
            <Food
                on:setDetails={setDetails}
                bind:diet={diet}
            ></Food>
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