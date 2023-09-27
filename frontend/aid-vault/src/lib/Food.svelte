<script lang="ts">
    import BodyForm from "./BodyForm.svelte";

    var foodActive = [false,false,false,false,false,false,false,false,false];

    function isActive(index:number) {
        if (foodActive[index]) {
            return " tag-active"
        }
        return ""
    }

</script>

<div id="Food">
    <button on:click={() => foodActive[0] = !foodActive[0]}><span class={foodActive[0] ? "tag tag-active" : "tag"}>Obst</span></button>
    <button on:click={() => foodActive[1] = !foodActive[1]}><span class={foodActive[1] ? "tag tag-active" : "tag"}>Gemüse</span></button>
    <button on:click={() => foodActive[2] = !foodActive[2]}><span class={foodActive[2] ? "tag tag-active" : "tag"}>Milchprodukte</span></button>
    <button on:click={() => foodActive[3] = !foodActive[3]}><span class={foodActive[3] ? "tag tag-active" : "tag"}>Fleisch</span></button>
    <button on:click={() => foodActive[4] = !foodActive[4]}><span class={foodActive[4] ? "tag tag-active" : "tag"}>Fisch</span></button>
    <button on:click={() => foodActive[5] = !foodActive[5]}><span class={foodActive[5] ? "tag tag-active" : "tag"}>Eier</span></button>
    <button on:click={() => foodActive[6] = !foodActive[6]}><span class={foodActive[6] ? "tag tag-active" : "tag"}>Weißmehl</span></button>
    <button on:click={() => foodActive[7] = !foodActive[7]}><span class={foodActive[7] ? "tag tag-active" : "tag"}>Vollkorn</span></button>
    <button on:click={() => foodActive[8] = !foodActive[8]}><span class={foodActive[8] ? "tag tag-active" : "tag"}>Soja</span></button>
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