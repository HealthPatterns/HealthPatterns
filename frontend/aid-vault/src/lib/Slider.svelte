<script>
    import { trackingData, loginData } from '../store.js';
    import { apiSetDetails } from './ApiFunctions.js';

    function updateIntensity() {
        apiSetDetails ($loginData.accessToken, $trackingData.tracking_id, $trackingData.front_regions, $trackingData.back_regions, $trackingData.intensity, $trackingData.diet)
    }

</script>

<div id="Slider">
    <input type="range" min="1" max="10" bind:value={$trackingData.intensity} on:input={updateIntensity} class="slider" id="myRange">
</div>

<style>
    #Slider {
        display: flex;
        width: 100%;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* The slider itself */
    .slider {
    -webkit-appearance: none;  /* Override default CSS styles */
    appearance: none;
    width: 100%; /* Full-width */
    height: 2px; /* Specified height */
    background: #0D698B;
    outline: none; /* Remove outline */
    opacity: 0.7; /* Set transparency (for mouse-over effects on hover) */
    -webkit-transition: .2s; /* 0.2 seconds transition on hover */
    transition: opacity .2s;
    }

    /* Mouse-over effects */
    .slider:hover {
    opacity: 1; /* Fully shown on mouse-over */
    }

    /* The slider handle (use -webkit- (Chrome, Opera, Safari, Edge) and -moz- (Firefox) to override default look) */
    .slider::-webkit-slider-thumb {
    -webkit-appearance: none; /* Override default look */
    appearance: none;
    width: 10px; /* Set a specific slider handle width */
    height: 10px; /* Slider handle height */
    background: #0D698B; /* Green background */
    cursor: pointer; /* Cursor on hover */
    border-radius: 25px;
    }

    .slider::-moz-range-thumb {
    border-radius: 25px;
    width: 10px; /* Set a specific slider handle width */
    height: 10px; /* Slider handle height */
    background: #0D698B; /* Green background */
    cursor: pointer; /* Cursor on hover */
    }

</style>