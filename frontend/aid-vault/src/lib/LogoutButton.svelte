<script lang="ts">
    import Cookies from 'js-cookie';
    
    function toggleLogout() {
        Cookies.remove('HealthPatterns');
        location.reload()
    }
</script>

<button class="logout-button" on:click={toggleLogout}>Logout</button>

<style>
    .logout-button {
        background-color: var(--accent-color);
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
</style>