<script lang="ts">
  import { onMount } from "svelte";
  import "./font.css"
  import TrackingScreen from "./views/home/TrackingScreen.svelte";
  import LoginScreen from "./views/login/LoginScreen.svelte";


  let enableTrackingScreen : boolean = false, enableHomeScreen : boolean = false, enableLoginScreen : boolean = false, enableNavbar : boolean = false;
  let enableMessage : boolean = false, enableError : boolean, errorMessage : string;

  onMount(() => {
    enableLoginScreen = true;
    enableTrackingScreen = false;
	});
</script>

{#if !enableTrackingScreen && enableLoginScreen}
  <LoginScreen 
    bind:enableTrackingScreen={enableTrackingScreen}
    bind:enableLoginScreen={enableLoginScreen}>
  </LoginScreen>
{:else if enableTrackingScreen && !enableLoginScreen}
  <TrackingScreen
    bind:enableHomeScreen={enableTrackingScreen}
    bind:enableNavbar={enableNavbar} 
    bind:enableMessage={enableMessage}
    bind:enableError={enableError} 
    errorMessage={errorMessage}>
  </TrackingScreen>
{/if}