<script lang="ts">
    import BodyForm from "./BodyForm.svelte";

    var foodActive = [false,false,false,false,false,false,false,false,false];

    function isActive(index:number) {
        if (foodActive[index]) {
            return " tag-active"
        }
    }

    function changeActive (index:number) {
        foodActive[index] = foodActive[index] ? false : true;
    }

</script>

<div id="Food">
    <button on:click={() => {changeActive(0)}}><span class={"tag"+ isActive(0)}>Obst</span></button>
    <button on:click={() => {changeActive(1)}}><span class={"tag"+ isActive(1)}>Gemüse</span></button>
    <button on:click={() => {changeActive(2)}}><span class={"tag"+ isActive(2)}>Milchprodukte</span></button>
    <button on:click={() => {changeActive(3)}}><span class={"tag"+ isActive(3)}>Fleisch</span></button>
    <button on:click={() => {changeActive(4)}}><span class={"tag"+ isActive(4)}>Fisch</span></button>
    <button on:click={() => {changeActive(5)}}><span class={"tag"+ isActive(5)}>Eier</span></button>
    <button on:click={() => {changeActive(6)}}><span class={"tag"+ isActive(6)}>Weißmehl</span></button>
    <button on:click={() => {changeActive(7)}}><span class={"tag"+ isActive(7)}>Vollkorn</span></button>
    <button on:click={() => {changeActive(8)}}><span class={"tag"+ isActive(8)}>Soja</span></button>
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