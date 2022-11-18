import React, { useState } from 'react';

const ButtonLink = ({href, className, children}) => {
  return (
    <a href={href} className={className}>
      {children}
    </a>
  );
}

export default ButtonLink;