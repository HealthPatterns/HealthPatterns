<script lang="ts">
  import { onMount } from "svelte";
  import "./font.css"
  import TrackingScreen from "./views/home/TrackingScreen.svelte";
  import LoginScreen from "./views/login/LoginScreen.svelte";

  let enableTrackingScreen : boolean = false;
  let enableLoginScreen : boolean = false;
  let enableMessage : boolean = false;
  let enableError : boolean;
  let errorMessage : string;

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
{:else if !enableLoginScreen}
  <TrackingScreen
    bind:enableTrackingScreen={enableTrackingScreen}
    bind:enableMessage={enableMessage}
    bind:enableError={enableError} 
    errorMessage={errorMessage}>
  </TrackingScreen>
{/if}