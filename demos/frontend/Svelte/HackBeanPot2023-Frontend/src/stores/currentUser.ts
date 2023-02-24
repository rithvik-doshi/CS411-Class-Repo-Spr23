import { writable, type Writable } from "svelte/store";
import type { UserProps } from "../types";

export const currentUser: Writable<UserProps> = writable({userId: -1, username: "", firstname:"", lastname:"", color:""});

