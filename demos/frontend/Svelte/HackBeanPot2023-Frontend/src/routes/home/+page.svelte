<script lang="ts">
    import Post from "../../components/Post.svelte";
    import MakePost from "../../components/MakePost.svelte";
    import type {PageData} from './$types';
    import { currentUser } from "../../stores/currentUser";
    import { onMount } from "svelte";
	import { goto } from "$app/navigation";

    onMount(() => {
        if($currentUser.userId == -1){
            goto("/");
        }
    })

    export let data: PageData;
    let {posts} = data;
    let user = $currentUser;
    
</script>

<div class=''>
    <div class='
        flex flex-col
        items-center
    '><MakePost {user}></MakePost></div>
    <div class='
        flex flex-col
        items-center
    '>
        {#each posts as post}
            <Post {post}/>
        {/each}
    </div>
</div>




