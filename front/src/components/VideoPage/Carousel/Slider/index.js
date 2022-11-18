import React from 'react'
import SlickSlider from 'react-slick';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import { Container } from './styles';

const Slider = ({children}) => {
  return (
    <Container>
        <SlickSlider {...{
            dots: false,
            infinite: false,
            speed: 300,
            centerMode: false,
            variableWidth: true,
            adaptiveHeight: true,
            }}>
            {children}
        </SlickSlider>
    </Container>

  )
}

export default Slider