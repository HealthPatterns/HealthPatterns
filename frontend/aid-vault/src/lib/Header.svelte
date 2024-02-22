<script lang="ts">
    import Navbar from "./Navbar.svelte";
    let enableNavbar : boolean = false;
    export let enableTrackingScreen : boolean;
    export let enablePreviousTrackingsScreen : boolean;
</script>

<Navbar 
    bind:enable={enableNavbar}
    bind:enableTrackingScreen={enableTrackingScreen}
    bind:enablePreviousTrackingsScreen={enablePreviousTrackingsScreen}>
</Navbar>
<div style="display: flex; width:100%; justify-content:space-between; flex-direction:row; margin-top:1rem">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions-->
    <svg on:click={()=>{enableNavbar = !enableNavbar}} xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-menu-2" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M4 6l16 0"></path>
        <path d="M4 12l16 0"></path>
        <path d="M4 18l16 0"></path>
    </svg>
    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-user-circle" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"></path>
        <path d="M12 10m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0"></path>
        <path d="M6.168 18.849a4 4 0 0 1 3.832 -2.849h4a4 4 0 0 1 3.834 2.855"></path>
    </svg>
</div>

<style></style>