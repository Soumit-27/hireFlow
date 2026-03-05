import { postRequest } from "./api";

interface RegisterData {
  name: string;
  email: string;
  role: string;
  company_name: string;
}

interface User {
  name: string;
  email: string;
  role: string;
  company_name: string;
}

interface RegisterResponse {
  message: string;
  user: User;
  access_token?: string;
}

export const register = async (
  data: RegisterData
): Promise<RegisterResponse> => {
  return await postRequest<RegisterResponse>(
    "/auth/register",
    data
  );
};