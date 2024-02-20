<script lang="ts">
    import { loginData, trackingData } from '../../store.js';
    export let enableTrackingScreen : boolean, enableLoginScreen : boolean;

    let username = "";
    let password = "";
    let errorMessage = "";

    async function apiLogin(username : string, password : string) {
        const url = "http://localhost:3000/auth/login";

        const formData = new URLSearchParams();
        formData.append('username', username);
        formData.append('password', password);

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
            const data = await response.json();
            $loginData.accessToken = data.access_token;
            enableTrackingScreen = true;
            enableLoginScreen = false;
            fetchData();
        } else {
            errorMessage = "Login fehlgeschlagen. Bitte überprüfen Sie Ihre Eingaben.";
        }
        } catch (error) {
        console.error("Error:", error);
        }
    }

    async function fetchData() {
    try {
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
        $loginData.username =  data.display_name;
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
          if (data && data.front_regions !== null){
            $trackingData.front_regions = data.front_regions;
            $trackingData.back_regions = data.back_regions;
            $trackingData.intensity = data.intensity;
            $trackingData.diet = data.diet;
          }
      } else {
          console.log("Error during API call 'GetDetails'.");
      }
      } catch (error) {
      console.error("Error:", error);
      }
    }
  
    const handleLogin = () => {
        errorMessage = "";
        apiLogin(username, password);
    };
    const register = () => {
      //TODO: folgendes ist nur platzhalter
        enableLoginScreen = false;
        enableTrackingScreen = true;
    };
</script>

<div id=LoginScreen>
    <h1>Registrieren</h1>
    <div id=LoginFields>
        <form on:submit|preventDefault={handleLogin}>
            <input type="text" id="username" bind:value={username} placeholder="Nutzername"/>
            <input type="password" id="password" bind:value={password} placeholder="Passwort"/>
            <button type="submit">Login</button>
            {#if errorMessage}
            <p id="error">{errorMessage}</p>
            {/if}
        </form>
        <p id="createAccount">Noch keinen Account? <a href="#" on:click|preventDefault={register}>Registrieren</a></p>
    </div>
</div>

<style>
#LoginScreen {
    display: flex;
    height: 100%;
    width: 100%;
    flex-direction: column;
    justify-content: center;
    align-content: center;
    align-items: center;
}
#LoginFields {
    height: 70%;
    width: 80%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-content: space-between;
}
h1 {
    font-size: xx-large;
    font-weight: 500;
    align-items: center;
    justify-content: center;
    display: flex;
    height: 30%;
}
button {
    background-color: #0d698b;
    color: #f2f1e8;
    border: 0;
    border-radius: 0.4rem;
    font-size: x-large;
    font-weight: 500;
    padding: 0.5rem;
    margin-top: 2rem;
    width: 100%;
    align-items: center;
    justify-content: center;
    display: flex;
}
input {
    background-color: #E9EFF3;
    border: 0;
    border-radius: 0.4rem;
    font-weight: 500;
    padding: 0.75rem;
    margin-top: 1.5rem;
    width: 100%;
    align-items: center;
    justify-content: center;
    display: flex;
}
input::placeholder {
    color: #8e9294;
}
input:focus {
    outline-color: #0D698B;
}
p {
    margin-top: 1rem;
    margin-bottom: 2.5rem;
    text-align: center;
}
#error {
    color: #e34234;
}
a {
    color: #0D698B;
    text-decoration: none;
}
</style>