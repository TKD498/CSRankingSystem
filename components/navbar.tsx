"use client";

import { useState } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Menu } from "lucide-react";
import Image from "next/image";

export function NavbarComponent() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <nav className="bg-[#212330] text-white h-[60px] flex items-center">
      <div className="container mx-auto px-4 flex items-center justify-between">
        {/* Logo */}
        <Link href="/" className="text-xl font-bold flex-shrink-0">
          GitLeeted
        </Link>

        {/* Desktop menu items */}
        <div className="hidden md:flex items-center space-x-6 flex-grow justify-center">
          <Link href="/leetcode" className="hover:text-gray-300">
            Leetcode
          </Link>
          <Link href="/github" className="hover:text-gray-300">
            Github
          </Link>
          <Link href="/challenges" className="hover:text-gray-300">
            Challenges
          </Link>
          <Link href="/leaderboard" className="hover:text-gray-300">
            Leaderboard
          </Link>
        </div>

        {/* Login and Signup buttons */}
        <div className="hidden md:flex items-center space-x-4 flex-shrink-0">
          <Button
            variant="outline"
            className="text-white border-white hover:bg-white hover:text-[#212330]"
          >
            Login
          </Button>
          <Button className="bg-white text-[#212330] hover:bg-gray-200">
            Sign Up
          </Button>
        </div>

        {/* Mobile menu button */}
        <div className="md:hidden">
          <Button
            variant="ghost"
            size="icon"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            <Menu className="h-6 w-6" />
            <span className="sr-only">Toggle menu</span>
          </Button>
        </div>
      </div>

      {/* Mobile menu dropdown */}
      {isMenuOpen && (
        <div className="absolute top-[60px] left-0 right-0 bg-[#212330] md:hidden">
          <div className="container mx-auto px-4 py-2 flex flex-col space-y-2">
            <Link href="/leetcode" className="hover:text-gray-300 py-2">
              Leetcode
            </Link>
            <Link href="/github" className="hover:text-gray-300 py-2">
              Github
            </Link>
            <Link href="/challenges" className="hover:text-gray-300 py-2">
              Challenges
            </Link>
            <Link href="/leaderboard" className="hover:text-gray-300 py-2">
              Leaderboard
            </Link>
            <Button
              variant="outline"
              className="text-white border-white hover:bg-white hover:text-[#212330] w-full"
            >
              Login
            </Button>
            <Button className="bg-white text-[#212330] hover:bg-gray-200 w-full">
              Sign Up
            </Button>
          </div>
        </div>
      )}
    </nav>
  );
}
