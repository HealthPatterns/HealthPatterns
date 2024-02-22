<script lang="ts">
    import Header from '../../lib/Header.svelte';
    import Loader from '../../lib/Loader.svelte';
    import { apiGetAllTrackings } from '../../lib/ApiFunctions.svelte';
    import { loginData } from '../../store.js';

    export let enablePreviousTrackingsScreen : boolean;
    export let enableTrackingScreen : boolean;
    let trackings = apiGetAllTrackings($loginData.accessToken);

  function handleClick(index) {
    console.log('Clicked on item:', trackings[index]);
  }
</script>

<main>
    {#if enablePreviousTrackingsScreen}
    <div id="PreviousScreen">
        <Header
            bind:enableTrackingScreen={enableTrackingScreen}
            bind:enablePreviousTrackingsScreen={enablePreviousTrackingsScreen}>
        </Header>
        <h1 style="margin-top: 1.4rem; margin-bottom: 1.4rem">Trackingeinträge</h1>
        {#await trackings}
            <Loader></Loader>
        {:then trackingsData}
            {#each trackingsData as tracking, index}
                <div class="row">
                    <div class="column-item">
                        <div class="date">{new Date(tracking.time_start * 1000).toLocaleDateString()}</div>
                        <div class="time">{new Date(tracking.time_start * 1000).toLocaleTimeString()}</div>
                    </div>
                    <div class="column-button">
                        <div class="arrow" on:click={() => handleClick(index)}>➡️</div>
                    </div>
                </div>
            {/each}
        {/await}
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
      background-color: #fff;
      position: relative;
  }
  #PreviousScreen {
    display: flex;
    height: 90%;
    width: 80%;
    flex-direction: column;
    }

    h1 {
    font-size: x-large;
    font-weight: 500;
}
  
  .row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    border-bottom: 1px solid #ccc;
  }

  .date {
    font-size: 18px;
    font-weight: bold;
    margin-right: 10px;
  }

  .time {
    font-size: 14px;
    color: #888;
    margin-right: 10px;
  }

  .arrow {
    cursor: pointer;
  }

  .column-item {
    display: flex;
    flex-direction: column;
  }

  .column-button {
    display: flex;
    justify-content: flex-end;
  }
</style>