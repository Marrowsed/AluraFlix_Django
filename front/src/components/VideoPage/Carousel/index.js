import React from 'react'
import {Title, VideoCardContainer, VideoCardGroupContainer, SliderItem} from './styles.js'
import Slider from './Slider'

const Carousel = ({data}) => {
    const categoryColor = 'red'
    const videos = data


    let getYouTubeId = (youtubeURL) => {
        return youtubeURL
          .replace(
            /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/,
            '$7',
          );
      }
      const imageURL = (videoURL) => {
        return `https://img.youtube.com/vi/${getYouTubeId(videoURL)}/hqdefault.jpg`;
      }

  return (
    <VideoCardGroupContainer>
        <Slider>
            {videos.map( (v, index) => (
              <>
              <Title style={{backgroundColor: categoryColor}}>
              {v.category_name}
                </Title>
                  <SliderItem key={v.title}>
                    <VideoCardContainer
                      url={imageURL(v.url)}
                      href={v.url}
                      target="_blank"
                      style={{ borderColor: categoryColor || 'red' }}
                      title={v.title}
                    />
                    <h2>{v.title.length >= 23 ? v.title.slice(0, 23) + '...' : v.title}</h2>           
                  </SliderItem>
              </>
              ))
            }
        </Slider>
    </VideoCardGroupContainer>
    
  )
}

export default Carousel