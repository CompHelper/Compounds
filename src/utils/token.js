const TOKEN = "Bearer";
export const localSave = (name, value) => {
  sessionStorage.setItem(name, value);
};

export const localRead = name => {
  return sessionStorage.getItem(name);
};

export const localRemove = name => {
  return sessionStorage.removeItem(name);
};

export const getToken = () => {
  return localRead(TOKEN);
};
export const saveToken = token => {
  localSave(TOKEN, token); //存token
};
export const removeToken = () => {
  localRemove(TOKEN); //删除token
};
