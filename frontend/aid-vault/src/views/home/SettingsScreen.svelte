<script lang="ts">
    import Header from '../../lib/Header.svelte';
    import Loader from '../../lib/Loader.svelte';
    import LogoutButton from '../../lib/LogoutButton.svelte';
    import { loginData } from '../../store.js';
    import { apiResetPassword } from '../../lib/ApiFunctions.ts';

    export let enableSettingsScreen : boolean;
    export let enableTrackingScreen : boolean;
    export let enablePreviousTrackingsScreen : boolean;

    let isLoading = false;
    let errorMessage : string | undefined;
    let currentPassword = '';
    let newPassword = '';
    let confirmPassword = '';

    function handlePwdChange () {
        errorMessage = "";
        isLoading = true;
        if (!currentPassword || !newPassword || !confirmPassword){
            isLoading = false;
            errorMessage="Es müssen alle Felder ausgefüllt werden.";
            return;
        } else if (newPassword !== confirmPassword) {
            isLoading = false;
            errorMessage="Die neuen Passwörter stimmen nicht überein.";
            return;
        } else if (currentPassword === newPassword){
            isLoading = false;
            errorMessage="Das neue Passwort darf nicht dem alten entsprechen.";
            return;
        } else {
            apiResetPassword($loginData.accessToken ,currentPassword, newPassword).then((result) => {
                if (result === true) {
                    errorMessage = "Passwort erfolgreich geändert!";
                    currentPassword = '';
                    newPassword = '';
                    confirmPassword = '';
                } else {
                    errorMessage = "Da hat etwas nicht geklappt. Bitte versuchen Sie es erneut.";
                }
                isLoading = false;
            });
        }
    }

</script>

<main>
    {#if isLoading}
    <div id="Loader">
        <Loader/>
    </div>
    {/if}
    {#if enableSettingsScreen}
    <div id="SettingsScreen">
        <Header
        bind:enableTrackingScreen={enableTrackingScreen}
        bind:enablePreviousTrackingsScreen={enablePreviousTrackingsScreen}
        bind:enableSettingsScreen={enableSettingsScreen}>
        </Header>
        <h1>Einstellungen</h1>

        <form id="change-password-form" on:submit|preventDefault={handlePwdChange}>
            <label for="current-password">Aktuelles Passwort:</label>
            <input type="password" bind:value={currentPassword} autocomplete="current-password" id="current-password">

            <label for="new-password">Neues Passwort:</label>
            <input type="password" bind:value={newPassword} autocomplete="new-password" id="new-password">

            <label for="confirm-password">Neues Passwort bestätigen:</label>
            <input type="password" bind:value={confirmPassword} autocomplete="new-password" id="confirm-password">

            <button type="submit">Passwort ändern</button>
            {#if errorMessage}
            <p id="error">{errorMessage}</p>
            {/if}
        </form>
        <div id="lower-button">
            <LogoutButton></LogoutButton>
        </div>
    </div>
    {:else}
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
    background-color: var(--primary-background-color);
    position: relative;
}
#Loader {
    position: fixed;
    z-index: 2;
    width: 100%;
    height: 100%;
    background-color: rgba(77, 77, 77, 0.184);
}
#SettingsScreen {
    display: flex;
    height: 90%;
    width: 80%;
    flex-direction: column;
}
  
h1 {
    font-size: x-large;
    font-weight: 500;
    margin-top: 1.4rem;
    margin-bottom: 2rem;
}

button {
    background-color: var(--primary-100-color);
    color: var(--secondary-background-color);
    border: 0;
    border-radius: 0.4rem;
    font-size: x-large;
    font-weight: 500;
    padding: 0.5rem;
    width: 100%;
    align-items: center;
    justify-content: center;
    display: flex;
}
input {
    background-color: var(--primary-10-color);
    border: 0;
    border-radius: 0.4rem;
    font-weight: 500;
    padding: 0.75rem;
    margin-bottom: 1.5rem;
    width: 100%;
    align-items: center;
    justify-content: center;
    display: flex;
}
input::placeholder {
    color: #8e9294;
}
input:focus {
    outline-color: var(--primary-100-color);
}

#lower-button {
    position: absolute;
    bottom: 2.8rem;
    width: 80%;
    margin-left: auto;
    margin-right: auto;
    left: 0;
    right: 0;
}
p {
    margin-top: 1rem;
    margin-bottom: 2.5rem;
    text-align: center;
}
#error {
    color: var(--accent-color);
}
</style>