<script lang="ts">
  import AddDetails from "../../lib/AddDetails.svelte";
  import HomeScreen from "../../lib/HomeScreen.svelte";
  import Navbar from "../../lib/Navbar.svelte";
  import Loader from "../../lib/Loader.svelte";

  export let enableTrackingScreen;
  export let enableMessage;
  export let enableError;
  export let errorMessage;
  let enableAddDetails : boolean = false;
  let enableNavbar : boolean = false;


  function toggleDetails () {
    enableAddDetails = !enableAddDetails;
    enableTrackingScreen = !enableTrackingScreen;
  }
</script>

<main style="background-color: { enableAddDetails ? "#F2F1E8" : "#fff" }">
    <Navbar bind:enable={enableNavbar}></Navbar>

    <HomeScreen 
        bind:enableMessage={enableMessage} 
        on:toggle={toggleDetails} 
        bind:navbarEnabled={enableNavbar} 
        enabled={enableTrackingScreen} 
        bind:enableError={enableError} 
        errorMessage={errorMessage}>
    </HomeScreen>

    <AddDetails on:toggle={toggleDetails} enabled={enableAddDetails}></AddDetails>
    {#if !enableAddDetails && !enableTrackingScreen }
      <Loader></Loader>
    {/if}
</main>
  
<style>
  main {
      display: flex;
      height: 100%;
      width: 100%;
      font-family: 'Montserrat';
      align-items: center;
      justify-content: center;
      background-color: #fff;
      position: relative;
  }
</style>