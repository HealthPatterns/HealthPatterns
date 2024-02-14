<script lang="ts">
    import { trackingData, loginData } from '../store.js';
    import { apiSetDetails } from './ApiSetDetails.svelte';

    function updateFood(foodType: string) {
        $trackingData.diet[foodType] = !$trackingData.diet[foodType];
        apiSetDetails($loginData.accessToken, $trackingData.tracking_id, $trackingData.front_regions, $trackingData.back_regions, $trackingData.intensity, $trackingData.diet);
    }

</script>

<div id="Food">
    <button on:click={() => updateFood("Obst")}><span class={$trackingData.diet["Obst"] ? "tag tag-active" : "tag"}>Obst</span></button>
    <button on:click={() => updateFood("Gemüse")}><span class={$trackingData.diet["Gemüse"] ? "tag tag-active" : "tag"}>Gemüse</span></button>
    <button on:click={() => updateFood("Milchprodukte")}><span class={$trackingData.diet["Milchprodukte"] ? "tag tag-active" : "tag"}>Milchprodukte</span></button>
    <button on:click={() => updateFood("Fleisch")}><span class={$trackingData.diet["Fleisch"] ? "tag tag-active" : "tag"}>Fleisch</span></button>
    <button on:click={() => updateFood("Fisch")}><span class={$trackingData.diet["Fisch"] ? "tag tag-active" : "tag"}>Fisch</span></button>
    <button on:click={() => updateFood("Eier")}><span class={$trackingData.diet["Eier"] ? "tag tag-active" : "tag"}>Eier</span></button>
    <button on:click={() => updateFood("Weißmehl")}><span class={$trackingData.diet["Weißmehl"] ? "tag tag-active" : "tag"}>Weißmehl</span></button>
    <button on:click={() => updateFood("Vollkorn")}><span class={$trackingData.diet["Vollkorn"] ? "tag tag-active" : "tag"}>Vollkorn</span></button>
    <button on:click={() => updateFood("Soja")}><span class={$trackingData.diet["Soja"] ? "tag tag-active" : "tag"}>Soja</span></button>
</div>

<style>

#Food {
    display: inline-block;
    width: 100%;
    flex-direction: row;
    height: fit-content;
}

.tag {
    display: inline-block;
    padding: .2em .5em .3em;
    margin: .25em .1em;
    font-size: 1em;
    border-radius: 8px;
    font-weight: 400;
    border: 2px #e6f0f3 solid;
    background-color: #e6f0f3;
}

.tag-active {
    border: 2px #0D698B solid;
    background-color: #fff;
}


</style>