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
  let enableMessage = false;
  
  let enableError : boolean;
  let errorMessage : string;

  function toggleDetails () {
    enableAddDetails = !enableAddDetails;
    enableHomeScreen = !enableHomeScreen;
    console.log(isTracking);
  }

  async function fetchData() {
    try {
      const user_id = 1;
      username = await apiGetUsername(user_id);
      console.log(username);
    } catch (error) {
      console.error("Error fetchData:", error);
    }
  }

  fetchData();


  //API
  async function apiGetUsername(user_id) {
    const url = `http://localhost:3000/users/${user_id}`;

    const options = {
      method: 'GET',
      headers: {
        'accept': 'application/json'
      }
    };

    try {
      const response = await fetch(url, options);
      const statusCode = response.status;
      if (statusCode === 200) {
        console.log("API call 'getUsername' successful.");
        const data = await response.json();
        return data.full_name;
      } else {
        console.log("Error during API call 'GetUsername'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function apiStartTracking(apiToken) {
    const url = "http://localhost:3000/tracking";

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
      if (statusCode === 201) {
        console.log("API call 'StartTracking' successful.");
      } else {
        console.log("Error during API call 'StartTracking'.");
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
  
  <HomeScreen 
    bind:enableMessage={enableMessage} 
    on:toggle={toggleDetails} 
    bind:navbarEnabled={enableNavbar} 
    bind:isTracking={isTracking} 
    enabled={enableHomeScreen} 
    username={username} 
    bind:enableError={enableError} 
    errorMessage={errorMessage}>
  </HomeScreen>

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
