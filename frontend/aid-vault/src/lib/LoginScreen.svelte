<script lang="ts">
    import { loginData } from '../store.js';
    export let enabled : boolean;
    export let homeEnabled : boolean;

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
            enabled = false;
            homeEnabled = true;
            //TODO: add fetchData function
        } else {
            errorMessage = "Login failed. Please check your credentials.";
        }
        } catch (error) {
        console.error("Error:", error);
        }
    }
  
    const handleLogin = () => {
        errorMessage = "";
        apiLogin(username, password);
    };
</script>

{#if enabled}
<div id=LoginScreen>
    <h1>Login</h1>
    <form on:submit|preventDefault={handleLogin}>
        <label for="username">Nutzername:</label>
        <input type="text" id="username" bind:value={username} />

        <label for="password">Passwort:</label>
        <input type="password" id="password" bind:value={password} />

        <button type="submit">Login</button>
    </form>
    {#if errorMessage}
    <p style="color: red;">{errorMessage}</p>
    {/if}
</div>
{/if}

<style>
#LoginScreen {
    display: flex;
    height: 90%;
    width: 80%;
    flex-direction: column;
}
h1 {
    font-size: x-large;
    font-weight: 500;
}
input {
    border: 1px solid;
    border-radius: 4px;
    border-color: #0D698B;
}
button {
    background-color: #0D698B;
    color: #fff;
    border-radius: 4px;
}
</style>