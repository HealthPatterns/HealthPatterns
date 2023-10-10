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

  //API
  async function apiStartTracking(apiToken) {
  const url = "http://localhost/";

  const requestData = {
    "currentTime": new Date().toISOString()
  };

  const options = {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + apiToken,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(requestData)
  };

  try {
    const response = await fetch(url, options);
    const statusCode = response.status;
    if (statusCode === 200) {
      console.log("API call 'tracking started' successful.");
    } else {
      console.log("Error during API call 'tracking started'.");
    }
  } catch (error) {
    console.error("Error:", error);
  }
}


  function apiStopTracking () {
    
  }

  function apiDetails () {
    
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
