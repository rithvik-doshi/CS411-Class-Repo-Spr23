import type { PostProps } from '../../types'
import type { PageLoad } from './$types'

let posts: PostProps[] = [
    {
        user: { userId: 1, username: "chris18", firstname: "Chris", lastname: "Chan", color: "blue"},
        content: "wordssssss this is a post yeyeyeyeyeye"
    },
    {
        user: { userId: 2, username: "rithvik123", firstname: "Rithvik", lastname: "Doshi", color: "amber"},
        content: "Anotha Post"
    },
    {
        user: { userId: 1, username: "chris18", firstname: "Chris", lastname: "Chan", color: "blue"},
        content: "I can't stop postingggg"
    },
    {
        user: { userId: 3, username: "axelv19", firstname: "Axel", lastname: "Vega", color: "purple"},
        content: "Yeyeyeyeye"
    }
]

export const load = (() => {
    return {
        posts
    }
}) satisfies PageLoad;