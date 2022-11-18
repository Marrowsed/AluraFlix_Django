import { useState } from 'react';

function useForm(initialData) {
  const [values, setValues] = useState(initialData);

  function setValue(key, value) {
    setValues({
      ...values,
      [key]: value,
    });
  }

  function handleChange(eventInfo) {
    setValue(
      eventInfo.target.getAttribute('name'),
      eventInfo.target.value,
    );
  }

  function clearForm() {
    setValues(initialData);
  }

  return {
    values,
    handleChange,
    clearForm,
  };
}

export default useForm;
