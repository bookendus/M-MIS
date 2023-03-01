import React from "react";

// Chakra imports
import { Button, Flex, Link, Text } from "@chakra-ui/react";

// Assets
import banner from "assets/img/nfts/NftBanner1.png";

export default function Banner() {
  // Chakra Color Mode
  return (
    <Flex
      direction='column'
      bgImage={banner}
      bgSize='cover'
      py={{ base: "30px", md: "56px" }}
      px={{ base: "30px", md: "64px" }}
      borderRadius='30px'>
      <Text
        fontSize={{ base: "24px", md: "34px" }}
        color='white'
        mb='14px'
        maxW={{
          base: "100%",
          md: "64%",
          lg: "46%",
          xl: "70%",
          "2xl": "50%",
          "3xl": "42%",
        }}
        fontWeight='700'
        lineHeight={{ base: "32px", md: "42px" }}>
        우리 회사의 메타버스 통합 개발 플랫폼 MAXVERSE가
        드디어 세상에 나왔습니다. 
      </Text>
      <Text
        fontSize='md'
        color='#E3DAFF'
        maxW={{
          base: "100%",
          md: "64%",
          lg: "40%",
          xl: "56%",
          "2xl": "46%",
          "3xl": "34%",
        }}
        fontWeight='500'
        mb='40px'
        lineHeight='28px'>
        메타버스 세상을 만들어가는 새로운 방법 MAXVERSE ! 여러분의 많은 관심 부탁드려요.
      </Text>
      <Flex align='center'>
        <a href="https://www.maxverse.io/ko" target="_blank">
        <Button
          bg='white'
          color='black'
          _hover={{ bg: "whiteAlpha.900" }}
          _active={{ bg: "white" }}
          _focus={{ bg: "white" }}
          fontWeight='500'
          fontSize='14px'
          py='20px'
          px='27'
          me='38px'>
          Discover now
        </Button> </a>
        <a href="https://www.youtube.com/watch?v=nNIxOFU_xZ0" target="_blank">
          <Text color='white' fontSize='sm' fontWeight='500'>
            Watch video
          </Text>
        </a>
      </Flex>
    </Flex>
  );
}
