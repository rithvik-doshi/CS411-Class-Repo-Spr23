export interface PostProps {
    user: UserProps;
    content: string;
}

export interface UserProps {
    userId: number;
    username: string;
    firstname: string;
    lastname: string;
}