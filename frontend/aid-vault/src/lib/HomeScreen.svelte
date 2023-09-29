<script lang="ts">

    let username = "Random Username";
    let isTracking = true;

    let timer : any;

    let count = 0;
    let hour = 0;
    let minute = 0;
    let second = 0;

    let hrString : string;
    let minString : string;
    let secString : string;
    let countString : string;

    createStrings();

    function start () {
        timer = true;
        stopWatch();
    }

    function stop () {
        timer = false;
    }

    function reset () {
        timer = false;
        hour = 0;
        minute = 0;
        second = 0;
        count = 0
    };

    function stop_reset() {
        stop();
        reset();
    }

    function createStrings() {
        hrString = hour.toString();
        minString = minute.toString();
        secString = second.toString();
        countString = count.toString();

        if (hour < 10) {
            hrString = "0" + hrString;
        }

        if (minute < 10) {
            minString = "0" + minString;
        }

        if (second < 10) {
            secString = "0" + secString;
        }

        if (count < 10) {
            countString = "0" + countString;
        }
    }

function stopWatch() {
    if (timer) {
        count++;

        if (count == 100) {
            second++;
            count = 0;
        }

        if (second == 60) {
            minute++;
            second = 0;
        }

        if (minute == 60) {
            hour++;
            minute = 0;
            second = 0;
        }

        createStrings();

        setTimeout(stopWatch, 10);
    }
}


</script>

<div id="HomeScreen">
    <h1 style="margin-top: 20px;">Guten Morgen {username}!</h1>
    <div class="time"> 
        <!-- <p class="circle">{hrString}:{minString}:{secString}</p> -->
        <div class="x0">
            <div class="x1">
                <div class="x2">
                    <div class="x3">
                        <!-- BEG Content -->
                        <div class="x4">
                        </div>
                        <div class="x6">
                            <div style="display: flex; height:100%; align-items:center; justify-content:center"><p>{hrString}:{minString}:{secString}</p></div>
                        </div>                
                        <div class="x5">
                        </div>
                        <!-- END Content -->
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div style="display:flex; align-items: center; flex-direction:column; width:100%; margin-top: auto; ">


        {#if !isTracking}
        <button class="details-button">Details hinzufügen</button>
        {/if}
        <button on:click={() => {isTracking ? start() : stop_reset(); isTracking = !isTracking;}} class={isTracking ? "tracking-button" : "tracking-button tracking-active" }>
            {#if isTracking}
            <svg style="margin-right: 0.5rem;" xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-player-play-filled" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M6 4v16a1 1 0 0 0 1.524 .852l13 -8a1 1 0 0 0 0 -1.704l-13 -8a1 1 0 0 0 -1.524 .852z" stroke-width="0" fill="currentColor"></path>
            </svg>
            Schmerz tracken
            {/if}
            {#if isTracking == false}
            <svg style="margin-right: 0.5rem;" xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-player-stop-filled" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <path d="M17 4h-10a3 3 0 0 0 -3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3 -3v-10a3 3 0 0 0 -3 -3z" stroke-width="0" fill="currentColor"></path>
             </svg>
             Tracking beenden
            {/if}
        </button>
    </div>
</div>

<style>

#HomeScreen {
    display: flex;
    height: 90%;
    width: 80%;
    flex-direction: column;
}

h1 {
    font-size: x-large;
    font-weight: 500;
    margin-bottom: 0.6em;
}

h2 {
    font-size: large;
    font-weight: 500;
}

@media (max-width: 320px)
{
    .x2 {padding: 50%;}
}

@media (min-width: 321px) and (max-width: 800px)
{
    .x2 {padding: 25%;}
}

@media (min-width: 801px)
{
    .x1 {width:800px}
    .x2 {padding: 12.5%;}
}
.x0 {
    float:left;
    width:fit-content;
}
.x1 {
    margin:0px auto;
}
.x2 {
    overflow:hidden;
    display:block;
    float:left;
    width:auto;
    height:auto;
    position: relative;
    border-radius:50%;
    -moz-border-radius:50%;
    -webkit-border-radius:50%;
    -khtml-border-radius: 50%;
    background:#eee;

}
.x3 {
    position: absolute;
    width: 100%;
    left: 0;
    top:0;
    font-size: 100%;
    float:left;
    height:100%;
    background-color:red;
}
/* BEG Content */
.x3 div{float:left;}
.x4,.x5,.x6 {
    width:100%;
}
.x7,.x8 {
    width:50%;
    float:left;
    height:100%;
}
.x4,.x5,.x7,.x8 {
    text-align:center;
}
.x4 {
    background-color:blue;
    height:20%;
}
.x5 {
    background-color:yellow;
    height:20%;
}
.x6 {
    height:60%;
}
.x7 {
    background-color:green;
}
.x8 {
    background-color:orange;
}
/* END Content */


.time {
    display: flex;
    flex: 1;
    font-size: 3.5rem;
    font-weight: 500;
    width: 100%;
    height:auto;
    text-align: center;
    justify-content: center;
    align-items: center;
}

.tracking-button {
    background-color: #0d698b;
    color: #f2f1e8;
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

.details-button {
    border: 0;
    border-radius: 2rem;
    background-color: #c2d3db;
    font-size: medium;
    margin-bottom: 1.3rem;
    width: fit-content;
    padding: 0.3rem;
    padding-left: 3rem;
    padding-right: 3rem;
    font-size: 0.9rem;
}

.tracking-active {
    background-color: #e34234;
}

</style>