<script lang="ts">
    import { apiLogin, apiRegister } from '../../lib/ApiFunctions.ts'
    import Loader from "../../lib/Loader.svelte";

    export let enableTrackingScreen : boolean
    export let enableLoginScreen : boolean;
    export let enableRegisterMessage : boolean;

    let isLoading = false;
    let username = "";
    let password = "";
    let password2 = "";
    let errorMessage : string | undefined;
    let enableRegister = false;

    const handleLogin = () => {
        isLoading = true;
        apiLogin(username, password).then((result) => {
            isLoading = false;
            if (result === true) {
                errorMessage = "";
                enableTrackingScreen = true;
                enableLoginScreen = false;
            } else {
                errorMessage = result;
            }
        });
    };

    const hasUpperCase = (password: string) => /[A-Z]/.test(password);
    const hasLowerCase = (password: string) => /[a-z]/.test(password);
    const hasNumber = (password: string) => /[0-9]/.test(password);
    const hasSpecialChar = (password: string) => /[!@#$%^&*]/.test(password);
    const hasEightChars = (password: string) => password.length >= 8;

    const handleRegister = () => {
        errorMessage = "";
        isLoading = true;
        if (password !== password2) {
            isLoading = false;
            errorMessage = "Passwörter stimmen nicht überein";
            return;
        } else {
          if (hasUpperCase(password) && hasLowerCase(password) && hasNumber(password) && hasSpecialChar(password) && hasEightChars(password)) {
            apiRegister(password).then((result) => {
              isLoading = false;
              if (result === true) {
                  errorMessage = "";
                  enableTrackingScreen = true;
                  enableRegisterMessage = true;
                  enableLoginScreen = false;
              } else {
                  errorMessage = result;
              }
            });
          } else {
            isLoading = false;
            errorMessage = "Passwort muss mindestens 8 Zeichen, 1 Groß-, 1 Kleinbuchstaben und 1 Sonderzeichen haben.";
          }
        }
    };
</script>

{#if isLoading}
  <div id="Loader">
    <Loader/>
  </div>
{/if}
{#if !enableRegister}
  <div id=LoginScreen>
    <h1>Login</h1>
    <div id=LoginFields>
      <form on:submit|preventDefault={handleLogin}>
        <input type="text" id="username" bind:value={username} placeholder="Nutzername"/>
        <input type="password" id="password" bind:value={password} placeholder="Passwort"/>
        <button type="submit">Login</button>
        {#if errorMessage}
        <p id="error">{errorMessage}</p>
        {/if}
      </form>
      <p id="createAccount">Noch keinen Account? <a href=" " on:click|preventDefault={() => enableRegister = true}>Registrieren</a></p>
    </div>
  </div>
{:else}
  <div id=LoginScreen>
    <h1>Registrieren</h1>
    <div id=LoginFields>
      <form on:submit|preventDefault={handleRegister}>
        <input type="password" id="password" bind:value={password} placeholder="Passwort" on:focus={() => {errorMessage = ""}}/>
        <ul id="passwordRequirements">
          <li class:valid={hasEightChars(password)}>Mindestens 8 Zeichen lang</li>
          <li class:valid={hasUpperCase(password)}>Mindestens 1 Großbuchstaben (A-Z)</li>
          <li class:valid={hasLowerCase(password)}>Mindestens 1 Kleinbuchstaben (a-z)</li>
          <li class:valid={hasNumber(password)}>Mindestens 1 Zahl (0-9)</li>
          <li class:valid={hasSpecialChar(password)}>Mindestens 1 Sonderzeichen (@-$)</li>
        </ul>
        <input type="password" id="password" bind:value={password2} placeholder="Passwort wiederholen" on:focus={() => {errorMessage = ""}}/>
        <button type="submit">Registrieren</button>
        {#if errorMessage}
        <p id="error">{errorMessage}</p>
        {/if}
      </form>
      <p id="createAccount">Bereits registriert? <a href=" " on:click|preventDefault={() => enableRegister = false}>Login</a></p>
    </div>
  </div>
{/if}

<style>
#Loader {
    position: fixed;
    z-index: 2;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.75);
}
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

#passwordRequirements {
    list-style-position: inside;;
    margin-top: 1rem;
}

#passwordRequirements li {
    list-style-type: "\274C";
    color: red;
}

#passwordRequirements li.valid {
    list-style-type: "\2705";
    color: green;
}
</style>