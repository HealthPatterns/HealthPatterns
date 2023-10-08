<script lang="ts">
  import AddDetails from "./lib/AddDetails.svelte";
  import HomeScreen from "./lib/HomeScreen.svelte";
  import Navbar from "./lib/Navbar.svelte";
  import "./font.css"

  let username = "Finn";
  let isTracking = false;

  let enableAddDetails = false;
  let enableHomeScreen = true;
  let enableNavbar = false;

  // Speichern der Tracking 
  // Speichern des Nutzers ( Cookie )
  // Exception Handler

  function toggleDetails () {
    enableAddDetails = !enableAddDetails;
    enableHomeScreen = !enableHomeScreen;
    console.log(isTracking);
  }

</script>

<main style="background-color: { enableAddDetails ? "#F2F1E8" : "#fff" }">
  <Navbar bind:enable={enableNavbar}></Navbar>
  <HomeScreen on:toggle={toggleDetails} bind:navbarEnabled={enableNavbar} bind:isTracking={isTracking} enabled={enableHomeScreen} username={username}></HomeScreen>
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
    position: relative;
}

</style>
