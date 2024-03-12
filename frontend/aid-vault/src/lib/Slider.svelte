<script lang="ts">
    import { createEventDispatcher } from 'svelte'
    const dispatch = createEventDispatcher();

    export let intensity : number;

    function updateIntensity() {
        dispatch('setDetails')
    }
</script>

<div id="Slider">
    <input type="range" min="1" max="10" bind:value={intensity} on:input={updateIntensity} class="slider" id="myRange">
</div>

<style>
    #Slider {
        display: flex;
        width: 100%;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .slider {
    -webkit-appearance: none;
    appearance: none;
    width: 100%;
    height: 2px;
    background: var(--primary-100-color);
    outline: none;
    opacity: 0.7;
    -webkit-transition: .2s;
    transition: opacity .2s;
    }

    .slider:hover {
    opacity: 1;
    }

    .slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 10px;
    height: 10px;
    background: var(--primary-100-color);
    cursor: pointer;
    border-radius: 25px;
    }

    .slider::-moz-range-thumb {
    border-radius: 25px;
    width: 10px;
    height: 10px;
    background: var(--primary-100-color);
    cursor: pointer;
    }

</style>