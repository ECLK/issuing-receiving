import { Staff } from "./staff";

export interface ReportToWork extends Staff{
    time: string;
    date: string;
}
