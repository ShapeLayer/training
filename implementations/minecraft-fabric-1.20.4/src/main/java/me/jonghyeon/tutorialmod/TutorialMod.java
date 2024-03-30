package me.jonghyeon.tutorialmod;

import me.jonghyeon.tutorialmod.blocks.ModBlocks;
import me.jonghyeon.tutorialmod.items.ModItemGroups;
import me.jonghyeon.tutorialmod.items.ModItems;
import net.fabricmc.api.ModInitializer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class TutorialMod implements ModInitializer {
	public static final String MOD_ID = "tutorialmod";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

	@Override
	public void onInitialize() {
		ModItemGroups.registerItemGroups();
		ModItems.registerModItems();
		ModBlocks.registerModBlocks();
	}
}
