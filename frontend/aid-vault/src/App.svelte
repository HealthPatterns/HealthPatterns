<script lang="ts">
  import AddDetails from "./lib/AddDetails.svelte";
  import HomeScreen from "./lib/HomeScreen.svelte";
  import "./font.css"

  let enableAddDetails = true;
  let enableHomeScreen = false;
</script>

<main style="background-color: {enableAddDetails ? "#F2F1E8" : "#fff" }">
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
    background-color: #fff;
  }
</style>
