import { URL_BACKEND } from '../../environments/environments';
import {
	FIN_CARGANDO_LOGIN,
	INICIO_CARGANDO_LOGIN,
	SET_SUCCESS_LOGIN
} from '../types/types';
import axios from 'axios';
const inicioCargandoLogin = () => {
	return {
		type: INICIO_CARGANDO_LOGIN
	};
};
const finCargandoLogin = () => {
	return {
		type: FIN_CARGANDO_LOGIN
	};
};

export const iniciarSesionAction = (correo, password) => {
	return async (dispatch) => {
		dispatch(inicioCargandoLogin());

		//const endpoint = `${URL_BACKEND}/login`;
		const endpoint = `http://127.0.0.1:8000/api/token/`;
		const response = await axios.post(
			endpoint,
			JSON.stringify({ username: correo, password: password }),
			{
				headers: {
					'Content-type': 'application/json'
				}
			}
		);
		if (response.status === 200) {
			//console.log(response.data);
			let token = response.data.access;
			localStorage.setItem('token', token);
			//console.log(token);
			let payload = token.split('.')[1];
			//console.log(payload);
			let payloadDecoded = atob(payload);
			let payloadJSON = JSON.parse(payloadDecoded);
			console.log("payload",payloadJSON)
			dispatch({
				type: SET_SUCCESS_LOGIN,
				payload: {
					autenticado: true,
					usu_id: payloadJSON.user_id,
					token: token
				}
			});
		}
		dispatch(finCargandoLogin());
	};
};

export const iniciarSesionLocalStorage = () => {
	return async (dispatch) => {
		dispatch(inicioCargandoLogin());
		//let token = localStorage.getItem('token');
		let token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNjU5MTM2NCwiaWF0IjoxNjM2NTA0OTY0LCJqdGkiOiJmZmM1ZWJmOTY5Nzk0OTBhODlmZmZlMTEyMmYxN2M3MiIsInVzZXJfaWQiOjJ9.D1Jdh1Q5vhS_cGdasspsDIpmbYDNINtB-dEi6zUdP8g'
		try {
			if (token) {
				const endpoint = `${URL_BACKEND}/auth/empleado`;
				const response = await axios.get
				(endpoint,
				{
					headers: {
						'authorization': `bearer ${token}`
					}
				}
				);
				console.log(response.data)
				if (response.data.ok) {

					localStorage.setItem('empleado_nom', response.data.content.empleado_nom);
					
					let payload = token.split('.')[1];
					let payloadDecoded = atob(payload);
					let payloadJSON = JSON.parse(payloadDecoded);
					
					dispatch({
						type: SET_SUCCESS_LOGIN,
						payload: {
							autenticado: true,
							usu_id: payloadJSON.usu_id,
							token: token
						}
					});
					dispatch(finCargandoLogin());
				}
			} else {
				dispatch(finCargandoLogin());
			}
		} catch (error) {
			console.log('errosh');
			localStorage.removeItem('token');
			dispatch(finCargandoLogin());
		}
	};
};
