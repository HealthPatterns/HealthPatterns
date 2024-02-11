<script lang="ts">
    import { loginData, trackingData } from '../store.js';
    import { get } from 'svelte/store';
</script>

<script lang="ts" context="module">

  export async function apiLogin(username : string, password : string) {
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
        get(loginData).accessToken = data.access_token;
      } else {
        console.log("Error during API call 'Login'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  export async function apiGetUsername(api_token : string) {
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
        get(loginData).username =  data.display_name;
      } else {
        console.log("Error during API call 'GetUsername'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  export async function apiGetActiveTracking(api_token : string) {
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
            get(trackingData).tracking_id =  data[0].id;
            get(trackingData).unixtime = data[0].time_start;
            get(trackingData).isTracking = true;
          }
      } else {
        console.log("Error during API call 'GetActiveTracking'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

   export async function apiGetDetails (api_token : string, tracking_id : string) {
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
          if (data && data.front_regions !== null){
            get(trackingData).front_regions = data.front_regions;
            get(trackingData).back_regions = data.back_regions;
            get(trackingData).intensity = data.intensity;
            get(trackingData).diet = data.diet;
          }
      } else {
          console.log("Error during API call 'GetDetails'.");
      }
      } catch (error) {
      console.error("Error:", error);
      }
    }

    export async function apiSetDetails (api_token : string, tracking_id : string, front_regions, back_regions, intensity, diet) {
    const url = `http://localhost:3000/trackings/${tracking_id}/details`;

    const options = {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
      },
      body: JSON.stringify({
        'front_regions': front_regions,
        'back_regions': back_regions,
        'intensity': intensity,
        'diet': diet
      })
    };

    try {
      const response = await fetch(url, options);
      const statusCode = response.status;
      if (statusCode === 200) {
        console.log("API call 'SetDetails' successful.");
      } else {
        console.log("Error during API call 'SetDetails'.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }
</script>