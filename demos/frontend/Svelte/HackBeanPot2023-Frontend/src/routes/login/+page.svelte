<script lang='ts'>
    import { goto } from "$app/navigation";
    import { currentUser } from "../../stores/currentUser";
	import type { UserProps } from "../../types";

    let username = '';
    let password = '';

    function handleSubmit(){
        // check if username and password
        currentUser.update(():UserProps => {return {userId: 1, username: "chris18", firstname: "Chris", lastname: "Chan", color:"blue"}})

        goto("/home")
    }
</script>

<div>
    <input type="text" placeholder="username" bind:value={username}>
    <input type="password" bind:value={password}>
    <button on:click={handleSubmit}>Sign In</button>
</div>