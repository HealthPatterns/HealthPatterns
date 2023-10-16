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

  async function fetchData(api_token) {
    try {;
      username = await apiGetUsername(api_token);
      console.log(username);
    } catch (error) {
      console.error("Error fetchData:", error);
    }
  }

  //Testdata
  const api_token = apiLogin("admin", "admin");
  fetchData(api_token);


  //API
  async function apiLogin(username, password) {
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
        return data.access_token;
      } else {
        console.log("Error during API call 'Login'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function apiGetUsername(api_token) {
    const url = "http://localhost:3000/user";

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

  async function apiStartTracking(api_token) {
    const current_time = Math.floor(Date.now() / 1000);
    const url = "http://localhost:3000/trackings";

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
      },
      body: JSON.stringify({
        'start_time': current_time
      })
    };

    try {
      const response = await fetch(url, options);
      const statusCode = response.status;
      if (statusCode === 201) {
        console.log("API call 'StartTracking' successful.");
        const data = await response.json();
        return data.id;
      } else {
        console.log("Error during API call 'StartTracking'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function apiStopTracking (api_token, tracking_id) {
    const current_time = Math.floor(Date.now() / 1000);
    const url = "http://localhost:3000/trackings/tracking";

    const options = {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
      },
      body: JSON.stringify({
        'id': tracking_id,
        'end_time': current_time
      })
    };

    try {
      const response = await fetch(url, options);
      const statusCode = response.status;
      if (statusCode === 200) {
        console.log("API call 'StopTracking' successful.");
      } else {
        console.log("Error during API call 'StopTracking'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function apiGetDetails (api_token, tracking_id) {
    const url = `http://localhost:3000/trackings/tracking/details?tracking_id=${tracking_id}`;

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
        return data;
      } else {
        console.log("Error during API call 'GetDetails'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  async function apiSetDetails (api_token, tracking_id, front_regions, back_regions, intensity, sleep, diet) {
    const url = "http://localhost:3000/trackings/tracking/details";

    const options = {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
      },
      body: JSON.stringify({
        'id': tracking_id,
        'front_regions': [
          front_regions
        ],
        'back_regions': [
          back_regions
        ],
        'intensity': intensity,
        'sleep': sleep,
        'diet': diet
      })
    };

    try {
      const response = await fetch(url, options);
      const statusCode = response.status;
      if (statusCode === 200) {
        console.log("API call 'GetDetails' successful.");
      } else {
        console.log("Error during API call 'GetDetails'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
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
