<script lang="ts">
    import BodyForm from "./BodyForm.svelte";
</script>

<div id="Food">
    <button><span class="tag">Obst</span></button>
    <button><span class="tag">Gemüse</span></button>
    <button><span class="tag">Milchprodukte</span></button>
    <button><span class="tag">Fleisch</span></button>
    <button><span class="tag">Fisch</span></button>
    <button><span class="tag">Eier</span></button>
    <button><span class="tag">Weißmehl</span></button>
    <button><span class="tag">Vollkorn</span></button>
    <button><span class="tag">Soja</span></button>
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
}

.tag-active {
    border: 2px #0D698B solid;
}


</style>