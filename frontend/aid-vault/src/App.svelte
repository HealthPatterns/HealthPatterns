<script lang="ts">
  import AddDetails from "./lib/AddDetails.svelte";
  import HomeScreen from "./lib/HomeScreen.svelte";
  import Navbar from "./lib/Navbar.svelte";
  import { onMount } from "svelte";
  import Loader from "./lib/Loader.svelte";
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

  //API
  async function apiLogin(username : string, password : string) {
    const url = "http://localhost:3000/auth/login";

    const formData = new URLSearchParams();
    formData.append('grant_type', '');
    formData.append('username', username);
    formData.append('password', password);
    formData.append('scope', '');
    formData.append('client_id', '');
    formData.append('client_secret', '');

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'accept': 'application/json'
      },
      body: formData
    };

    try {
      const response = await fetch(url, options);
      const statusCode = response.status;
      if (statusCode === 200) {
        console.log("API call 'Login' successful.");
        const data = await response.json();
        $loginData.accessToken = data.access_token;
      } else {
        console.log("Error during API call 'Login'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function apiGetUsername(api_token : string) {
    const url = "http://localhost:3000/user/name";

    const options = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
      }
    };

    try {
      const response = await fetch(url, options);
      const statusCode = response.status;
      if (statusCode === 200) {
        console.log("API call 'GetUsername' successful.");
        const data = await response.json();
        $loginData.username =  data.full_name;
      } else {
        console.log("Error during API call 'GetUsername'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function apiGetActiveTracking(api_token : string) {
    const url = "http://localhost:3000/trackings/active";

    const options = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
      }
    };

    try {
        const response = await fetch(url, options);
        const statusCode = response.status;
        if (statusCode === 200) {
          console.log("API call 'GetActiveTracking' successful.");
          const data = await response.json();
          if (data && data.length > 0) {
            $trackingData.tracking_id =  data[0].id;
            $trackingData.unixtime = data[0].time_start;
            $trackingData.isTracking = true;
          }
      } else {
        console.log("Error during API call 'GetActiveTracking'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

   async function apiGetDetails (api_token : string, tracking_id : string) {
      const url = `http://localhost:3000/trackings/${tracking_id}/details`;

      const options = {
      method: 'GET',
      headers: {
          'Content-Type': 'application/json',
          'accept': 'application/json',
          'Authorization': 'Bearer ' + api_token,
      }
      };

      try {
      const response = await fetch(url, options);
      const statusCode = response.status;
      if (statusCode === 200) {
          console.log("API call 'GetDetails' successful.");
          const data = await response.json();
          $trackingData.front_regions = data.front_regions;
          $trackingData.back_regions = data.back_regions;
          $trackingData.intensity = data.intensity;
          $trackingData.diet = data.diet;
      } else {
          console.log("Error during API call 'GetDetails'.");
      }
      } catch (error) {
      console.error("Error:", error);
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
