import React from 'react'
import {Title, VideoCardContainer, VideoCardGroupContainer, SliderItem} from './styles.js'
import Slider from './Slider'
import Button from '../../Button'
import { Link } from 'react-router-dom'

const Carousel = ({ignoreFirstVideo, data}) => {
    const categoryTitle= data.title
    const categoryColor = data.color
    const videos = data.videos

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
        {categoryTitle &&
        <Title style={{backgroundColor: categoryColor}}>
            {categoryTitle}
        </Title>}
        {videos.length === 0 ? (<h2>There're no videos in this category yet ! Help us with a <Button as={Link} className="ButtonLink" to="/register/videos">
        New Video
      </Button></h2>) : null}
        <Slider>
            { videos.map((v, index) => {
                if (ignoreFirstVideo && index === 0) {
                    return null
                }
                return (
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
                    )
                })}
        </Slider>
    </VideoCardGroupContainer>
    
  )
}

export default Carousel