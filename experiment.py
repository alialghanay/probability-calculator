import copy

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Perform a number of experiments to estimate the probability of drawing certain balls.
    """
    success_count = 0
    for _ in range(num_experiments):
        # Create a copy of the hat for each experiment
        hat_copy = copy.deepcopy(hat)
        
        # Draw a specified number of balls from the hat
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Create a dictionary of drawn balls for comparison
        drawn_balls_count = {}
        for ball in drawn_balls:
            if ball in drawn_balls_count:
                drawn_balls_count[ball] += 1
            else:
                drawn_balls_count[ball] = 1

        # Check if the drawn balls meet or exceed the expected balls
        success = True
        for ball, count in expected_balls.items():
            if drawn_balls_count.get(ball, 0) < count:
                success = False
                break
        
        if success:
            success_count += 1

    # Return the probability as the ratio of successful experiments to total experiments
    return success_count / num_experiments