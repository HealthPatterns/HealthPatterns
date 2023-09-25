<script lang="ts">
  import AddDetails from "./lib/AddDetails.svelte";
  import HomeScreen from "./lib/HomeScreen.svelte";
  import "./font.css"

  let enableAddDetails = false;
  let enableHomeScreen = true;
</script>

<main>
  {#if enableHomeScreen}
  <HomeScreen></HomeScreen>
  {/if}
  {#if enableAddDetails}
  <AddDetails ></AddDetails>
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
  }
</style>
