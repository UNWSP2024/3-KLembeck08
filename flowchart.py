START
    PROMPT for number of people
    PROMPT for hot dogs per person
    CALCULATE total hot dogs needed
--->
    SET dogs per package = 10
    SET buns per package = 8
--->
    CALCULATE dog_packages = CEILING(total_hotdogs / dogs_per_package)
    CALCULATE bun_packages = CEILING(total_hotdogs / buns_per_package)

    CALCULATE leftover dogs = dog packages  10 - total_hotdogs
    CALCULATE leftover buns = bun packages  8 - total_hotdogs
--->
     dog_packages
     bun_packages
     leftover_dogs
    leftoverbuns
END
