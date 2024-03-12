<script lang="ts">
    import LogoutButton from "./LogoutButton.svelte";
    import "../app.css"

    export let enable : boolean;
    export let enableTrackingScreen : boolean;
    export let enablePreviousTrackingsScreen : boolean;

    function toggleTrackingScreen() {
        enable = false;
        enableTrackingScreen = true;
        enablePreviousTrackingsScreen = false;
    }

    function togglePreviousTrackingsScreen() {
        enable = false;
        enablePreviousTrackingsScreen = true;
        enableTrackingScreen = false;
    }

</script>

{#if enable}
    <div class="BackgroundFilter">
        <div id="Navbar">
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <!-- svelte-ignore a11y-no-static-element-interactions-->
            <div style="width: 100%; display:flex; justify-content:flex-start; padding:1.5rem; margin-top: 1rem"> 
                <svg on:click={() => {enable = !enable}} style="margin-right: 1rem;" xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-x" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                    <path d="M18 6l-12 12"></path>
                    <path d="M6 6l12 12"></path>
                </svg>
            </div>
            <div style="display: flex; flex-direction:column;">
                <button class="navbutton" on:click={toggleTrackingScreen}>Schmerztracking</button>
                <button class="navbutton" on:click={togglePreviousTrackingsScreen}>Trackingeinträge</button>
                <button class="navbutton">Analyse</button>
                <button class="navbutton">Daten exportieren</button>
                <button class="navbutton">Einstellungen</button>
            </div>
            <div id="lower-button">
                <LogoutButton></LogoutButton>
            </div>
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
    #lower-button {
        position: absolute;
        bottom: 2.5rem;
        width: 80%;
        margin-left: auto;
        margin-right: auto;
        left: 0;
        right: 0;
    }
</style>