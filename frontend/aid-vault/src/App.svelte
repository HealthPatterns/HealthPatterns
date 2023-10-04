<script lang="ts">
  import AddDetails from "./lib/AddDetails.svelte";
  import HomeScreen from "./lib/HomeScreen.svelte";
  import "./font.css"

  let username = "Finn";

  let enableAddDetails = false;
  let enableHomeScreen = true;

  function toggleDetails () {
    enableAddDetails = !enableAddDetails;
    enableHomeScreen = !enableHomeScreen;
  }

</script>

<main style="background-color: {enableAddDetails ? "#F2F1E8" : "#fff" }">
  <HomeScreen on:toggle={toggleDetails} enabled={enableHomeScreen} username={username} ></HomeScreen>
  <AddDetails on:toggle={toggleDetails} enabled={enableAddDetails}></AddDetails>
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
