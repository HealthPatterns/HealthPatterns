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
    <div id=LoginFields>
        <form on:submit|preventDefault={handleLogin}>
            <input type="text" id="username" bind:value={username} placeholder="Nutzername"/>
            <input type="password" id="password" bind:value={password} placeholder="Passwort"/>
            <button type="submit">Login</button>
        </form>
        {#if errorMessage}
        <p style="color: red;">{errorMessage}</p>
        {/if}
    </div>
</div>
{/if}

<style>
#LoginScreen {
    display: flex;
    height: 90%;
    width: 80%;
    flex-direction: column;
    justify-content: center;
}
#LoginFields {
    height: 70%;
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
    text-align: center;
}
</style>