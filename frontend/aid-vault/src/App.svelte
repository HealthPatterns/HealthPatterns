<script lang="ts">
  import { onMount } from "svelte";
  import Cookies from 'js-cookie';
  import { fetchData } from "./lib/ApiFunctions";
  import { loginData } from "./store.js";
  import "./font.css"
  import TrackingScreen from "./views/home/TrackingScreen.svelte";
  import PreviousTrackingsScreen from "./views/home/PreviousTrackingsScreen.svelte";
  import LoginScreen from "./views/login/LoginScreen.svelte";

  let enableTrackingScreen : boolean = false;
  let enablePreviousTrackingsScreen : boolean = false;
  let enableLoginScreen : boolean = false;
  let enableMessage : boolean = false;
  let enableRegisterMessage : boolean = false;
  let enableError : boolean;
  let errorMessage : string;

  onMount(() => {
    let cookieValue = Cookies.get('HealthPatterns');
    if (cookieValue) {
      $loginData.accessToken = cookieValue;
      fetchData();
      enableLoginScreen = false;
      enableTrackingScreen = true;
    } else {
      enableLoginScreen = true;
      enableTrackingScreen = false;
    }
	});
</script>

{#if !enableTrackingScreen && enableLoginScreen}
  <LoginScreen
    bind:enableTrackingScreen={enableTrackingScreen}
    bind:enableLoginScreen={enableLoginScreen}
    bind:enableRegisterMessage={enableRegisterMessage}>
  </LoginScreen>
{:else if !enableLoginScreen && enableTrackingScreen}
  <TrackingScreen
    bind:enableTrackingScreen={enableTrackingScreen}
    bind:enablePreviousTrackingsScreen={enablePreviousTrackingsScreen}
    bind:enableMessage={enableMessage}
    bind:enableRegisterMessage={enableRegisterMessage}
    bind:enableError={enableError}
    errorMessage={errorMessage}>
  </TrackingScreen>
{:else if !enableLoginScreen && enablePreviousTrackingsScreen}
  <PreviousTrackingsScreen
    bind:enableTrackingScreen={enableTrackingScreen}
    bind:enablePreviousTrackingsScreen={enablePreviousTrackingsScreen}>
  </PreviousTrackingsScreen>
{/if}