export interface RouteInterface {
	component: React.FunctionComponent | React.ComponentClass;
	path: string;
	exact: boolean;
	protected: boolean;
}
export const routes: RouteInterface[] = [];
