<script lang="ts">
</script>

<svg id="load" xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-loader-3" width="64" height="64" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path d="M3 12a9 9 0 0 0 9 9a9 9 0 0 0 9 -9a9 9 0 0 0 -9 -9"></path>
    <path d="M17 12a5 5 0 1 0 -5 5"></path>
 </svg>

 <style>
    #load{
    animation-name: ckw;
    animation-duration: 1s;
    animation-iteration-count: infinite;
    transform-origin: 50% 50%;
    animation-timing-function:linear;
}
@keyframes ckw {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}</style>