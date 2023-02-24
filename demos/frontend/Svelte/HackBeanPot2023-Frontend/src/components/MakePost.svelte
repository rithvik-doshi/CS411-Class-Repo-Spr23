<script lang='ts'>
	import type { UserProps } from '../types';
    import UserProfileIcon from './UserProfileIcon.svelte'
    import { currentUser } from '../stores/currentUser';

    let user = $currentUser;

</script>

<div class='flex
    w-full max-w-2xl
    my-6
'>
    <div class='m-2'><UserProfileIcon {user}/></div>
    <input 
        class='border-2 rounded-md 
            ml-5 w-full px-3
        '
        type='text' placeholder='Start a post'>
</div>