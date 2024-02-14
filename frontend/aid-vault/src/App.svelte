<script lang="ts">
  import AddDetails from "./lib/AddDetails.svelte";
  import HomeScreen from "./lib/HomeScreen.svelte";
  import Navbar from "./lib/Navbar.svelte";
  import { onMount } from "svelte";
  import Loader from "./lib/Loader.svelte";
  import { apiLogin, apiGetUsername, apiGetActiveTracking, apiGetDetails }  from "./lib/ApiFunctions";
  import "./font.css"
  import { loginData, trackingData } from './store.js';

  let enableAddDetails : boolean = false, enableHomeScreen : boolean = false, enableNavbar : boolean = false;
  
  let enableMessage :boolean = false, enableError : boolean, errorMessage : string;

  function toggleDetails () {
    enableAddDetails = !enableAddDetails;
    enableHomeScreen = !enableHomeScreen;
  }

  async function fetchData() {
    try {
      await apiLogin("admin", "admin"); //Testdata
      await apiGetUsername($loginData.accessToken);
      await apiGetActiveTracking($loginData.accessToken);
      if ($trackingData.isTracking){
        apiGetDetails ($loginData.accessToken, $trackingData.tracking_id)
      }
    } catch (error) {
      console.error("Error fetchData:", error);
    }
  }

  onMount(() => {
      fetchData().then(() => {
        enableHomeScreen = true;
      });
	});

</script>

<main style="background-color: { enableAddDetails ? "#F2F1E8" : "#fff" }">
  <Navbar bind:enable={enableNavbar}></Navbar>
  
  <HomeScreen 
    bind:enableMessage={enableMessage} 
    on:toggle={toggleDetails} 
    bind:navbarEnabled={enableNavbar} 
    enabled={enableHomeScreen} 
    bind:enableError={enableError} 
    errorMessage={errorMessage}>
  </HomeScreen>

  <AddDetails on:toggle={toggleDetails} enabled={enableAddDetails}></AddDetails>
  {#if !enableAddDetails && !enableHomeScreen }
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
