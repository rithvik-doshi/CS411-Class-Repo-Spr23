<script lang="ts">
    import type { PostProps } from "../types";
    import UserProfileIcon from "./UserProfileIcon.svelte";

    export let post: PostProps;
    let {user} = post;
    
</script>

<div class='
    w-full
    my-4 max-w-2xl
    flex flex-row
    border-2 rounded-lg
    '>
    <div class='m-2 mr-5'><UserProfileIcon {user}/></div>
    <div class='mt-2 pb-5'>
        <h3 class='font-bold text-xl'>
            {user.username}
        </h3>
        <div>
            {post.content}
        </div>
    </div>
</div>

