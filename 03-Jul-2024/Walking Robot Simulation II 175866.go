# Problem: Walking Robot Simulation II - https://leetcode.com/problems/walking-robot-simulation-ii/

using System;
using System.Collections.Generic;

public class Robot
{
    private static readonly Dictionary<(int, int), string> DIRECTIONS = new Dictionary<(int, int), string>
    {
        {(1, 0), "East"},
        {(0, 1), "North"},
        {(-1, 0), "West"},
        {(0, -1), "South"}
    };

    private int maxX;
    private int maxY;
    private int[] pos;
    private int[] dir;
    private int moves;
    private bool moved;

    public Robot(int width, int height)
    {
        this.maxY = height - 1;
        this.maxX = width - 1;
        this.pos = new int[] { 0, 0 };
        this.dir = new int[] { 0, -1 };
        this.moves = 0;
        this.moved = false;
    }

    public void Step(int num)
    {
        this.moves += num;
        this.moved = true;
    }

    public List<int> GetPos()
    {
        if (this.moves > 0)
        {
            this.Move(this.moves % (2 * (this.maxY) + 2 * this.maxX));
            this.moves = 0;
        }

        return new List<int>(this.pos);
    }

    public string GetDir()
    {
        if (this.moves > 0)
        {
            this.Move(this.moves % (2 * (this.maxY) + 2 * this.maxX));
            this.moves = 0;
        }

        return this.moved ? DIRECTIONS[(this.dir[0], this.dir[1])] : "East";
    }

    private void Move(int num)
    {
        int dx = num * this.dir[0];
        int dy = num * this.dir[1];
        this.pos[0] += dx;
        this.pos[1] += dy;

        if (this.pos[0] > this.maxX || this.pos[0] < 0)
        {
            this.ChangeDirection();

            if (this.pos[0] < 0)
            {
                int overflow = -this.pos[0];
                this.pos[0] = 0;
                this.Move(overflow);
            }
            else
            {
                int overflow = this.pos[0] - this.maxX;
                this.pos[0] = this.maxX;
                this.Move(overflow);
            }
        }
        else if (this.pos[1] > this.maxY || this.pos[1] < 0)
        {
            this.ChangeDirection();

            if (this.pos[1] < 0)
            {
                int overflow = -this.pos[1];
                this.pos[1] = 0;
                this.Move(overflow);
            }
            else
            {
                int overflow = this.pos[1] - this.maxY;
                this.pos[1] = this.maxY;
                this.Move(overflow);
            }
        }
    }

    private void ChangeDirection()
    {
        this.dir[1] *= -1;
        int temp = this.dir[0];
        this.dir[0] = this.dir[1];
        this.dir[1] = temp;
    }
}
