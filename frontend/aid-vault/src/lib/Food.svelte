<script lang="ts">
    import { createEventDispatcher } from 'svelte'
    const dispatch = createEventDispatcher();

    export let diet: Array<string>;

    function updateFood(foodType: string) {
        diet[foodType] = !diet[foodType];
        dispatch('setDetails')
    }
</script>

<div id="Food">
    <button on:click={() => updateFood("Obst")}><span class={diet["Obst"] ? "tag tag-active" : "tag"}>Obst</span></button>
    <button on:click={() => updateFood("Gemüse")}><span class={diet["Gemüse"] ? "tag tag-active" : "tag"}>Gemüse</span></button>
    <button on:click={() => updateFood("Milchprodukte")}><span class={diet["Milchprodukte"] ? "tag tag-active" : "tag"}>Milchprodukte</span></button>
    <button on:click={() => updateFood("Fleisch")}><span class={diet["Fleisch"] ? "tag tag-active" : "tag"}>Fleisch</span></button>
    <button on:click={() => updateFood("Fisch")}><span class={diet["Fisch"] ? "tag tag-active" : "tag"}>Fisch</span></button>
    <button on:click={() => updateFood("Eier")}><span class={diet["Eier"] ? "tag tag-active" : "tag"}>Eier</span></button>
    <button on:click={() => updateFood("Weißmehl")}><span class={diet["Weißmehl"] ? "tag tag-active" : "tag"}>Weißmehl</span></button>
    <button on:click={() => updateFood("Vollkorn")}><span class={diet["Vollkorn"] ? "tag tag-active" : "tag"}>Vollkorn</span></button>
    <button on:click={() => updateFood("Soja")}><span class={diet["Soja"] ? "tag tag-active" : "tag"}>Soja</span></button>
</div>

<style>

#Food {
    display: inline-block;
    width: 100%;
    flex-direction: row;
    height: fit-content;
}

button {
    background-color: var(--primary-background-color);
}

.tag {
    display: inline-block;
    padding: .2em .5em .3em;
    margin: .25em .1em;
    font-size: 1em;
    border-radius: 8px;
    font-weight: 400;
    border: 2px #e6f0f3 solid;
    background-color: var(--primary-25-color);
}

.tag-active {
    border: 2px var(--primary-100-color) solid;
    background-color: var(--primary-background-color);
}


</style>