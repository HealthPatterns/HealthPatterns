<script lang="ts">
    export let enable : boolean;

    

</script>

{#if enable}
    <div id="Navbar">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions-->
        <div style="width: 100%; display:flex; justify-content:flex-start; padding:1.5rem;"> 
            <svg on:click={() => {enable = !enable}} style="margin-right: 1rem;" xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-x" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M18 6l-12 12"></path>
                <path d="M6 6l12 12"></path>
            </svg>
        </div>
        <div style="display: flex; flex-direction:column;">
            <button class="navbutton">Schmerztracking</button>
            <button class="navbutton">Analyse</button>
            <button class="navbutton">Daten exportieren</button>
            <button class="navbutton">Einstellungen</button>
        </div>
    </div>
{/if}

<style>
    #Navbar {
        background-color: white;
        width: 80%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
    }

    .navbutton{
        text-align: left;
        margin-left: 1.5rem;
        font-size: x-large;
    } 
</style>